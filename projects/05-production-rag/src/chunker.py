


def chunk_by_paragraph(document_text):

    chunks = [
        paragraph.strip() 
        for paragraph in document_text.split("\n\n") 
        if paragraph.strip()
    ]

    return chunks

def chunk_by_paragraph_with_limit(document_text, max_words=30):

    paragraphs = [
        p.strip()
        for p in document_text.split("\n\n")
        if p.strip()
    ]

    chunks = []

    current_chunk = []
    current_word_count = 0

    for paragraph in paragraphs:

        paragraph_word_count = len(paragraph.split())

        if(current_word_count + paragraph_word_count > max_words and current_chunk):
            chunks.append("\n\n".join(current_chunk))
        
            current_chunk = []
            current_word_count = 0
        
        current_chunk.append(paragraph)
        current_word_count += paragraph_word_count

    if current_chunk:
        chunks.append("\n\n".join(current_chunk))

    return chunks


def chunk_with_overlap(text, chunk_size=30, overlap=2):

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):
        
        end = start + chunk_size
        
        chunk = words[start:end]
        
        chunks.append("\n\n".join(chunk))

        start += (chunk_size - overlap)

    return chunks