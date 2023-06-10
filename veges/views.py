from django.shortcuts import render,redirect
from veges.views import *
from veges.models import *
# Create your views here.

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

