import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8,
    )

    return response.choices[0].text.strip()
