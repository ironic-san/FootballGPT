from rag import FootballRAG

rag = FootballRAG()

rag.load_database()

question = input("Ask a football question: ")

results = rag.retrieve(question)

for i, doc in enumerate(results, start=1):

    print("\n" + "=" * 70)

    print(f"Result {i}")

    print(f"Source : {doc.metadata.get('source')}")

    print(f"Page   : {doc.metadata.get('page_label')}")

    print("-" * 70)

    print(doc.page_content[:900])