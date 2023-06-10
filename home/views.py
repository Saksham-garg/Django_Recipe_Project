from django.shortcuts import render

# Create your views here.

def home(request):
    peoples = [
        {'name':'Saksham garg','age':21},
        {'name':'Abhijeet Singh','age':23},
        {'name':'Rahul Chawla','age':12},
        {'name':'Suresh Kumar','age':43},
        {'name':'Golu tripathi','age':54},
    ]
    context = {'peoples':peoples}
    return render(request,'home/index.html',context)

def about(request):
    return render(request,'home/about.html',context={'data':'This is page data'})