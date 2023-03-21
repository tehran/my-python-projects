Update your settings.py file in the chatgpt_project folder to include the OpenAI API key:

# Add this line at the end of the file
OPENAI_API_KEY = "your_api_key_here"


python manage.py migrate

python manage.py runserver