from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from stdapp.forms import Customform, studentform, teacherform, marksaddform
from stdapp.models import teacher, student, marksadd


# Create your views here.

def homepage(request):
    return render(request,'homepage.html')

def loginpage(request):
    return render(request,'loginpage.html')



def studentreg(request):
    login_form=Customform()
    student_form=studentform()
    if request.method == 'POST':
        login_form=Customform(request.POST)
        student_form=studentform(request.POST,request.FILES)
        if login_form.is_valid() and student_form.is_valid():
            obj1=login_form.save(commit=False)
            obj1.is_student=True
            obj1.save()
            obj2=student_form.save(commit=False)
            obj2.one=obj1
            obj2.save()
            return redirect('loginpage')
    return render(request,'studenttemplate/stdregistration.html',{"show1":login_form,"show2":student_form})

def teacherreg(request):
    login_form = Customform()
    teacher_form = teacherform()
    if request.method == 'POST':
        login_form = Customform(request.POST)
        teacher_form = teacherform(request.POST)
        if login_form.is_valid() and teacher_form.is_valid():
            obj1 = login_form.save(commit=False)
            obj1.is_teacher = True
            obj1.save()
            obj2 = teacher_form.save(commit=False)
            obj2.two = obj1
            obj2.save()
            return redirect('loginpage')
    return render(request, 'teachertemplate/teacherreg.html', {"show1": login_form, "show2": teacher_form})

def Login_view(request):
    if request.method == 'POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminpage')
            elif user.is_student:
                return redirect('studentpage')
            elif user.is_teacher:
                return redirect('teacherpage')

        else:
            messages.info(request,'Invalid Credentials')
    return render(request,'loginpage.html')

def adminpage(request):
    return render(request,'admintemplate/adminpage.html')

def studentpage(request):

    return render(request,'studenttemplate/studentpage.html')

def teacherpage(request):

    return render(request,'teachertemplate/teacherpage.html')

# def tchrstudentview(request):
#     show=student.objects.all
#     return render(request,'teachertemplate/teacherpage.html')

def studentpersonal(request):
    u = request.user
    show = student.objects.get(one=u)
    return render(request,'studenttemplate/stdprofile.html',{"show":show})

def stdmarksadd(request):
    view = marksaddform()
    if request.method=='POST':
        view = marksaddform(request.POST)
        if view.is_valid():
            view.save()
            return redirect('teacherpage')
    return render(request,'teachertemplate/stdmarkadd.html',{"view":view})

def stdmarksview(request):
    show=marksadd.objects.all()
    return render(request,'teachertemplate/stdmarkview.html',{"show":show})