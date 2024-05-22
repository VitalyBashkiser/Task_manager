from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from tasks.models import Task, Tag
from tasks.forms import TaskForm, TagForm


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all().order_by('is_done', '-created_at')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:task-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Task'
        return context


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:task-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Task'
        return context


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:task-list')


class TaskToggleStatusView(View):
    def get(self, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect('task-list')


class TagListView(ListView):
    model = Tag
    template_name = 'tasks/tag_list.html'
    context_object_name = 'tags'


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tasks/tag_form.html'
    success_url = reverse_lazy('tasks:tag-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Tag'
        return context


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'tasks/tag_form.html'
    success_url = reverse_lazy('tasks:tag-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Tag'
        return context


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'tasks/tag_confirm_delete.html'
    success_url = reverse_lazy('tasks:tag-list')
