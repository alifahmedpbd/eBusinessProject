from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('Senior Developer', 'Senior Developer'),
        ('Creative Director', 'Creative Director'),
        ('Project Manager', 'Project Manager'),
        ('Business Analyst', 'Business Analyst'),
        # Add more roles if needed
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='team_profiles/')
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"


from django.db import models

class Portfolio(models.Model):

    CATEGORY_CHOICES = (
        ('app', 'App'),
        ('product', 'Product'),
        ('branding', 'Branding'),
        ('books', 'Books'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('visitor', 'Visitor'),
        ('staff', 'Staff'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='visitor'
    )

def save(self, *args, **kwargs):
    if self.is_superuser:
        self.is_staff = True
    elif self.role == 'staff':
        self.is_staff = True
    else:
        self.is_staff = False

    super().save(*args, **kwargs)

    def __str__(self):
        return self.username