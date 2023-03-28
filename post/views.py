from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from post.models import article, Category, Comment, contact_us, User
from django.core.paginator import Paginator
from .forms import ContactusForm,add_article
from django.views.generic.base import View,TemplateView
from django.views.generic import ListView
import os

def post(request,slug):
    Article=get_object_or_404(article,slug=slug)
    if request.method=="POST":
        parent_id=request.POST.get('parent_id')
        body=request.POST.get('body')
        Comment.objects.create(body=body,Article=Article,user=request.user,parent_id=parent_id)
    return render(request, "post/article-details.html", {"Article":Article})


def post_list(request):
    Article = article.objects.all()
    page_number=request.GET.get('page')
    paginator=Paginator(Article,1)
    object_list=paginator.get_page(page_number)
    recent_article=article.objects.all().order_by("-created")
    category=Category.objects.all()
    return render(request,"post/Articles_list.html",{"Article":object_list,"recent_articles":recent_article,"category":category})
def category_detail(request,pk):
    category=get_object_or_404(Category,id=pk)
    Article=category.article_set.all()
    return render(request,"post/Articles_list.html",{"Article":Article})

def search(request):
    q=request.GET.get('q')
    Article=article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(Article, 1)
    object_list = paginator.get_page(page_number)
    return render(request,"post/Articles_list.html",{"Article":object_list})

def contactus(request):
    if request.method=="POST":
        form=ContactusForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            l_name=form.cleaned_data['l_name']
            phone=form.cleaned_data["phone"]
            Email=form.cleaned_data['Email']
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']
            contact_us.objects.create(name=name,l_name=l_name,Email=Email,phone=phone,title=title,description=description)

    else:
        form=ContactusForm()
    return render(request,"post/contact_us.html",{"form":form})

#class TestBaseView(View):
#    name="amir"
#    def hello(self,request):
#        return HttpResponse(self.name)

def AddArticle(request):
    if request.method=="POST":
        form=add_article(request.POST,request.FILES)
        if form.is_valid():
            #author=form.cleaned_data['author']
            #category=form.cleaned_data['category']
            title=form.cleaned_data["title"]
            body=form.cleaned_data['body']
            image=form.cleaned_data['image']
            #created=form.cleaned_data['created']
            #updated=form.cleaned_data['updated']
            slug=form.cleaned_data['slug']
            article.objects.create(author=request.user,title=title,body=body,image=image,slug=slug)
    else:
        form=add_article()
    return render(request,"post/add_article.html",{"form":form})



def profile(request):
    Article=article.objects.filter(author=request.user)
    return render(request,"post/profile.html",{"Article":Article})






class ArticleList(TemplateView):
    template_name = "post/Articles_list.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["Article"]=article.objects.all()
        return context
