# views.py
from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
    else:
        user_input = ''
    return render(request, 'home.html', {'user_input': user_input})
