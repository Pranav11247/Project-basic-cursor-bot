from openai import OpenAI

client = OpenAI(
    api_key="",
    base_url="https://api.sambanova.ai/v1",
)

response = client.chat.completions.create(
    model="Llama-4-Maverick-17B-128E-Instruct",
    messages=[{"role": "user", "content": "tell me a joke"}],
    temperature=0.1,
    top_p=0.1,
)

print(response.choices[0].message.content)
