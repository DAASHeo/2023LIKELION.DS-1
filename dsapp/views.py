from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, babyLion, failure
from django.utils import timezone
from django.core.paginator import Paginator
from dsapp.forms import ViewBabylionForm
# Create your views here.

def main(request):
    return render(request, '../templates/main.html')

def talk(request):
    posts = Post.objects.filter().order_by('-date')
    comments = Comment.objects.filter().order_by('-date')
    paginator = Paginator(posts,  3)
    page = request.GET.get('page', None)
    if page == None or page == " ":
        page = 1
    posts = paginator.page(page)
    return render(request, 'talk.html', {'posts' : posts, 'comments' : comments})

def create(request):
    if(request.method == 'POST'):                   
        post = Post()                              
        post.content = request.POST['content']
        if post.content == "":
            return redirect('talk')
        else:  
            post.date = timezone.now()
            post.save()                               
    return redirect('talk')

def about(request):
    return render(request, 'about.html')

def org(request):
    return render(request, 'org.html')

def recruit(request):
    return render(request, 'recruit.html')

def babylion(request):
    if request.method == 'POST':
        form = ViewBabylionForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            phone_num = form.cleaned_data.get("phone_num")
            email = form.cleaned_data.get("email")

            passer = babyLion.objects.filter(name=name).filter(phone_num=phone_num).filter(email=email)
            fail = failure.objects.filter(name=name).filter(phone_num=phone_num).filter(email=email)

            return render(request, 'result.html', {'passer':passer, 'fail':fail, 'name':name,})
        
        return redirect('babylion')
    else:
        form = ViewBabylionForm()
    return render(request, 'babylion.html',{'form':form})

def result(request):
    return render(request, 'result.html')