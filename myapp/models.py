from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField

# Custom validator for checking if the date of birth is above 18 years old
def validate_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError('Participant must be 18 years or older. Format: MMDDYYYY', code='invalid')



class Participant(models.Model):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    ]

    date_of_birth = models.DateField(validators=[validate_age])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(
        validators=[RegexValidator(regex=r'.*@ur.ac.rw$', message='Email must end with @ur.ac.rw')],
        default='default@example.com'  # Add a default value here
    )
    phone_number = PhoneNumberField(max_length=13)
    reference_number = models.IntegerField(
        validators=[
            MinValueValidator(99, message='Reference number must be between 99 and 999'),
            MaxValueValidator(999, message='Reference number must be between 99 and 999')
        ]
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def clean(self):
        # Additional validation if needed
        super().clean()

    def save(self, *args, **kwargs):
        # Additional actions before saving if needed
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"











def validate_manufacture_date(value):
    current_year = date.today().year
    if value < 2000 or value > current_year:
        raise ValidationError('Manufacture date should be between 2000 and the current year.')




class Vehicle(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    plate_number_validator = RegexValidator(
    regex=r'^(RA[ABCDEFGH]|(RNP|RDF|GR|IT|CD))[0-9]{3}[0-9A-HJ-NP-Y]{1}$', 
    message='Enter a valid plate number with exactly one letter after the numbers.')



    plate_number = models.CharField(
        max_length=20, 
        validators=[plate_number_validator],
        unique=True
    )
    manufacture_date = models.IntegerField(validators=[validate_manufacture_date])
    color = models.CharField(max_length=20)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='vehicles')

    def clean(self):
        # Additional validation if needed
        super().clean()

    def save(self, *args, **kwargs):
        # Additional actions before saving if needed
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.make} {self.model} - {self.plate_number}"