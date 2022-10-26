from django.shortcuts import redirect, render
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def articles(request):
  articles = Article.objects.all().order_by('date')
  return render(request, 'articles/articles.html', { 'title': 'Articles', 'articles': articles })

def article(request, slug):
  article = Article.objects.get(id=int(slug))
  return render(request, 'articles/article.html', { 'title': 'Article', 'article': article })

@login_required(login_url="/accounts/login")
def article_create(request):
  if request.method == 'POST':
    form = forms.CreateArticle(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.author = request.user
      instance.save()
      return redirect('/articles/')
  else:  
    form = forms.CreateArticle()
  return render(request, 'articles/create.html', { 'title': 'Create', 'form': form })
