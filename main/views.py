from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewsLetterForm
from .emails import send_welcome_email
from .models import Subscriber

# Create your views here.
def newsletter(request):

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = Subscriber(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('newsletter')

    else:
        form = NewsLetterForm()

    return render(request, 'index.html', {"form": form})
