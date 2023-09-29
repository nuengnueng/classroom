from django.shortcuts import render, redirect
from classroom.models import *
from classroom.form import *

scoreList = []
def home(request):
    if request.method == 'POST':
        selected_name = request.POST.get('name1')  # รับค่าจาก select name1
        selected_course = request.POST.get('course')  # รับค่าจาก select course
        score = request.POST.get('score')  # รับค่าจาก input score
        print(selected_name)
        tempList = []
        tempList.append(selected_name)
        tempList.append(selected_course)
        tempList.append(score)
        scoreList.append(tempList)
        print(scoreList)

    dog =  Course.objects.all()
    data = Student.objects.all()
    return render(request, 'classroom/home.html', {'data': data, 'dog': dog})
def stream(req):
    return render(req, 'pages/stream.html')
def classwork(req):
    return render(req, 'pages/classwork.html')
def people(req):
    return render(req, 'pages/people.html')
def grade(req):
            
    return render(req, 'pages/grade.html',{'scoreList':scoreList})
def menu(req):
    return render(req, 'pages/menu.html')


