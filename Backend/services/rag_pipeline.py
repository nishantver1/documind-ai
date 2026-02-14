from services.chunker import chunk_text
from services.embeddings import create_embeddings
from services.vector_db import build_faiss_index, similarity_search
from services.question_generator import ask_llm


from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def process_document(text):
    chunks = chunk_text(text)
    embeddings = create_embeddings(chunks)
    build_faiss_index(embeddings, chunks)

def ask_question(question):
    q_embedding = model.encode([question])
    relevant_chunks = similarity_search(q_embedding)
    context = "\n".join(relevant_chunks)

    return ask_llm(context, question)

