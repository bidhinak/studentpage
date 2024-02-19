from django.urls import path

from stdapp import views

urlpatterns=[
       path("",views.homepage,name="homepage"),
       path("loginpage",views.loginpage,name="loginpage"),
       path("adminpage",views.adminpage,name="adminpage"),
       path("studentpage",views.studentpage,name="studentpage"),
       path("Login_view",views.Login_view,name="Login_view"),
       path("studentreg",views.studentreg,name="studentreg"),
       path("teacherpage",views.teacherpage,name="teacherpage"),
       path("teacherreg",views.teacherreg,name="teacherreg"),
       path("studentpersonal",views.studentpersonal,name="studentpersonal"),
       path("stdmarksadd",views.stdmarksadd,name="stdmarksadd"),
       path("stdmarksview",views.stdmarksview,name="stdmarksview")
]