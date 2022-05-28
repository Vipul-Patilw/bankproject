#pylint:disable=E0602
#pylint:disable=E0001

from quopri import decodestring
from django.shortcuts import redirect, render
from bankingSolution.models import Balance, ChangePin, Login ,BankDetails, Withdraw, Credit, SendMoney, MobileRecharge, Operator, ChangePassword, Lock, Lock2
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
import re
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from bankproject import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from . tokens import generate_token
from django.core.mail import EmailMessage
from datetime import  datetime

# Create your views here.

a = 0.00

class changePassword(PasswordChangeView):
	form_class = PasswordChangeForm
	success_url = reverse_lazy('password_success')




def password_success(request):
	messages.info(request,"Password Changed Successfully")
	return render (request, 'setting.html')
#	global b
	#if request.method =="POST":
	#	password = request.POST.get('password')
	#	pass3 = request.POST.get('pass3')
		#pass4 = request.POST.get('pass4')
		#changepass =  ChangePasdword (password=password, pass3=pass3, pass4=pass4)
	#	changepass.save()
	#	if b == str(password):
	#		if len(password)>=6 and re.#search(r"[A-Z][a-z]+[@_!#$%^&*()?/}{~:]+[0-9]",password):
	#			message.success(request,"password change successfully")
			#	return redirect ("/home")
		#	else:
			#		messages.error(request,"password should be at least 8 character long. contain both uppercase and lowercase character, at least one alpha numeric and one special charecter  (eg:Test@123)")
			#		return redirect ('/changepass')
	#	else:
	#		message.error(request,"old password doesn't matched")
			

def index(request):
		if request.method =="POST":
		
			full_name = request.POST.get('full_name')
			bank_name = request.POST.get('bank_name')
			mobile_number= request.POST.get('mobile_number')
			account_number= request.POST.get('account_number')
			card_number= request.POST.get('card_number')
			email = request.POST.get('email')
			password= request.POST.get('password')
			gender = request.POST.get('gender')
			country = request.POST.get('country')
			birthdate = request.POST.get('birthdate')
			password2 = request.POST.get('password2')
			
			#try:
				
			Account = ["1234 5678 986 7800","345 1234 5678 986","256 5778 786 7600","486 6678 986 6800","446 2678 286 3800","556 7678 786 7800","156 5658 966 7300","856 5478 926 7800","416 5078 986 3830","356 6678 686 9850","226 4648 586 6800","656 7678 986 6800","456 5478 946 7840","156 2678 386 800"]
			
			if User.objects.filter(email=email):
						messages.error(request,"this email address already registered with us try different email address or click on forgot password while login if you don't remember your password")
						return redirect("/sign")
						
			if User.objects.filter(username=account_number):
						messages.error(request,"this account is already registered with another name")
						return redirect("/sign")

			if password != password2:
				messages.error(request,"confirm password doesn't matched with the password")
				return redirect ('/sign')
				
			if len(full_name)<12:
				messages.error(request,"Enter your full name (eg:Vipul Ramesh Patil)")
				return redirect ('/sign')
				
			if len(password)>=6 and re.search(r"[A-Z][a-z]+[@_!#$%^&*()?/}{~:]+[0-9]",password):
				pass
				
			else:
				messages.error(request,"password should be at least 6 character long. contain both uppercase and lowercase character, at least one alpha numeric and one special charecter  (eg:Test@123)")
				return redirect("/sign")
				
			for i in Account:
				if i == str(account_number):
					messages.success(request, full_name.title())
					myuser = User.objects.create_user(account_number,email,password)
					myuser.first_name = full_name
					myuser.last_name = bank_name
					myuser.save()
					myuser.is_active = False	
					
					users = Login(full_name=full_name,account_number=account_number, mobile_number=mobile_number,bank_name=bank_name,email=email,birthdate=birthdate,card_number=card_number,gender=gender,country=country)
					users.save()		
	
					#confirmation email
					current_site = get_current_site(request)
					email_sub2 = 'Activate your BANK-PAY Account'
					message2 = render_to_string('email_confirmation.html',{
						'name': myuser.first_name, 
						'domain': current_site.domain,
						'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
						'token': generate_token.make_token(myuser)
						})
					email = EmailMessage(
						email_sub2,
						message2,
						settings.EMAIL_HOST_USER,
						[myuser.email],
						)
					
					email.fail_silently= True
					email.send()
				#	context={ "bank": bank_name,
				#	"mobile": mobile_number,
				#	"card":card_number}
					
					return render(request, 'gotologin.html')
					
					
			else: 		
					messages.error(request," Account number is not valid")	
					return redirect("/sign")
		#	except:
			#	messages.error(request,"some problem come in our application please reopen the application")
			#	return redirect ('/sign')
				
		#return render(request, 'logininfo.html')	
		return render(request, 'logininfo.html')
	
	#  return HttpResponse("vipul patil")

def gotologin(request):
	return render (request,'gotologin.html')	
def sign(request):

	if request.method =="POST":
		Loginpassword= request.POST.get('Loginpassword')
		account_number1 = request.POST.get('account_number1')
		user = authenticate(username=account_number1, password=Loginpassword)
		if user is not None:
			
			login(request, user)
			return render (request,'lock.html')
			#full_name = user.first_name
		
		

		else:
	#	if str(Loginpassword) == str(b):
		#	messages.error(request,"password matched")
		#	return redirect('/login')    			
	  
			messages.error(request, "Please enter correct account number and  password ")
			return redirect('/login')    
		#	return render(request,'index.html')   
	return render(request,'index.html')

	
def home(request):
		global a
		

		if request.method =="POST":
			amount = request.POST.get('amount')
			add = request.POST.get('add')
			email = request.POST.get('email')
			credit = Credit(amount=amount,email=email)
			credit.save()
			balance = User.objects.get(email=email)
			bal = Login.objects.get(email=email)
			bal.balance += float(amount)
			bal.save()
			messages.success(request, amount)
			current_site = get_current_site(request)
			emailsub = "Bank-Pay Transaction"
			emailbody = render_to_string('creditsmail.html',{'amount': amount,
  'domain': current_site.domain,
  'name': balance.first_name,
  'balance': bal.balance })
			from_mail = settings.EMAIL_HOST_USER
			to_mail = [credit.email]
			email = EmailMessage(emailsub,emailbody,from_mail,to_mail)
			email.fail_silently=True
			email.send()
			date = datetime.now()
			return render(request,'/home',{'date':date})
			
		
		#	if b == user:
				#	return render (request,'sendMoney.html')
			
			
	
		return render (request,"home.html")	


	
def withdraw(request):
	global a	
	if request.method =="POST":
		email = request.POST.get('email')
		amount2 = request.POST.get('amount2')
		withdraw = Withdraw(amount2=amount2, email=email)
		withdraw.save()
		balance = User.objects.get(email=email)
		bal = Login.objects.get(email=email)
		if bal.balance < float(amount2):
				messages.error(request, amount2 + " Can't be Withdraw from your account,  you don't have sufficient balance")
				return redirect ("withdraw.html")
		else:
			bal.balance -= float(amount2)
			messages.success(request, amount2 + ", withdraw from your account successfully" )
			current_site = get_current_site(request)
			emailsub = "Bank-Pay Transaction"
			emailbody = render_to_string('withdrawmail.html',{'amount': amount2,
  'domain': current_site.domain,
  'name': balance.first_name,
  'balance': bal.balance })
			from_mail = settings.EMAIL_HOST_USER
			to_mail = [withdraw.email]
			email = EmailMessage(emailsub,emailbody,from_mail,to_mail)
			email.fail_silently=True
			email.send()
			return render (request,"withdraw.html")	
	return render (request,"withdraw.html")


def balance(request):
	if request.method =="POST":
		account_number = request.POST.get('account_number')
		email = request.POST.get('email')
		pin1 = request.POST.get('pin1')
		acc = Balance(account_number=account_number,email=email,pin1=pin1)
		passw = Lock2.objects.get(email=email)
		if pin1 != passw.pin1:
			messages.error(request,"Incorrect Pin, try again")
			return redirect('/balance')
		else:
			acc.save()
			bal = Login.objects.get(account_number=account_number)
			messages.info(request, bal.balance)
			credits = Credit.objects.filter(email=passw.email).all()
			withdraws = Withdraw.objects.filter(email=passw.email).all()
			moneysends = SendMoney.objects.filter(email=passw.email).all()
			recharges = MobileRecharge.objects.filter(email=passw.email).all()
			return render (request,'balance2.html', { 'credits': credits,'withdraws': withdraws,'moneysends': moneysends,'recharges': recharges})
	return render (request,'balance.html')
	
def setting(request):
	return render (request,'setting.html')
		
def sendMoney(request):
	global a
	if request.method =="POST":

	
		my_account_number = request.POST.get('my_account_number')
		Bank = request.POST.get('Bank')
		note = request.POST.get('note')
		account_number = request.POST.get('account_number')
		confirm_number = request.POST.get('confirm_number')
		amount = request.POST.get('amount')
		send = SendMoney(my_account_number=my_account_number,account_number=account_number,amount=amount,note=note)
		send.save()
		user = User.objects.get(username=my_account_number)
		bal = Login.objects.get(account_number=my_account_number)
		
	#	if Bank != bal2.bank_name:
		#	messages.error(request,'bank details are wrong please check and re-enter')
		#	return redirect ('/send')
			
#		if account_number != bal2.account_number:
	#		messages.error(request,'bank details are wrong please check and re-enter')
	#		return redirect ('/send')

		if account_number == my_account_number:
				messages.error(request,"Enter the account number of the person whom you want to send money. don't enter your account number!!")
				return redirect ('/send')
			
		if confirm_number != account_number:
				messages.error(request,"account number didn't matched!! Type same account number in confirm account also.")
				return redirect ('/send')
				
		if bal.balance < float(amount):
							messages.error(request,"Transaction failed!  you don't have sufficient balance")
							return redirect ('/send')
			
		else:
							bal2 = Login.objects.get(account_number=account_number)
							bal.balance -= float(amount)
							bal.save()
							bal2.balance += float(amount)
							bal2.save()
							messages.info(request, amount,account_number)
							current_site = get_current_site(request)
							emailsub = "Bank-Pay Transaction"
							emailbody = render_to_string('mailmoneysendtourself.html',{'amount': amount,
					'domain': current_site.domain,
					'name': user.first_name,
					'balance': bal.balance,
					'name2':bal2.full_name
					})
							from_mail = settings.EMAIL_HOST_USER
							to_mail = [bal.email]
							email = EmailMessage(emailsub,emailbody,from_mail,to_mail)
							email.fail_silently=True
							email.send()
							emailsub = "Bank-Pay Transaction"
							emailbody = render_to_string('mailmoneysendtoOther.html',{'amount': amount,
					'domain': current_site.domain,
					'name': bal2.full_name,
					'balance': bal2.balance, 
					'name2':user.first_name,
					'note':note})
							from_mail = settings.EMAIL_HOST_USER
							to_mail = [bal2.email]
							email = EmailMessage(emailsub,emailbody,from_mail,to_mail)
							email.fail_silently=True
							email.send()
							return render (request,'sendDetails.html',{'name':bal2.full_name,
							          'bank':bal2.bank_name,
							          'account':bal2.account_number,
							          'note':note})
					
	return render (request,'sendMoney.html')


def operator(request):

	if request.method =="POST":
		operator = request.POST.get('operator')
		mobile_number = request.POST.get('mobile_number')
		operators =  Operator(operator=operator, mobile_number=mobile_number)
		operators.save()
		return redirect ('/recharge')
	return render (request,'operator.html')

def recharge (request):
	global a
	if request.method =="POST":
			amount = request.POST.get('amount')
			email = request.POST.get('email')

			recharge =  MobileRecharge(amount=amount,email=email)
			log = Login.objects.get(email=email)
			recharge.save()
			if float(amount) > log.balance: 
				messages.error(request, amount+ " recharge failed ")
				return redirect ("/recharge.html")
			elif float(amount) == 1099.0:
				log.balance -= float(amount)
				messages.success(request, amount + " recharge succesfull")
				log.balance += 50.0
				messages.success(request, "Congrats! you get Rs 50 cashback on recharge of 1099")
				log.save()
				return render (request,'recharge.html')
			else:
				log.balance -= float(amount)
				log.save()
				messages.success(request, amount + " recharge succesfull")
				return render (request,'recharge.html')
				
	return render (request,'recharge.html')
	
def personalDetails (request):
	return render (request,'personalDetails.html')
	
def bankDetails (request):
	if request.method =="POST":
		email1 = request.POST.get('email1')
		pin1 = request.POST.get('pin1')
		acc = BankDetails(email1=email1,pin1=pin1)
		passw = Lock2.objects.get(email=email1)
		if pin1 != passw.pin1:
			messages.error(request,"Incorrect Pin, try again")
			return redirect('/bank')
		else:
			acc.save()
			bal = Login.objects.get(email=email1)
			return render (request,'BankDetails.html',{'card':bal.card_number,
														'gender':bal.gender,
														'mobile':bal.mobile_number,
														'birth':bal.birthdate})
	return render (request,'BankDetails2.html')
	
def bankDetails2(request):
	if request.method =="POST":
			email1 = request.POST.get('email1')
			bal = Login.objects.get(email=email1)
			return render (request,'BankDetailsEdit.html',{'card':bal.card_number,
														'gender':bal.gender,
														'mobile':bal.mobile_number,
														'birth':bal.birthdate})
	return render (request,'BankDetailsNotice.html')


def bankDetailsEdit(request):
	if request.method =="POST":
			full_name = request.POST.get('full_name')
			email = request.POST.get('email')
			mobile_number= request.POST.get('mobile_number')
			gender = request.POST.get('gender')
			birthdate = request.POST.get('birthdate')
			
			users = Login.objects.get(email=email)
			users.full_name = full_name
			users.mobile_number = mobile_number
			users.save()
			
			return render (request,'BankDetails.html')
	return render (request,'BankDetailsEdit.html')	
	


def about (request):
	return render (request,'about.html')

def privacy (request):
	return render (request,'privacy.html')



def admin(request):
	return render(request,"admin.html")

def logoutuser(request):
	logout(request)
	return redirect ("/login")

def activate(request, uidb64, token):
	try:
		uid = decodestring(urlsafe_base64_decode(uidb64))
		myuser = User.objects.get(pk=uid)
		return redirect ('/sign')
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		myuser = None

	if myuser is not None and generate_token.check_token(myuser, token):
		myuser.is_active = True
		myuser.save()
		login(request,myuser)
		return redirect('/login')
		
	else:
		return render(request, 'activation_failed.html')

def lock2(request):
		#	try:
				if request.method =="POST":
					pin1 = request.POST.get('pin1')
					pin2 = request.POST.get('pin2')
					email = request.POST.get('email')
					generate = Lock2(pin1=pin1,pin2=pin2,email=email)
					
					if len(pin1)!= 4:
						messages.error(request,"pin should be of only 4 numbers")
						return redirect ('/lock2')
					if pin2 != pin1:
						messages.error(request,"pin doesn't matched with other pin")
						return redirect ('/lock2')
					else:
						generate.save()
						return redirect('/home')

				return render(request,'lock.html')
	#		except:
			#	messages.error(request,"You have already generated the pin please enter pin here!!")
				return redirect('/lock')

def lock(request):
		if request.user.is_anonymous:
			return redirect ("/login")
		try:
			if request.method =="POST":
				email = request.POST.get('email')
				pin1 = request.POST.get('pin1')
				authen = Lock(email=email,pin1=pin1)
				generated = Lock2.objects.get(email=email)
				
				if generated.pin1 != pin1:
					messages.error(request,"wrong pin, try again")
					return redirect('/lock')
				else:
					authen.save()
					return redirect ('/home')
					
			return render(request,'lock2.html')
		except :
					messages.error(request,"You didn't create the pin, Please first Create the pin and try again")
					return redirect('/lock2')
			

	
def changePin(request):
	if request.method =="POST":
			old_pin = request.POST.get('old_pin')
			new_pin1 = request.POST.get('new_pin1')
			new_pin2 = request.POST.get('new_pin2')
			email = request.POST.get('email')
			change = ChangePin(new_pin1=new_pin1,new_pin2=new_pin2,old_pin=old_pin,email=email)
			
			lock = Lock2.objects.get(email=email)
			if old_pin != lock.pin1:
				messages.error(request,"incorrect old pin")
				return redirect('/changePin.html')
			
			if new_pin1 != new_pin2:
					messages.error(request,"confirm pin doesn't matched")
					return redirect('/changePin.html')
			if len(new_pin1) != 4:
					messages.error(request,"pin should be of 4 numbers only")
					return redirect('/changePin.html')
			else:
				change.save()
				lock.pin1 = new_pin1
				lock.save()
				messages.success(request,"Pin has been changed sucessfully!!")
				return redirect('/setting.html')
	return render (request,'changePin.html')
	
