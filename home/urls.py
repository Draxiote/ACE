from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    #Login
    path("", views.login, name='login'),
    path("signup", views.signup, name='signup'),
    
    
    #Home
    path("home", views.index, name='home'),   
    
    
    #Forum
    path("forum_index", views.forum_index, name='forum_index'),
    path("c_forum", views.c_forum, name='c_forum'),
    path("post_detail/<int:id>", views.post_detail),
    
    path('post_detail/post_detail/d/<int:id>', views.del_post),
    
    
    #DOCs
    path("docs", views.docs, name='docs'),
    
    
    #Planner
    path("planner", views.planner, name='planner'),
    path("cal/<int:id>", views.cal, name='cal'),
    path("c_plan", views.c_plan, name='c_plan'),
    path("cal/d/<int:id>", views.del_plan),
    
    
    #About
    path("about", views.contact, name='about'),
    
    #Profile
    path("profile", views.profile, name='profile'),
   
   
   
    #Admin Panel
    path("adminpanel", views.adminpanel, name='adminpanel'),
    path("c_alert", views.c_alert, name='c_alert'),
    path("view_alerts", views.view_alerts, name='view_alerts'),
    path('<int:id>', views.del_alert),
    path('act/<int:id>', views.setact),
    path('inact/<int:id>', views.setinact),
    

    #TEST
    path("modaltest1", views.modaltest1, name='modaltest1')
]