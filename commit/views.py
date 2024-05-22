from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Display
from .forms import Display_Form

# Create your views here.
def index(request):
    if request.method == "POST":
        form= Display_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect(form.errors.as_json())
    posts= Display.objects.all().order_by('-created_at')[:20]
    return render(request,'http.html',{"posts":posts})    

def delete(request, post_id):
    post= Display.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect("/")
def edit(request, post_id):
    post= Display.objects.get(id=post_id)
    if request.method == "POST":
        form= Display_Form(request.POST, request.FILES,instance=post )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    return render(request, 'edit.html', {"post":post} ) 

def like_view(request, post_id):
    post= Display.objects.get(id=post_id)
    new_like_count= post.likes +1
    post.likes=new_like_count
    post.save()
    return HttpResponseRedirect('/')