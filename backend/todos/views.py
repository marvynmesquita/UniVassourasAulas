from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Todo
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")
