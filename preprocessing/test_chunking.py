from preprocess import get_transcript_text, format_transcript
from chunking import chunk_text
import sys

if __name__ == "__main__":
    # Get URL from command line or use a default
    url = sys.argv[1] if len(sys.argv) > 1 else "Not enough arguments provided"

    # Fetch the transcript
    transcript = get_transcript_text(url)

    if transcript is None:
        print("No transcript found")
    else:
        # Format the transcript into a single string
        text = format_transcript(transcript)

        # Chunk the transcript
        chunks = chunk_text(text)

        # Print first 100 characters of each chunk
        for i, c in enumerate(chunks):
            print(f"Chunk {i+1}: {c[:100]}...\n")
