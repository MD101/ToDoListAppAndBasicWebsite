from django.shortcuts import render, redirect
from .models import Category_of_List, Listing
from django.forms import modelform_factory

# Create your views here.
ListForm = modelform_factory(Listing, exclude=[])

def Tasks(request):
    cat_list = Category_of_List.objects.all()
    lists = Listing.objects.all()
    print(request.POST)

    if request.method == "POST":
        if "taskDelete" in request.POST:

            if "checkedbox" not in request.POST:
                return redirect("listing")
            else:
                checkedList = request.POST["checkedbox"]
                print(checkedList)
                print(type(checkedList))
                todo = Listing.objects.get(id=int(checkedList))
                todo.delete()
                
        title = request.POST["title"]
        date  = str(request.POST["due_date"])
        category = request.POST["category"]
        content = title + "---" + category + "---" + date + "---" + request.POST["description"]
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listing")


    else:
        form = ListForm()

    return render(request, "index.html", {"cat_list":cat_list, "lists":lists, "form":form})
