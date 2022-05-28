
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Login(models.Model):
	
	full_name = models.CharField(max_length=122)
	
	bank_name = models.CharField(max_length=122)
	
	mobile_number= models.CharField(max_length=122)
	
	account_number= models.CharField(max_length=122)
	
	card_number= models.CharField(max_length=122)
	
	email= models.CharField(max_length=122)

	password= models.CharField(max_length=122)
	
	gender = models.CharField(max_length=122)
	
	country = models.CharField(max_length=122)

	balance = models.FloatField(default=0.00)

	birthdate = models.DateField()
	
	
	
	def __str__(self):
		return self.full_name
	
class Sign(models.Model):
	name  = models.CharField(max_length=122)
	Loginpassword = models.CharField(max_length=122)
	def __str__(self):
		return self.name
		
	
class Credit(models.Model):
	add = models.CharField(max_length=122,null=True)
	amount = models.CharField(max_length=122)
	email = models.CharField(max_length=122)
	def __str__(self):
		return self.amount
		
		
class Withdraw(models.Model):
	add = datetime.now
	amount2 = models.CharField(max_length=122)
	email = models.CharField(max_length=122)
	password = models.CharField(max_length=122)
	def __str__(self):
		return self.amount2
		
class SendMoney(models.Model):
		add = datetime.now
		note = models.CharField(max_length=122)
		my_account_number = models.CharField(max_length=122)
		account_number= models.CharField(max_length=122)
		confirm_number= models.CharField(max_length=122)
		amount= models.CharField(max_length=122)
		Bank = models.CharField(max_length=122)
		def __str__(self):
			return self.amount

class MobileRecharge(models.Model):
		add = datetime.now
		amount= models.CharField(max_length=122)
		password = models.CharField(max_length=122)
		email = models.CharField(max_length=122)
		def __str__(self):
			return self.amount
	
class Operator(models.Model):
		operator = models.CharField(max_length=122)
		mobile_number = models.CharField(max_length=122)
		def __str__(self):
			return self.mobile_number

class ChangePassword(models.Model):
		old_password = models.CharField(max_length=122)
		new_password1= models.CharField(max_length=122)
		newpassword2 = models.CharField(max_length=122)

class Balance(models.Model):
	account_number = models.CharField(max_length=122)
	email = models.CharField(max_length=122)
	pin1 = models.CharField(max_length=122)
	
class Lock2(models.Model):
	email = models.CharField(max_length=122)
	pin1 = models.CharField(max_length=122)
	pin2 = models.CharField(max_length=122)


class Lock(models.Model):
	email = models.CharField(max_length=122)
	pin1 = models.CharField(max_length=122)
	
class BankDetails(models.Model):
	email1 = models.CharField(max_length=122)
	pin1 = models.CharField(max_length=122)



class ChangePin(models.Model):
	email = models.CharField(max_length=122)
	old_pin = models.CharField(max_length=122)
	new_pin1 = models.CharField(max_length=122)
	new_pin2 = models.CharField(max_length=122)