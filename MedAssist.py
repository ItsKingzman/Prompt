import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

def med_assist(query):
    prompt = f"Please provide accurate, safe, and context-aware medical information for the following query: {query}"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )

    choice = response.choices[0]

    return choice.text.strip()

# Example queries
query1 = "What are the common symptoms of diabetes?"
query2 = "What are the potential side effects of aspirin?"

print("Query 1:", med_assist(query1))
print("Query 2:", med_assist(query2))
