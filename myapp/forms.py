from django import forms
from .models import Participant, validate_manufacture_date, Vehicle
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        validators=[RegexValidator(regex=r'.*@ur.ac.rw$', message='Email must end with @ur.ac.rw')],
        widget=forms.EmailInput(attrs={'placeholder': 'example@ur.ac.rw'})
    )
    
    reference_number = forms.IntegerField(
        validators=[
            MinValueValidator(99, message='Reference number must be between 99 and 999'),
            MaxValueValidator(999, message='Reference number must be between 99 and 999')
        ],
        widget=forms.NumberInput(attrs={'placeholder': 'Reference number between 99 and 999'})
    )


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['make', 'model', 'plate_number', 'manufacture_date', 'color', 'participant']
    manufacture_date = forms.IntegerField(
        validators=[validate_manufacture_date],
        widget=forms.TextInput(attrs={'placeholder': 'whole number between 2000 to the current year'})
    )

    def clean_manufacture_date(self):
        manufacture_date = self.cleaned_data['manufacture_date']
        validate_manufacture_date(manufacture_date)
        return manufacture_date

    

