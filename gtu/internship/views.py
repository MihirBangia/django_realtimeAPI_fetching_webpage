from django.shortcuts import render
import requests

def index(request):
    records={}
    url="https://inshorts.deta.dev/news?category="
    response= requests.get(url=url)
    inshorts_data = response.json()
    records['indexfile']= inshorts_data
    return render(request,'index.html',records)

def sports(request):
    records={}
    url = "https://inshorts.deta.dev/news?category=sports"
    response = requests.get(url=url)
    inshorts_data= response.json()
    records['sports']= inshorts_data
    return render(request,'sports.html',records)

def buisness(request):
    records={}
    url = "https://inshorts.deta.dev/news?category=business"
    response = requests.get(url=url)
    inshorts_data= response.json()
    records['buisness']= inshorts_data
    return render(request,'buisness.html',records)

def technology(request):
    records={}
    url = "https://inshorts.deta.dev/news?category=technology"
    response = requests.get(url=url)
    inshorts_data= response.json()
    records['technology']= inshorts_data
    return render(request,'technology.html',records)

def entertainment(request):
    records={}
    url = "https://inshorts.deta.dev/news?category=entertainment"
    response = requests.get(url=url)
    inshorts_data= response.json()
    records['entertainment']= inshorts_data
    return render(request,'entertainment.html',records)

def politics(request):
    records={}
    url = "https://inshorts.deta.dev/news?category=politics"
    response = requests.get(url=url)
    inshorts_data= response.json()
    records['politics']= inshorts_data
    return render(request,'politics.html',records)