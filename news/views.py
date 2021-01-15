from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserForm
from django.contrib.auth import authenticate, login as dj_login, logout
import requests
from bs4 import BeautifulSoup
from .models import Article, Category

# Create your views here.

def scrape(request):
  

    # tech Category
    # from TechCruch
    r = requests.get('https://techcrunch.com/startups/')
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent,'html5lib'                             )
    techcruch_title = soup.find_all('header', class_="post-block__header")
    for titles in techcruch_title:
        techcruch_headline = titles.find('a', class_="post-block__title__link")
        techcruch_headline = techcruch_headline.text.strip()
        techcruch_link_url = titles.find('a')['href']
        category = Category()
        category.name = "Tech"
        category.save()
        article = Article()
        article.title = techcruch_headline
        article.category = "Tech"
        article.save()
        
    print("Data scrap done")
       
        
     
    
    #print(techcruch_headline.text.strip())
    #print(techcruch_link_url.strip())

       # from Digital Trends
    r = requests.get('https://www.digitaltrends.com/')
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html5lib')
    dg_title = soup.find_all('div', class_="b-meta b-snippet__meta b-snippet--2-2__meta")
    for wired_titles in dg_title:
        dg_headline = wired_titles.find('a', class_="b-snippet__hot")
        category1 = Category()
        category1.category = "Tech"
        category1.save()
        article1 = Article()
        article1.title = dg_headline
        article1.name = "Tech"
        article1.save()
    
        

    #print(dg.text.strip())


#Sport
# ESPN
   # r = requests.get('https://www.espn.in/')
   # htmlcontent = r.content
    #soup = BeautifulSoup(htmlcontent, 'html5lib')
    #espn_title = soup.find_all('section', class_="contentItem__content contentItem__content--story has-image has-video contentItem__content--collection")
    #for wired_titles in espn_title:
       # espn_headline = wired_titles.find('h1', class_="contentItem__title contentItem__title--story")
        #print(espn_headline)
        #category2 = Category()
        #category2.name = "Sport"
        #category2.save()
        #article2 = Article()
        #article2.title = espn_headline
        #article2.category = "Sport"
        #article2.save()
        
        

    #print(espn_headline.text.strip())

#Sky Sport
    r = requests.get('https://www.skysports.com/football/news')
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html5lib')
    sky_title = soup.find_all('div', class_="news-list__body")
    for sky_titles in sky_title:
        sky_headline = sky_titles.find('a', class_="news-list__headline-link")
        category3 = Category()
        category3.category = "Sport"
        category3.save()
        article3 = Article()
        article3.title = sky_headline
        article3.name = "Sport"
        article3.save()
    return redirect('index')

    print(sky_headline.text.strip())













def index(request):
    article = Article.objects.all()
    content = {'ar': article}
    return render(request, 'layouts/index.html', content)

def main(request):
    article = Article.objects.all()
    content = {'ar': article}
    return render(request, 'User/home.html', content)



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Accout Created Succefully')
            return redirect('register')

    else:
        form = CustomUserCreationForm
    context = {'form':form}
    return render(request, 'authencation/register.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
                dj_login(request, user)
                return redirect('main')
        
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
        
    form = CustomUserCreationForm()
    context = {'form':form}

    return render(request, 'authencation/login.html', context)
    
   
    


                   



   

        

