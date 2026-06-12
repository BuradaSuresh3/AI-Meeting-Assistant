import ollama

print("Sending request...")

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": "Summarize this meeting in one sentence."
        }
    ]
)

print(response["message"]["content"])