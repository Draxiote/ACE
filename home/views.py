from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from home.models import Contact, Credentials, Forum, Event, Alert
from django.contrib import messages
from django.views import generic

email1='ok'

# Login and SignUp Page
def login(request):
    global email1
    if request.method == "POST":
        email1 = request.POST.get('email')
        password = request.POST.get('password')
        if Credentials.objects.filter(email=email1, password=password).exists():
            intro = Credentials.objects.get(email=email1)
            greet = intro.name
            return render(request, 'index.html', {'greet': greet})
            #return render(request, 'index.html')
        else:
            return HttpResponse("404")
    return render(request, 'login.html')  
    
def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        signup = Credentials(name=name,
                           email=email,
                           password=password)
        signup.save()
        messages.success(request, "Your account has been created")
    return render(request, 'signup.html') 



# Home
def index(request): 
    intro = Credentials.objects.get(email=email1)
    greet = intro.name
    hd = Alert.objects.get(disp=True)
    return render(request, 'index.html', {'greet': greet, 'hd':hd})



# Forums   
def c_forum(request):
    if request.method == "POST":
        name = request.POST.get('name')
        topic = request.POST.get('topic')
        category = request.POST.get('category') 
        body = request.POST.get('body') 
        c_forum = Forum(name=name,
                        topic=topic,
                        category=category,
                        body=body)
        c_forum.save()
        messages.success(request, "Your Forum has been created")
    return render(request, 'c_forum.html')
 
def forum_index(request):
    forum_list = Forum.objects.all()
    return render(request, 'forum_index.html', {'forum_list':forum_list})

def post_detail(request, id):
    forum = Forum.objects.filter(id=id)
    return render(request, 'post_detail.html', {'forum':forum})

def del_post(request, id):
    global email1
    si = Forum.objects.get(id=id)
    f = si.mail
    if f == email1:
        post_dlist = Forum.objects.filter(id=id)
        post_dlist.delete()
        messages.error(request, "Deletion was a success. Please return to see changes.")
    
    else:    
        messages.error(request, "Error, can't delete this.")
        
        
    return HttpResponseRedirect(reverse('forum_index'))


#DOCs
def docs(request):
    return render(request, 'docs.html')


# Planner
def planner(request):
    plan1 = Event.objects.filter(month=1, email=email1).count
    print(type(plan1))

    plan2 = Event.objects.filter(month=2, email=email1).count
    print(type(plan2))

    plan3 = Event.objects.filter(month=3, email=email1).count
    print(type(plan3))

    plan4 = Event.objects.filter(month=4, email=email1).count
    print(type(plan4))

    plan5 = Event.objects.filter(month=5, email=email1).count
    print(type(plan5))

    plan6 = Event.objects.filter(month=6, email=email1).count
    print(type(plan6))
    
    plan7 = Event.objects.filter(month=7, email=email1).count
    print(type(plan7))

    plan8 = Event.objects.filter(month=8, email=email1).count
    print(type(plan8))

    plan9 = Event.objects.filter(month=9, email=email1).count
    print(type(plan9))

    plan10 = Event.objects.filter(month=10, email=email1).count
    print(type(plan10))

    plan11 = Event.objects.filter(month=11, email=email1).count
    print(type(plan11))

    plan12 = Event.objects.filter(month=12, email=email1).count
    print(type(plan12))
    return render(request, 'planner.html', {'plan1':plan1, 'plan2':plan2, 'plan3':plan3, 'plan4':plan4, 'plan5':plan5, 'plan6':plan6,
                                            'plan7':plan7, 'plan8':plan8, 'plan9':plan9, 'plan10':plan10, 'plan11':plan11, 'plan12':plan12,})

def cal(request, id):
    pl = Event.objects.filter(month=id, email=email1)
    return render(request, 'cal.html', {'pl':pl})

def c_plan(request):
    if request.method == "POST":
        head = request.POST.get('head')
        mon = request.POST.get('mon')
        day = request.POST.get('day')
        body = request.POST.get('body')
        cpi = Event(head=head,email=email1, month=mon, date=day, body=body, created_at=datetime.today())
        cpi.save()
        messages.success(request, "Your event has been created :)")
    return render(request, 'c_plan.html')

def del_plan(request, id):
    pdl = Event.objects.filter(id=id)
    pdl.delete()
    messages.success(request, "Deletion was a success. Please return to see changes.")
    return render(request, 'cal.html')


#About
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,
                          email=email,
                          phone=phone,
                          desc=desc,
                          date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")
    return render(request, 'contact.html')
    


def profile(request):
    cred = Credentials.objects.filter(email=email1)
    bo = False
    co = Credentials.objects.filter(email=email1, priv=1)
    if co.exists():
        bo = True
    return render(request, 'profile.html', {'cred': cred, 'bo':bo})

  
  
  
    
def adminpanel(request):
    alert = Alert.objects.all()
    return render(request, 'adminpanel.html', {'alert':alert})

def c_alert(request):
    if request.method == "POST":
        topic = request.POST.get('heading')
        body = request.POST.get('desc')
        svc = Alert(topic=topic,body=body)
        svc.save()
        return render(request, 'adminpanel.html')

    return render(request, 'c_alert.html')

def view_alerts(request):
    alert = Alert.objects.all()
    return render(request, 'view_alerts.html', {'alert':alert})

def del_alert(request, id):
    alert = Alert.objects.all()
    adl = Alert.objects.filter(id=id)
    adl.delete()
    messages.success(request, "Deletion was a success. Please return to see changes.")
    return render(request, 'adminpanel.html', {'adl': adl, 'alert':alert})

def setact(request, id):
    Alert.objects.filter(disp=True).update(disp=False)
    Alert.objects.filter(id=id).update(disp=True)
    bo = False
    co = Credentials.objects.filter(email=email1, priv=1)
    if co.exists():
        bo = True
    d = Credentials.objects.filter(email=email1)
    if d.exists():
        return render(request, 'profile.html', {'d': d, 'bo': bo})

def setinact(request, id):
    cu = Alert.objects.get(id=id)
    if cu.disp == True:
        Alert.objects.filter(disp=True).update(disp=False)
        Alert.objects.filter(id=21).update(disp=True)
    bo = False
    co = Credentials.objects.filter(email=email1, priv=1)
    if co.exists():
        bo = True
    d = Credentials.objects.filter(email=email1)
    if d.exists():
        return render(request, 'profile.html', {'d': d, 'bo': bo})




# TEST

def modaltest1(request):
    return render(request, 'modaltest1.html')