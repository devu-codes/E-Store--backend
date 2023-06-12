from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
# from django.core.mail import EmailMessage, BadHeaderError
# from templated_mail.mail import BaseEmailMessage
# from .tasks import notify_customers
import requests

# On class based View
class HelloView(APIView):
    @method_decorator(cache_page(5*60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        return render(request, 'hello.html', {'name': data})

@cache_page(5*60)
def say_hello(request):
    # try: 
        # send_mail('subject', 'message', 'ankitpan38@gmail.com', ['devanshpandey977@gmail.com', 'dp9919669138@gmail.com'])
        # mail_admins('subject', 'message', html_message='message')
        # message = EmailMessage('Subject', 'Message', 'fromdev@domain.com', ['Mymail@domain.com', 'hismail@domain.com'])
        # message.attach_file('playground/static/images/dog.jpg')
        # message.send()

    #     message = BaseEmailMessage(
    #         template_name='emails/hello.html',
    #         context={'name': 'Dev'}
    #     )
    #     message.send(['some_email@domain.com'])
    # except BadHeaderError:
    #     pass
    response = requests.get('https://httpbin.org/delay/2')
    data = response.json()
    return render(request, 'hello.html', {'name': data})
