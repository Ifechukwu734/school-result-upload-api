from django.db.models.signals import post_delete, post_save, pre_delete, pre_save
from django.dispatch import receiver
from .models import GeneralInfo
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail


@receiver(post_save, sender=GeneralInfo)
def model_saved(sender, instance, created, **kwargs):
    User = get_user_model()
    users = User.objects.all()
    heading = instance.heading
    message = instance.message
    sender = settings.EMAIL_HOST_USER
    for user in users:
        send_mail(subject=heading, recipient_list=[user.email], message=message,from_email=sender, fail_silently=False )
