from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import messages
from accounts.models import Token
from django.core.urlresolvers import reverse

def send_login_email(request):
  email = request.POST['email']
  token = Token.objects.create(email = email)
  url = request.build_absolute_uri(
    reverse('login') + '?token=' + str(token.uid)
  )
  send_mail('Your login link for Superlists', f'Use this link to login:\n\n{url}', 'kgin52@gmail.com', [email])
  messages.success(
    request,
    "Check your email, we've sent you a link you can use to log in."
  )
  return redirect('/')

def login(request):
  return redirect('/')