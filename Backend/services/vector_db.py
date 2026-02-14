import faiss
import numpy as np

index = None
stored_chunks = []

def build_faiss_index(embeddings, chunks):
    global index, stored_chunks

    embeddings = np.array(embeddings).astype("float32")
    dimension = embeddings.shape[1]

    # if index not created yet
    if index is None:
        index = faiss.IndexFlatL2(dimension)

    # add new embeddings (not replace)
    index.add(embeddings)

    # store chunks also
    stored_chunks.extend(chunks)


def similarity_search(query_embedding, k=4):
    if index is None:
        return ["No document uploaded yet"]

    distances, indices = index.search(query_embedding, k)
    return [stored_chunks[i] for i in indices[0]]
