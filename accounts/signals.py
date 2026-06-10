from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import UserProfile,User


@receiver(post_save,sender=User)
def create_user_profile_receiver(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('user profile created')
    else:
        try:
            user_profile = UserProfile.objects.get(user=instance)
            user_profile.save()
            print('user profile fetched and updated')
        except:
            UserProfile.objects.create(user=instance)
            print('user updated successfully')
