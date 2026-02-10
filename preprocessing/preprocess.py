import re
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled

def get_video_id(url):
    """
    Extract the video ID from a YouTube URL.
    Supports standard YouTube watch URLs.
    """
    # Try to extract with regex
    pattern = r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_transcript_text(url):
    """
    Fetches the raw transcript for a YouTube video as a list of dictionaries.
    Returns None if no transcript is available or an error occurs.
    Uses the official 'fetch' method as documented on PyPI.
    """
    video_id = get_video_id(url)
    if not video_id:
        print("DEBUG: Could not extract video ID")
        return None

    try:
        # Official simple fetch call from the library docs
        ytt_api = YouTubeTranscriptApi()
        transcript_data = ytt_api.fetch(video_id, languages=["en"])
    except NoTranscriptFound:
        print("DEBUG: No transcript found for this video")
        return None
    except TranscriptsDisabled:
        print("DEBUG: Transcripts are disabled for this video")
        return None
    except Exception as e:
        print("DEBUG: Unexpected error:", e)
        return None

    return transcript_data

def format_transcript(transcript):
    """
    Turns the fetched transcript into a single string with timing info.
    """
    if not transcript:
        return ""

    txt = ""
    for snippet in transcript:
        try:
            txt += f"Text: {snippet.text} Start: {snippet.start}\n"
        except AttributeError:
            try:
                txt += f"Text: {snippet['text']} Start: {snippet['start']}\n"
            except Exception:
                pass
    return txt
