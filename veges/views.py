from django.shortcuts import render,redirect
from veges.views import *
from veges.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password =  request.POST.get('password')
        
        getusername = User.objects.filter(username = username)
        if not getusername.exists():
            messages.info(request,"Invalid Username")
            return redirect('/login_page/')

        user = authenticate(username = username,password = password)
    
        if user is None:
            messages.info(request,"Invalid Password")
            return redirect('/login_page/')
        else:
            login(request,user)
            return redirect('/recipes/')
        
    return render(request,'Login.html')

def logout_page(request):
    logout(request)
    return redirect('/login_page/')


def Register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        getusername = User.objects.filter(username = username)
        if getusername.exists():
            messages.info(request,"Username already exists")
            return redirect('/Register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()
        
        messages.info(request,"Sucessfully Registered, Welcome to this page!!")
        return redirect('/Register/')

    return render(request,'Register.html')

@login_required(login_url="/login_page/")
def recipes(request):
    if request.method == 'POST':
        recipes = request.POST
        recipe_name = recipes.get('recipe_name')
        recipe_desc = recipes.get('recipe_desc')
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_desc=recipe_desc,
            recipe_image=recipe_image
        )    
        
        return redirect('/recipes/')
    
    querySet = Recipe.objects.all()
    if request.GET.get('search_name'):
        querySet = querySet.filter(recipe_name__icontains = request.GET.get('search_name'))
    

    context = {'Recipes': querySet} 
    return render(request,'recipes.html',context)


def deleteRecipe(request,id):
    getItem = Recipe.objects.get(id = id)
    getItem.delete()
    return redirect('/recipes/')


def updateRecipe(request,id):
    queryItem = Recipe.objects.get(id = id)

    if request.method == "POST":
        recipes = request.POST
        recipe_name = recipes.get('recipe_name')
        recipe_desc = recipes.get('recipe_desc')

        print(queryItem)
        queryItem.recipe_name = recipe_name
        queryItem.recipe_desc = recipe_desc
        
        if request.FILES.get('recipe_image'):
            queryItem.recipe_image=request.FILES.get('recipe_image')

        queryItem.save()
        return redirect('/recipes/')

    context = {'recipe':queryItem}
    return render(request,'update_recipe.html',context)

