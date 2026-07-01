import glob
import os
import shutil

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


class FootballRAG:

    def __init__(self):

        self.data_folder = "data/*.pdf"

        self.persist_directory = "vector_db"

        self.skip_pages = {

            "laws_of_the_game.pdf": 4,

            "football_intelligence_and_tactics.pdf": 12,

            "fifa_world_cup_regulations.pdf": 6,

            "uefa_champions_league_regulations.pdf": 3,

            "fifa_world_cup_history.pdf": 1,

            "fifa_world_cup_anecdotes.pdf": 1

        }

        self.embeddings = HuggingFaceEmbeddings(

            model_name="sentence-transformers/all-MiniLM-L6-v2",

            model_kwargs={
                "device": "cpu"
            },

            encode_kwargs={
                "normalize_embeddings": True
            }

        )

    # -------------------------------------------------------

    def clean_documents(self, documents):

        cleaned = []

        removed = 0

        for doc in documents:

            source = doc.metadata.get("source", "")

            page = doc.metadata.get("page", 0)

            text = doc.page_content.strip()

            # Skip first pages for each PDF
            if page < self.skip_pages.get(source, 0):

                removed += 1
                continue

            # Skip almost empty pages
            if len(text) < 80:

                removed += 1
                continue

            cleaned.append(doc)

        print(f"\n🧹 Removed {removed} pages")
        print(f"✅ Remaining pages : {len(cleaned)}")

        return cleaned

    # -------------------------------------------------------

    def build_database(self):

        print("=" * 60)
        print("⚽ Building Football Knowledge Base")
        print("=" * 60)

        documents = []

        pdf_files = sorted(glob.glob(self.data_folder))

        print(f"\n📂 Found {len(pdf_files)} PDF(s)\n")

        for pdf in pdf_files:

            filename = os.path.basename(pdf)

            print(f"📖 Loading: {filename}")

            loader = PyPDFLoader(pdf)

            docs = loader.load()

            for doc in docs:

                doc.metadata["source"] = filename

            documents.extend(docs)

        print(f"\n✅ Loaded {len(documents)} pages")

        documents = self.clean_documents(documents)

        print("\n✂️ Splitting into chunks...")

        splitter = RecursiveCharacterTextSplitter(

            chunk_size=800,

            chunk_overlap=150,

            separators=[

                "\n\n",

                "\n",

                ". ",

                " ",

                ""

            ]

        )

        chunks = splitter.split_documents(documents)

        print(f"✅ Created {len(chunks)} chunks")

        if os.path.exists(self.persist_directory):

            shutil.rmtree(self.persist_directory)

        print("\n🧠 Creating Vector Database...")

        vector_db = Chroma.from_documents(

            documents=chunks,

            embedding=self.embeddings,

            persist_directory=self.persist_directory

        )

        print("\n🎉 Football Knowledge Base Ready!")

        print("=" * 60)

        return vector_db

    # -------------------------------------------------------

    def load_database(self):

        self.vector_db = Chroma(

            persist_directory=self.persist_directory,

            embedding_function=self.embeddings

        )

        self.retriever = self.vector_db.as_retriever(

            search_type="mmr",

            search_kwargs={

                "k": 4,

                "fetch_k": 20,

                "lambda_mult": 0.7

            }

        )

        print("✅ Vector database loaded.")

    # -------------------------------------------------------

    def retrieve(self, query):

        return self.retriever.invoke(query)