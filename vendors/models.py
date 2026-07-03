from django.db import models
from accounts.models import User,UserProfile
from accounts.utils import send_notification_email

# Create your models here.

class Vendor(models.Model):
    user = models.OneToOneField(User,related_name='user',on_delete=models.CASCADE,)
    user_profile = models.OneToOneField(UserProfile,related_name='user_profile',on_delete=models.CASCADE,)
    vendor_name = models.CharField(max_length=50,blank=False,null=False)
    vendor_liscence = models.ImageField(upload_to='vendors/liscence',blank=False,null=False)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name

    def save(self,*args,**kwargs):
        if self.pk is not None:
            org = Vendor.objects.get(pk=self.pk)
            if self.is_approved != org.is_approved:
                context = {
                    'user': self.user,
                    'is_approved': self.is_approved,
                }
                if self.is_approved == True:
                    email_subject = "Vendor Approval"
                    email_template = 'accounts/email/vendor_approval_email.html'
                    send_notification_email(email_subject,email_template,context)
                else:
                    email_subject = "Vendor Rejection"
                    email_template = 'accounts/email/vendor_approval_email.html'
                    send_notification_email(email_subject,email_template,context)
        return super(Vendor,self).save(*args,**kwargs)

            
        

