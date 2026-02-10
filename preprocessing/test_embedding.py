from preprocess import get_transcript_text, format_transcript
from chunking import chunk_text
from embedding import embed_chunks
import sys

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "Not enough arguments provided"
    
    # Fetch and format transcript
    transcript = get_transcript_text(url)
    if transcript is None:
        print("No transcript found")
        exit()

    text = format_transcript(transcript)

    # Chunk transcript
    chunks = chunk_text(text)

    # Create embeddings
    embeddings = embed_chunks(chunks)

    print(f"Created embeddings for {len(chunks)} chunks")
    print(f"Example embedding (first 5 values): {embeddings[0][:5]}")
