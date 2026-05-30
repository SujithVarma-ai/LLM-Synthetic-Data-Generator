from openai import OpenAI
import pandas as pd

OLLAMA_BASE_URL = "http://localhost:11434/v1"

ollama = OpenAI(
    base_url=OLLAMA_BASE_URL,
    api_key="ollama"
)

data = []

for i in range(100):

    response = ollama.chat.completions.create(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": """
Generate ONE realistic customer review.

Return ONLY in this format:

review text|sentiment

Sentiment must be one of:
Positive
Negative
Neutral

Note that the review text must be exactly 5-12 words and the sentiment must be consistent with the review text. Do not add any additional comments or explanations.
and also make sure there should be equally dustribution of sentiments in the generated reviews. For example, if you generate 100 reviews, there should be around 33 positive, 33 negative and 34 neutral reviews.
Donnot provide heading like negative and dont give 5 to 6 sentneces. Just give one sentence review with sentiment in the format mentioned above.
Example:
The product arrived on time and works perfectly.|Positive

Do not add explanations.
Do not add headings.
"""
            }
        ]
    )

    text = response.choices[0].message.content.strip()

    try:
        review, sentiment = text.split("|")

        data.append({
            "Review": review.strip(),
            "Sentiment": sentiment.strip()
        })

    except:
        print("Skipped:", text)

df = pd.DataFrame(data)

print(df)
print("\nTotal Reviews:", len(df))
print("\nSentiment Distribution:")
print(df["Sentiment"].value_counts())

df.to_csv("synthetic_reviews.csv", index=False)

print("\nSaved to synthetic_reviews.csv")
