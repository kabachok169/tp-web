from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from ask.models import *
import os


# def index(request):
#     return render(request, 'index.html')

def index(request):

    questions = Question.objects.all()
    questions = paginate(questions, request)

    context = {
        'questions' : questions
    }
    return render(request, 'index.html', context)


def hot_questions(request):

    questions = Question.objects.all()
    questions = paginate(questions, request)

    context = {
        'questions': questions
    }

    return render(request, 'hot_questions.html', context)

def tag(request, tag_name):

    questions = Question.objects.get(tag=tag)
    questions = paginate(questions, request)

    context = {
        'tag': tag_name,
        'questions': questions
    }

    return render(request, 'questions_by_tag.html', context)

def create_question(request):
    return render(request, 'ask.html')

def save_question(request):

    question = Question()
    question.title = request.POST['title']
    question.text = request.POST['text']
    question.likes = 0
    question.dislikes = 0
    #question.user = request.user
    question.save()

    return redirect("index")


def one_question(request, question_id):

    question = {
        'title': 'title ' + str(question_id),
        'id': 1,
        'text': 'text 1',
        'likes': 1,
        'answers': 2,
        'tags': ['i+1', 'i+2'],
    }

    context = {
        'question' : question
    }

    return render(request, 'question.html', context)

def settings(request):
    return render(request, 'settings.html')

def login(request):
    return render(request, 'login.html')

def login_confirm(request):
    login = request.POST['login']
    password = request.POST['pass']
    user = auth.authenticate(username=login, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect("index")

def logout(request):
    auth.logout(request)
    return redirect("login")

def registrate(request):
    return render(request, 'registration.html')

def registration_confirm(request):

    user = User.objects.create_user(username=request.POST['login'],
                                    email=request.POST['email'],
                                    password=request.POST['pass'])

    profile = Profile(user=user)
    profile.save()
    user.save()
    return redirect("index")


def paginate(objects_list, request):

    paginator = Paginator(objects_list, 3)

    try:
        questions = paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(2)

    return questions