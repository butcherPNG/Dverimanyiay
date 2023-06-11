from django.core.mail import send_mail

def send(user_email):
    send_mail(
        'Вы подписались на рассылку',
        'Спасибо, что подписались на рассылку новостей.',
        'dverimaniay@gmail.com',
        [user_email],
        fail_silently=False,
    )