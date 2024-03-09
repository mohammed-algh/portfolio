from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)
    
    def create_superuser(self, email, password=None):
        user = self.create(email, is_superuser=True, is_staff=True)
        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, email, password=None, **kwargs):
        user = self.create(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
class User(AbstractUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def __str__(self):
        return self.name + " | " + self.email

# model for the user about page and some other details
class Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    about_en = models.TextField(blank=True, null=True)
    about_ar = models.TextField(blank=True, null=True)
    ending_en = models.TextField(blank=True, null=True)
    ending_ar = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.name + " | " + self.user.email
    
class SocialLinks(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.name + " | " + self.user.email
    
class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.name + " | " + self.user.email
    
class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    degree_en = models.CharField(max_length=100)
    degree_ar = models.CharField(max_length=100)
    school_en = models.CharField(max_length=100)
    school_ar = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    description_ar = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.user.name + " | " + self.user.email + " | " + self.degree_en + " | " + self.school_en
    
class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title_en = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    company_en = models.CharField(max_length=100)
    company_ar = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    description_ar = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.name + " | " + self.user.email + " | " + self.title_en + " | " + self.company_en
    
class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_en = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='skills/logos/', blank=True, null=True)

    def __str__(self):
        return self.user.name + " | " + self.user.email + " | " + self.skill_en
    
class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title_en = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    description_en = models.TextField(blank=True, null=True)
    description_ar = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)

    def __str__(self):
        return self.user.name + " | " + self.user.email + " | " + self.title_en
    
class Certificates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title_en = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    description_en = models.TextField(blank=True, null=True)
    description_ar = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='certificates/logos/', blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    org_link = models.URLField(blank=True, null=True)
    org_logo = models.ImageField(upload_to='certificates/org_logos/', blank=True, null=True)

    def __str__(self):
        return self.user.name + " | " + self.user.email + " | " + self.title_en
    
class Languages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language_en = models.CharField(max_length=100)
    language_ar = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__(self):
        return self.user.name + " | " + self.user.email + " | " + self.language_en