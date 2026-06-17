from django.shortcuts import render,redirect
from . models import tasks
# Create your views here.
def todofn(request):
    item=tasks.objects.all()
    if request.method == 'POST':
        a=request.POST.get('task')
        b=request.POST.get('date')
        tasks.objects.create(task=a,deadline=b)
        return redirect('task')
    return render(request,'todoo.html',{'item':item})
def dlt_task(request,id):
    a=tasks.objects.filter(id=id)
    a.delete()
    return redirect('task')
def update_task(request,id):
    a=tasks.objects.get(id=id)
    if request.method=="POST":
        a.task=request.POST.get('task')
        a.deadline=request.POST.get('date')
        a.save()
        return redirect('task')
    return render(request,'update.html',{'a':a})
