from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Post
from articles.forms import ContactForm

def homepage(request):
    latests_posts = Post.objects.order_by('-timestamp')[0:3]

    context = {
        'latests': latests_posts
    }

    return render(request, 'homepage.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            form = ContactForm()
    
    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact.html', context)
