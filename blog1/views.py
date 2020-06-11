from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from blog1.forms import *
from blog1.models import *
from django.contrib.auth.models import User
# Create your views here.
def landing(request):
    objects = PublishUser.objects.order_by('-id')

    context ={'lists':objects}
    return render(request,'blog1/landing.html',context)


def userlogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('blog1:blogs'))
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('pass')
            user = authenticate(username= username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('blog1:blogs'))
                else:
                    return HttpResponse("Account not active")
            else:
                print("someone tried to login and failed ")
                print(f"Username :{username} and password :{password}")
                return HttpResponse("Invalid login credentials")

        else:
            return render(request,'blog1/login.html',context={})

# @login_required
def next1(request):
    return render(request,'blog1/after.html',context={})

@login_required
def userlogout(request):
    logout(request)
    return render(request,'blog1/landing.html')
#
def registration(request):
    registered = False
    if request.method == "POST":


        user_form = authenticateform(request.POST)

        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            email = user_form.cleaned_data.get('email')
            print(username,password)
            user_obj = User(username=username,password= password,email=email)
            print('hello1')

            user_obj.set_password(user_obj.password)
            print('hello2')
            user_obj.save()
            print('hello3')
            registered = True
            print('hello4')
            return HttpResponseRedirect(reverse('blog1:congo'))
        else:
            print(user_form.errors)
    else:

        context={"registered":registered}
        return render(request,'blog1/signup1.html',context)


## this works too
# def registration(request):
#     registered = False
#     if request.method == "POST":
#
#
#         user_form = authenticateform(request.POST)
#
#         if user_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#             registered = True
#         else:
#             print(user_form.errors)
#     else:
#         form =  authenticateform()
#         context={'registered':registered,'form':form}
#         return render(request,'blog1/signup1.html',context)
def congo(request):
    return render(request,'blog1/congrats.html',)


@login_required
def postmaker(request):
    x=[]
    objects = PublishUser.objects.all()
    type(objects)
    for obj in objects:
        if obj.author == request.user.username:
                print(obj)
                x.append(obj)
        else:
            continue
    context={'lists':x}
    print(x)

    return render(request,'blog1/blogs.html',context)


@login_required
def newposter(request):
    if request.method == "POST":
        form = BlogContent1Form(request.POST)
        print('hello1')
        if form.is_valid():
            print('hello2')

            # form.user=user
            # form.save()
            user1= request.user

            user = User.objects.get(id=user1.id)
            # user = request.user.userna
            title = form.cleaned_data['title']
            story = form.cleaned_data['story']


            print('hello3')

            form11 = BlogContent11(user=user,title=title,story=story)

            print('hello4')
            form11.save()
            print('hello5')
            return HttpResponseRedirect(reverse('blog1:blogs'))
        else:
            print(form.errors)
    return render(request,'blog1/newpost.html')




@login_required
def draftsuser(request,pk):

     model = User.objects.get(id=pk)
     print(model)
     context = {'objects':model}
     return render(request,'blog1/drafts.html',context)


def publish(request):
    print('hello')
    if request.method == "POST":

        print('hello')
        author = request.POST['user']
        title = request.POST['title']
        story = request.POST['story']
        model = PublishUser(author=author,title=title,story=story)
        model.save()
        return HttpResponseRedirect(reverse('blog1:blogs'))
