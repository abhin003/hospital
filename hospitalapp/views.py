from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from hospitalapp.models import *
import random
import string 
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def gallery(request):
	return render(request,'gallery.html')

def service(request):
	return render(request,'services.html')

def single(request):
	return render(request,'single.html')

def docreg(request):
	if request.method == 'POST':
	    name=request.POST['name']
	    license=request.POST['licens']
	    department=request.POST['spec']
	    email=request.POST['email']
	    password=request.POST['pass']
	    time=request.POST['time']
	    check=doctor_tb.objects.filter(email=email)
	    if check:
	    	return render(request,'docregistration.html',{'error':'email already exsist plz try again'})
	    else:
        	query=doctor_tb(name=name,licens_no=license,department=department,email=email,password=password,time=time) 
        	query.save() 
        	return render(request,'docregistration.html')
	else:
		return render(request,'docregistration.html')

							 


def doclogin(request):
	if request.method == 'POST':
	    email=request.POST['email']
	    password=request.POST['pass']
	    check=doctor_tb.objects.all().filter(email=email,password=password)
	    if check:
	    	for x in check:
	    
	    		request.session['userid']=x.id
	    	return render(request,'index.html')
	    else:
	    	return render(request,'doclogin.html')	
	return render(request,'doclogin.html')	



def patientreg(request):
	if request.method == 'POST':
	    name=request.POST['name']
	    age=request.POST['age']
	    phone=request.POST['p_no']
	    email=request.POST['email_p']
	    password=request.POST['pass_p']
	    query1=patient_tb(name=name,age=age,phone_no=phone,email=email,password=password) 
	    query1.save() 
	return render(request,'patientreg.html')


def patientlogin(request):
	if request.method == 'POST':
	    email=request.POST['email_p']
	    password=request.POST['pass_p']
	    check=patient_tb.objects.all().filter(email=email,password=password)
	    if check:
	    	for x in check:
	    
	    		request.session['userid']=x.id
	    	return render(request,'index.html')
	    else:
	    	return render(request,'patientlogin.html',{"msg":"wrong"})	
	return render(request,'patientlogin.html')



def booking(request):
	if request.session.has_key('userid'):
		if request.method=='POST':
			des=request.POST['spec']
			time=request.POST['time']
			date=request.POST['date']
			docid=request.POST['doc']
			pid=request.session['userid']
			did=doctor_tb.objects.get(id=docid)
			paid=patient_tb.objects.get(id=pid)
			query=booking_tb(description=des,time=time,date=date,pid=paid,did=did)
			query.save()
			viewquery=doctor_tb.objects.all()
			return render(request,'booking.html',{'viewquery':viewquery})
		else:
			viewquery=doctor_tb.objects.all()
			return render(request,'booking.html',{'viewquery':viewquery})
	else:
	    return render(request,'patientlogin.html')

def logout(request):
	if request.session.has_key('userid'):
		del request.session['userid']
	return render(request,'index.html')

def info(request):
	query = doctor_tb.objects.all()
	return render(request,'booking.html',{'viewquery':query})

def book(request):
	print("jsjsjjsjsjsjjjsjsjjs")
	boxid =request.GET.get('boxid')
	data = doctor_tb.objects.all().filter(id=boxid)
	for x in data:
		desc=x.department
		time=x.time
		dat ={"bdesc":desc,"btime":time}
		print(dat)
		return JsonResponse(dat) 

def newpass(request):
	if request.method=='POST':
		email=request.POST['email']
		check=doctor_tb.objects.filter(email=email)
		if check:
			for x in check:
				userid=x.id
				print(userid,"+++++++")
				x = ''.join(random.choices(email + string.digits, k=8))
				y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
				subject = 'new password'
				url = f':http://127.0.0.1:8000/passconfirm/?uid={userid}'
				message = f':please click on the link {url}'

				email_from = settings.EMAIL_HOST_USER 
				recipient_list = [email, ] 
				send_mail( subject, message, email_from, recipient_list ) 
				return render(request,'frgpass.html',{'msg':'plz check ur mail inbox'})
		else:
			return render(request,'frgpass.html',{'error':'enter correct email'})

	else:
		return render(request,'frgpass.html')




	 

def confirm(request):
	if request.method=='POST':
	   userid=request.POST['uid']

	   password=request.POST['pass1']
	   confirmpassword=request.POST['pass2']
	   if userid:
	   	query=doctor_tb.objects.all().filter(id=userid).update(password=password)
	   	return render(request,'doclogin.html',{'sucess':'sucessfully changed password'})
	   else:
	   	return render(request,'confirmpass.html',{'mssg':'enter same passsword'})
	else:
		 userid=request.GET['uid']
		 print('userid')
		 return render(request,'confirmpass.html',{'uid':userid})



def patmail(request):
	if request.method=='POST':
		email=request.POST['email']
		check=patient_tb.objects.filter(email=email)
		if check:
			for x in check:
				userid=x.id
				print(userid,"+++++++")
				x = ''.join(random.choices(email + string.digits, k=8))
				y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
				subject = 'new password'
				url = f':http://127.0.0.1:8000/patpass/?uid={userid}'
				message = f':please click on the link {url}'

				email_from = settings.EMAIL_HOST_USER 
				recipient_list = [email, ] 
				send_mail( subject, message, email_from, recipient_list ) 
				return render(request,'patmail.html',{'msg':'plz check ur mail inbox'})
		else:
			return render(request,'patmail.html',{'error':'enter correct email'})

	else:
		return render(request,'patmail.html')
	

def passpat(request):
	if request.method=='POST':
	   userid=request.POST['uid']

	   password=request.POST['pass1']
	   confirmpassword=request.POST['pass2']
	   if userid:
	   	query=patient_tb.objects.all().filter(id=userid).update(password=password)
	   	return render(request,'patientlogin.html',{'sucess':'sucessfully changed password'})
	   else:
	   	return render(request,'conpasspat.html',{'mssg':'enter same passsword'})
	else:
		 userid=request.GET['uid']
		 print('userid')
		 return render(request,'conpasspat.html',{'uid':userid})
	return render(request,'conpasspat.html')


def tabledata(request):

	viewquery = doctor_tb.objects.all()
	return render(request,'tableinduz.html',{'viewqueryinduz':viewquery})