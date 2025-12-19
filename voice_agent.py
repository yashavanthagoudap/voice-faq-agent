import os
from pdf_loader import load_faq_text, chunk_text
from retriever import FAQRetriever
from transcript import Transcript


OUT_OF_SCOPE_MSG = (
    "I’m sorry, I couldn’t clearly understand that. "
    "Could you please repeat or rephrase your question?"
)

class VoiceAgent:
    def __init__(self, pdf_dir="data"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, pdf_dir)

        pdf_files = [f for f in os.listdir(data_dir) if f.lower().endswith(".pdf")]
        if not pdf_files:
            raise FileNotFoundError(f"No PDF found in {data_dir}")

        pdf_path = os.path.join(data_dir, pdf_files[0])

        texts = load_faq_text(pdf_path)
        chunks = chunk_text(texts)

        self.retriever = FAQRetriever(chunks)
        self.transcript = Transcript()

    def handle_query(self, user_text: str) -> str:
        if not user_text.strip():
            self.transcript.add_agent(OUT_OF_SCOPE_MSG)
            return OUT_OF_SCOPE_MSG

        self.transcript.add_user(user_text)

        answer, distance = self.retriever.search(user_text)

        # 1️⃣ Strong match → answer
        if answer and distance < 0.7:
            final_answer = extract_direct_answer(answer)
            self.transcript.add_agent(final_answer)
            return final_answer

        # 2️⃣ Weak match → ask to repeat
        if answer and 0.7 <= distance <= 1.2:
            self.transcript.add_agent(OUT_OF_SCOPE_MSG)
            return OUT_OF_SCOPE_MSG

        # 3️⃣ No match → out of scope
        self.transcript.add_agent(OUT_OF_SCOPE_MSG)
        return OUT_OF_SCOPE_MSG



def extract_direct_answer(text: str) -> str:
    for line in text.split("."):
        if "will remain in effect" in line.lower():
            return line.strip() + "."
    return text.strip()

