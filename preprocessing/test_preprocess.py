import sys
from preprocess import get_transcript_text, format_transcript

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_preprocess.py <YouTube URL>")
        sys.exit(1)

    url = sys.argv[1]  # Get the URL from the command line
    print(f"Fetching transcript for: {url}")

    # Fetch the transcript using the official API style
    transcript = get_transcript_text(url)

    if transcript is None:
        print("No transcript found")
    else:
        # Format the transcript into a readable string
        text = format_transcript(transcript)
        print(text[:1000])  # Print first 1000 characters
