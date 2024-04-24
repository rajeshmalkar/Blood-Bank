from django.shortcuts import render,HttpResponse,render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from bank.models import Userprofile, Appointments
# Create your views here.
def about(request):
    return HttpResponse("Hello from blood bank")

def home(request):
    if request.method == 'GET':
        userid=request.user.id
        print(userid)
        return render(request, 'home.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        reason = request.POST.get('reason')
        age = request.POST.get('age')
        message = request.POST.get('message')

        
       
        
        m = Appointments.objects.create(
            user = request.user,
            name=name,
            email=email,
            phone=phone,
            date=date,
            reason=reason,
            age=age,
            message=message
        )
        
        
        m.save()
        
        # Redirect to a success page
        return redirect('/')
       


def About(request):
    return render (request,'about.html')

def Contact(request):
    return render (request, 'contact.html')

def register(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'register.html' )

    else:
        request.method == 'POST'
        n   =  request.POST['name']
        un  =  request.POST['uname']
        con =  request.POST['contact']
        p   =  request.POST['pass']
        cp  =  request.POST['cpass']
        dob   =  request.POST['dob']
        group  =  request.POST['group']
        add =  request.POST['add']

        '''
        print(n)
        print(un)
        print(con)
        print(p)
        print(cp)
        print(dob)
        print(group)
        print(add)
        '''
        if n==''or un=='' or con==''  or p=='' or cp=='' or dob=='' or group=='' or add=='':
            context['errmsg']='fields can not be blank'
            return render (request,'register.html',context)

        elif p!=cp:
            context['errmsg']='password and confirm password not match'
            return render(request,'register.html',context)

        elif len(p)<8:
            context['errmsg']='password must be 8 characters'
            return render(request,'register.html',context)

        else:
            try:
                u = User.objects.create(username=un)
                u.set_password(p)
                u.save()
                

                if u is not None:
                    pro = Userprofile.objects.create(user=u, name=n, contact=con, address=add, dob=dob, blood_group=group)
                    pro.save()
                    #print(pro)
                    context['success'] = 'Successfully registered'
                    return render(request, 'register.html', context)

                else:
                    context['errmsg'] = "Unfortunetely User Profile Not be created"
                    return render(request, 'register.html', context)
            
            except Exception:
                context['errmsg'] = "User Already exists"
                return render(request, 'register.html', context)

    

def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    else:
        un = request.POST.get('uname')
        p = request.POST.get('pass')

            

        u = authenticate(username=un, password=p)
        print(u)

        if u is not None:
            login(request, u)
            return redirect('/')
        else:
            context = {}
            context['errmsg'] = 'Invalid username or password'
            return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('/')


'''def profile(request):
    pro = Userprofile.objects.all()
    context={}
    context['data']=pro
    return render(request, "profile.html",context)

    m=Appointments.objects.all()
    print(m)
    context={} 
    context['data1']=m
    return render(request,'profile.html',context)'''

def profile(request):
    pro = Userprofile.objects.filter(user = request.user)
    appointment = Appointments.objects.filter(user = request.user)


    
    context = {
        'data': pro,
        'data1': appointment
    }
    
    return render(request, "profile.html", context)

def cancel(request,rid):
    appointments=Appointments.objects.filter(id=rid)
    appointments.delete()
    return redirect('/profile')





