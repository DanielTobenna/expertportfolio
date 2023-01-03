from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.core.mail import BadHeaderError, send_mail

# Create your views here.

def home(request):
	return redirect('https://en.wikipedia.org/wiki/Expert')

def putri_perbesi(request):
	return render(request, 'expertinfoapp/index.html')

#send_mail(username, "A client with username: {} has just signed up on your site with email: {}".format(username, email),email, ['support@quantumfinancecompany.com'])

def sendMessage(request):
	if request.method == 'POST':
		name= request.POST.get('name')
		subject= request.POST.get('subject') 
		email= request.POST.get('email') 
		message= request.POST.get('message')
		try:
			send_mail(name, "A client with name: {}, and email: {} has just sent you a message through Putri Perbesi page.".format(name,email), email,['bryananadae61@gmail.com'])
			return HttpResponse('Your message was sent successfully. I will get back to you shortly.')
		except BadHeaderError: 
			return("Your message couldn't be sent. Please try again later.")
	return HttpResponse('Thanks for sending us a message')
