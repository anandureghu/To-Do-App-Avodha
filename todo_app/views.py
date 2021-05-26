from django.shortcuts import render, redirect
from .models import ToDo
from .forms import UpdateForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class TaskListView(ListView):
    model = ToDo
    template_name = 'home.html'
    context_object_name = 'tasks'
    
    
class TaskDetailView(DetailView):
    model = ToDo
    template_name = 'details.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = ToDo
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('subject', 'priority', 'date')
    def get_success_url(self):
        return reverse_lazy('todo_app:details', kwargs={'pk': self.object.id})




def add_new_todo(request):
    if request.method == "POST":
        subject = request.POST['subject']
        priority = request.POST['priority']
        date = request.POST['date']
        tasks = ToDo(subject=subject, priority=priority, date=date)
        tasks.save()
        return redirect('todo_app:home')

# def details(request, id):
#     task = ToDo.objects.get(id=id)
#     return render(request, 'details.html', {"task": task})

# def update(request, id):
#     task = ToDo.objects.get(id=id)
#     if request.method == "POST":
#         task.subject = request.POST['subject']
#         task.priority = request.POST['priority']
#         task.date = request.POST['date']
#         task.save()
#         return redirect('todo_app:home')
#     return render(request, 'update.html', {'task': task})


def delete(request, id):
    if request.method == "POST":
        task = ToDo.objects.get(id=id)
        task.delete()
        return redirect('todo_app:home')
