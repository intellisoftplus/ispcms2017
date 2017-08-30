from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.core.mail import send_mail
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import ContactUsForm

from django.core.mail import send_mail


def index(request):
    return HttpResponse("Hello, world. You're at the sales index.")

def subscribe(request):
    if request.method == 'POST':

        send_to = 'support@intellisoftplus.com'

        subject = 'New Get Our Latest News SignUp'

        email = request.POST['email']

        message = email + " " + 'Signed up for all our latest news'

        sendmail(send_to,subject,message)

        messages.success(request, 'Subscription detail updated.')
        #messages.debug(request, ' SQL statements were executed.')
        #messages.info(request, 'Three credits remain in your account.')
        #messages.success(request, 'Profile details updated.')
        #messages.warning(request, 'Your account expires in three days.')
        #messages.error(request, 'Document deleted.')

        return HttpResponseRedirect('/')


def contactus(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactUsForm(request.POST)
        # check whether it's valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required

        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_to = 'support@intellisoftplus.com'

        subject = 'New Contact US Form SignUp'


        mail = "Name :" + " " + name + " " + "Email :" + " " + email + " " + "Message" + " " + message

        sendmail(send_to, subject, mail)

        messages.success(request, 'Thank you for contacting us. '
                                  'Your message has been received, o'
                                  'ne of our representatives will be '
                                  'in touch with you shortly')

         #  redirect to a new URL:

        return HttpResponseRedirect('/contacts/')

    # if a GET (or any other method) we'll create a blank form
    else:

        return HttpResponseRedirect('/contacts/')
        form = ContactUsForm()

    return HttpResponseRedirect('/contacts/')
    #return render(request, '/contacts/', {'form': form})



def sendmail( to, subject, message ):

    send_mail(subject, message, 'support@intellisoftplus.com',
              [to], fail_silently=True)

    return



