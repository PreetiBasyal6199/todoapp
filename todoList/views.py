from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from .forms import todoForm
from .models import todoList

# Create your views here.
def index(request):
    todo_list=todoList.objects.order_by('date')
    if request.method =="POST":
        form=todoForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect('')
    form=todoForm()
    context={
        'form':form,
        'items':todo_list

    }
    return render(request,'home.html',context)

def delete_item(request,id):
    todo_item=todoList.objects.get(pk=id)
    todo_item.delete()
    items=todoList.objects.all()
    form=todoForm()
    context={
        'form':form,
        'items':items

    }
    return render(request,'home.html',context)
def add_item(request):
    if request.method =="POST":
        form=todoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    form=todoForm()
    context={
        'form':form,
       

    }
    return render(request,'add.html',context)

def edit_item(request,pk):
    get_data=get_object_or_404(todoList,pk=pk)
    form=todoForm(instance=get_data)
    if request.method=="POST":
        form=todoForm(data=request.POST,instance=get_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request,'edit.html',{'form':form})