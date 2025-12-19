import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class FAQRetriever:
    def __init__(self, chunks: list[str]):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.chunks = chunks
        self.embeddings = self.model.encode(chunks)
        
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))

    def search(self, query: str, threshold=1.0):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, 1)

        distance = distances[0][0]
        idx = indices[0][0]

        if distance > threshold:
            return None, distance

        return self.chunks[idx], distance

