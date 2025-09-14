from django.shortcuts import render,redirect
from .models import *

# # Create your views here.
# def layout(request):
#     user = User.objects.get(email=request.session['email'])
#     return render(request,'layout.html',{'user':user})
    
def index(request):
    blog = CreateBlog.objects.all()
    if request.session.get('email') :
        user = User.objects.get(email=request.session['email'])
        return render(request,'index.html',{'blog':blog,'user':user})
    else:
        return render(request,'index.html',{'blog':blog})

def about(request):
    if request.session.get('email') :
        user = User.objects.get(email=request.session['email'])
        return render(request,'about.html',{'user':user})
    else:
        return render(request,'about.html')


def signup(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            if user:
                msg = "user Already Exists"
                return render(request,'signup.html',{'msg':msg})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                User.objects.create(
                    name = request.POST['name'],
                    email = request.POST['email'],
                    password = request.POST['password'],
                )
                return redirect('login')
            else:
                msg = "Password does not match"
                return render(request,'signup.html',{'msg':msg})
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email = request.POST['email'])
            if user.password == request.POST['password']:
                request.session['email'] = request.POST['email']
                return redirect('index')
            else:
                msg = "password does not match"
                return render(request,'login.html',{'msg':msg})
        except:
            msg = "user Not Found"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')

def logout(request):
    del request.session['email']
    try:
        del request.session['profile']
    except:
        print("prpfile not found")
    return redirect('login')

def contect(request):
    if request.session.get('email'):
        user = User.objects.get(email=request.session['email'])
        return render(request,'contect.html',{'user':user})
    else:
        return render(request,'contect.html')

def profile(request):
    user = User.objects.get(email = request.session['email'])
    blog = CreateBlog.objects.filter(user=user)
    return render(request,'profile.html',{'user':user,'blog':blog})

def addblog(request):
    if request.method == "POST":
        user = User.objects.get(email = request.session['email'])  
        CreateBlog.objects.create(
            user = user,
            name = request.POST['name'],
            desc = request.POST['desc'],
            image = request.FILES['image']
        )
        return redirect('profile')
    else:
        return render(request,'addblog.html')

def editprofile(request):
    user = User.objects.get(email = request.session['email'])
    if request.method == "POST":
        user.name = request.POST['name']
        user.bio = request.POST['bio']
        try:
            user.profile = request.FILES['profile']
        except:
            print("image not gound")
        user.save()
        request.session['profile'] = user.profile.url
        return redirect('profile')
    else:
        return render(request,'editprofile.html',{'user':user})
    
def editblog(request,pk):
    user = User.objects.get(email = request.session['email'])
    blog = CreateBlog.objects.get(pk=pk)
    if request.method == "POST":
        blog.name = request.POST['name']
        blog.desc = request.POST['desc']
        try:
            blog.image = request.FILES['image']
        except:
            print("image not gound")
        blog.save()
        return redirect('profile')
    else:
        return render(request,'editblog.html',{'blog':blog})
    
def deleteblog(request,pk):
    user = User.objects.get(email = request.session['email'])
    blog = CreateBlog.objects.get(pk=pk)
    blog.delete()
    return redirect('profile')
    
def blogdetails(request,pk):
    try:
        user = User.objects.get(email = request.session['email'])
        blog = CreateBlog.objects.get(pk=pk)
        return render(request,'blogdetails.html',{'blog':blog,'user':user})
    except:
        return redirect('login')
    
def addwish(request,pk):
    try:
        user = User.objects.get(email=request.session['email'])
        blog = CreateBlog.objects.get(pk=pk)
        Wishlist.objects.create(
            user = user,
            blog = blog
        )
        return redirect('wishlist')
    except Exception as e:
        print("===================================",e)
        return redirect('login')
    

def deletewishlist(request,pk):
    wish = Wishlist.objects.get(pk=pk)
    wish.delete()
    return redirect('wishlist')
    
def wishlist(request):
    user = User.objects.get(email=request.session['email'])
    wish = Wishlist.objects.filter(user=user)
    return render(request,'wishlist.html',{'wish':wish})

def addlike(request,pk):
    user = User.objects.get(email=request.session['email'])
    blog = CreateBlog.objects.get(pk=pk)
    
    Likeuser.objects.create(
        user=user,
        blog=blog
    )
    blog.like+=1
    blog.save()
    a = blog.like
    print("==========================", a)
    return redirect('index')


def adddislike(request,pk):
    user = User.objects.get(email=request.session['email'])
    blog = CreateBlog.objects.get(pk=pk)
    
    DisLikeuser.objects.create(
        user=user,
        blog=blog
    )
    blog.dislike+=1
    blog.save()
    a = blog.dislike
    print("==========================",a)
    return redirect('index')