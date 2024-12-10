from django.db import models
from accounts.models import User, UserProfile

# Create your models here.
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="userprofile")
    vendor_name = models.CharField(max_length=50)
    vendor_licence = models.ImageField(upload_to='vendor/licences')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name