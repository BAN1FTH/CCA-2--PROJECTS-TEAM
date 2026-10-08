# Name: Your Full Name
# PRN: Your PRN Number

from transformers import pipeline

# Load the free sentiment analysis model from Hugging Face
sentiment_analyzer = pipeline("sentiment-analysis")

# ========== PROBLEM STATEMENTS ==========
# 1. Basic customer review
# 2. Social media tweet
# 3. Product feedback
# 4. Student feedback about college
# 5. Movie review

texts = [
    "I absolutely love this product, best purchase ever!",
    "This is the worst service I have ever experienced. Never again.",
    "The delivery was okay, nothing special.",
    "MIT-WPU is a great place to study, teachers are helpful.",
    "The movie was so boring I fell asleep halfway."
]

print("===== Hugging Face Sentiment Monitor =====\n")

for text in texts:
    result = sentiment_analyzer(text)[0]
    print(f"Text: {text}")
    print(f"Sentiment: {result['label']} (confidence: {result['score']:.2f})")
    print("-" * 60)
