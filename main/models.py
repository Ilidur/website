from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractUser,BaseUserManager)
from django.utils.translation import gettext_lazy as _


class SpaceUserManager(BaseUserManager):
    def create_user(self, email, password=None, space=None):
        """
        Creates and saves a User with the given email, space
        and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            space=space,
        )

        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email
        and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    space = models.ForeignKey('Space', models.SET_NULL, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = SpaceUserManager();

    class Meta:
        ordering = ["first_name"]

class Space(models.Model):

    STATUS_CHOICES = (
        ("Active", "Active"),
        ("Starting", "Starting"),
        ("Suspended", "Suspended"),
        ("Defunct", "DEFUNCT"),
    )

    COUNTRY_CHOICES = (
        ("England", "England"),
        ("Guernsey","Guernsey"),
        ("Ireland", "Ireland"),
        ("Scotland", "Scotland"),
        ("Wales", "Wales"),
    )

    name = models.CharField(max_length=100)
    town = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, default='ENGLAND')
    region = models.CharField(max_length=100, blank=True)
    have_premises = models.BooleanField(default=False)
    address_first_line = models.CharField(max_length=250, blank=True)
    postcode = models.CharField(max_length=9, blank=True)
    lat = models.DecimalField('latitude', max_digits=10, decimal_places=7)
    lng = models.DecimalField('longitude', max_digits=10, decimal_places=7)
    main_website_url = models.URLField(blank=True)
    logo_image_url = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    changed_date = models.DateTimeField(default=timezone.now)
    email = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["name"]

    def publish(self):
        self.changed_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
