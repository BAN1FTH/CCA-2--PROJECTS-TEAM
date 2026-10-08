# Name: Your Full Name
# PRN: Your PRN Number

# Simple fake RAG example (no heavy libraries needed)

knowledge_base = {
    "what is github": "GitHub is a website to store and share code with others.",
    "what is sentiment analysis": "Sentiment analysis detects if text is positive, negative or neutral.",
    "what is hugging face": "Hugging Face provides free ready-made AI models.",
    "what is machine learning": "Machine learning is when computers learn patterns from data."
}

# Extra rules I added
rules = [
    "Always answer politely",
    "If you don't know, say 'I don't know'",
    "Keep answers short and clear"
]

def rag_answer(question):
    question = question.lower()
    for key in knowledge_base:
        if key in question:
            return knowledge_base[key]
    return "I don't know the answer to that."

print("===== Simple RAG System =====")
print("Rules:", rules)
print()

questions = [
    "What is GitHub?",
    "What is sentiment analysis?",
    "Who is the president of India?"
]

for q in questions:
    print(f"Question: {q}")
    print(f"Answer: {rag_answer(q)}")
    print("-" * 40)
