from django.shortcuts import render

# Create your views here.
def chat(request):
       return render (request,'chatapp/chat.html')