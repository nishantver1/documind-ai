def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    print(words)
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
        print(chunk)

    return chunks
print(chunk_text("i am noob hello",2,1))