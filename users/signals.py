from django import dispatch
from django.db.models.signals import pre_save, post_delete, pre_delete, post_save
from accounts.models import *
from django.contrib.auth.models import User
from django . dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import Group

def create_customer(sender, instance, created, **kwargs):
    if created:
        user = instance
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        customer = Customer.objects.create(
            user=user,
            name=user.username,
            email=user.email,
        )

        subject = 'Welcome to Ad-din'
        message = 'You are new mamber of my famaily'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [customer.email],
            fail_silently=False,
        )


def update_profile(sender, instance, created, **kwargs):
    customer = instance
    user =customer.user
    if created == False:
       user.username = customer.name
       user.email = customer.email
       user.save()


def delete_user(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


post_save.connect(create_customer, sender=User)
post_save.connect(update_profile, sender=Customer)
post_delete.connect(delete_user, sender=Customer)