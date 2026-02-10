import faiss
import numpy as np
import pickle

class FaissVectorStore:
    def __init__(self, embedding_dim, index_path=None):
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatL2(embedding_dim)  # L2 distance
        self.texts = []  # Keep track of chunks for retrieval
        self.index_path = index_path

    def add_embeddings(self, chunks, embeddings):
        """
        chunks: list of text chunks
        embeddings: np.array of shape (num_chunks, embedding_dim)
        """
        self.index.add(np.array(embeddings, dtype='float32'))
        self.texts.extend(chunks)

    def query(self, query_embedding, top_k=5):
        """
        query_embedding: np.array of shape (1, embedding_dim)
        Returns: top-k chunks and their distances
        """
        D, I = self.index.search(np.array([query_embedding], dtype='float32'), top_k)
        results = [self.texts[i] for i in I[0]]
        return results, D[0]

    def save(self, index_path=None, metadata_path=None):
        """Save FAISS index and chunk texts to disk"""
        index_path = index_path or self.index_path or "faiss.index"
        metadata_path = metadata_path or "faiss_texts.pkl"
        faiss.write_index(self.index, index_path)
        with open(metadata_path, "wb") as f:
            pickle.dump(self.texts, f)

    def load(self, index_path=None, metadata_path=None):
        """Load FAISS index and chunk texts from disk"""
        index_path = index_path or self.index_path or "faiss.index"
        metadata_path = metadata_path or "faiss_texts.pkl"
        self.index = faiss.read_index(index_path)
        with open(metadata_path, "rb") as f:
            self.texts = pickle.load(f)
