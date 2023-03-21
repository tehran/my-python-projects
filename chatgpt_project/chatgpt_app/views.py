from django.shortcuts import render

# Create your views here.
from .forms import ChatForm
from .openai_utils import generate_response

def chat(request):
    chat_history = []
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data["message"]
            response = generate_response(message)
            chat_history = request.POST.getlist("chat_history")
            chat_history.extend([message, response])
            form = ChatForm()
    else:
        form = ChatForm()

    return render(request, "chat.html", {"form": form, "chat_history": chat_history})
