from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'./home.html')
def chat_view(request, user1,user2):
    return render(request, 'chat.html', {
        'user1': user1,
        'user2': user2
    })

