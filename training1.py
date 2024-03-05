from litellm import completion

reponse = completion(
model="ollama/llama2",
messages=[{ "content": "répondez en 20 mots. Où est ma faute d'ortographe ?", "role": "user"}],
api_base="http://localhost:11434"
)

print(reponse)