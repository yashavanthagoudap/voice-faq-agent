from pypdf import PdfReader

def load_faq_text(pdf_path: str) -> list[str]:
    reader = PdfReader(pdf_path)
    pages = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)

    return pages


def chunk_text(texts, chunk_size=300):
    chunks = []
    for text in texts:
        words = text.split()
        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i + chunk_size])
            chunks.append(chunk)
    return chunks
