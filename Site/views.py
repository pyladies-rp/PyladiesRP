from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def pyladies(request):
    return render(request, 'members/pyladies_list.html', {})

def about(request):
    return render(request, 'about/about.html', {})

def contact(request):
    return render(request, 'contact/contact.html', {})
