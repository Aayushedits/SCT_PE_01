import ollama

response = ollama.chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "user",
            "content": "Explain the difference between a Python list and tuple in two sentences."
        }
    ]
)

print(response["message"]["content"])