import sys
import numpy as np
from sentence_transformers import SentenceTransformer

from preprocessing.preprocess import get_transcript_text, format_transcript
from preprocessing.chunking import chunk_text
from vectorstore.faiss_store import FaissVectorStore
from llm import get_llm


def build_vector_store(url, embedder):
    print(f"\nFetching transcript for: {url}")

    transcript = get_transcript_text(url)
    if transcript is None:
        print("No transcript found for this video.")
        return None

    text = format_transcript(transcript)
    chunks = chunk_text(text)

    print(f"Created {len(chunks)} chunks")
    print("Generating embeddings...")

    embeddings = embedder.encode(chunks, convert_to_numpy=True)

    store = FaissVectorStore(embeddings.shape[1])
    store.add_embeddings(chunks, embeddings)

    print("Vector store ready!")
    return store


def qa_loop(store, llm, embedder, top_k=4):
    print("\nYou can now ask questions about this video.")
    print("Type 'new' to load another video, or 'exit' to quit.\n")

    while True:
        question = input(" Your question: ").strip()

        if question.lower() == "exit":
            sys.exit(0)

        if question.lower() == "new":
            return  # break QA loop and ask for new URL

        # Embed question
        q_embedding = embedder.encode([question], convert_to_numpy=True)

        # Retrieve relevant chunks
        chunks, distances = store.query(q_embedding[0], top_k=top_k)
        context = "\n".join(chunks)

        # Generate answer
        answer = llm.generate_answer(context, question)

        print("\n Answer:")
        print(answer)
        print("-" * 60)


def main():
    print("YouTube Video QA Bot (Local LLaMA + FAISS)\n")

    # Load models once
    print("Loading embedding model...")
    embedder = SentenceTransformer("all-MiniLM-L6-v2")

    print("Loading local LLM...")
    llm = get_llm("llama2")

    while True:
        url = input("\n Enter YouTube URL (or 'exit'): ").strip()

        if url.lower() == "exit":
            break

        store = build_vector_store(url, embedder)
        if store is None:
            continue

        qa_loop(store, llm, embedder)


if __name__ == "__main__":
    main()
