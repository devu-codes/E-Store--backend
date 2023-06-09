from django.shortcuts import render
# from django.core.mail import EmailMessage, BadHeaderError
# from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers


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
    notify_customers.delay('HELLO!')


    return render(request, 'hello.html', {'name': 'Mosh'})
