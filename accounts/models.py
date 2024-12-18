from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email,phone_number=None, password=None):
        if not email:
            raise ValueError("User Must Have an Email Address")
        
        if not username:
            raise ValueError("User must have an Username")
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,
            phone_number = phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email,phone_number=None, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
            phone_number = phone_number
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    VENDOR = 1
    CUSTOMER = 2
    ROLE_CHOICE = (
        (VENDOR, 'VENDOR'),
        (CUSTOMER, 'CUSTOMER')
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12,null=True,blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    objects = UserManager()

    def __str__(self):
        return self.email
    

    def has_perm(self, perm, object=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    def get_role(self):
        if self.role == 1:
            user_role = VENDOR
        elif self.role == 2:
            user_role= CUSTOMER
        return user_role


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='user/profile_pictures', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='user/cover_photo', blank=True, null=True)
    address = models.CharField(max_length=250, blank=True,null=True)
    country = models.CharField(max_length=15, blank=True,null=True)
    state = models.CharField(max_length=15, blank=True,null=True)
    city = models.CharField(max_length=15, blank=True,null=True)
    pin_code = models.CharField(max_length=6, blank=True,null=True)
    latitude = models.CharField(max_length=20, blank=True,null=True)
    longitude = models.CharField(max_length=50, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.user.email
    



