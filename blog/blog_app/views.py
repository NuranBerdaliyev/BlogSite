from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'blog_app/main.html')
def about(request):
    return render(request, 'blog_app/about.html')
