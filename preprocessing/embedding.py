from sentence_transformers import SentenceTransformer

# Initialize the local model
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks):
    """
    Accepts a list of text chunks and returns a list of embeddings.
    """
    embeddings = model.encode(chunks, show_progress_bar=True)
    return embeddings
