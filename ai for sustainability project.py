from google import genai

client = genai.Client(api_key="YOUR API KEY")

item = input("Enter the waste item that u have: ")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=f"""
You are an AI Waste Segregation Assistant.

Analyze this waste item:

{item}

Return ONLY these 5 things with their headings:

Category:
Disposal:
Preparation:
Reuse idea:
Eco tip:

Do not include anything else.
"""
)

print(response.text)
