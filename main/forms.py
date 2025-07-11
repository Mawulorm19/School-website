from django import forms
from django_countries.fields import CountryField
import phonenumbers
from django.core.exceptions import ValidationError

# Gender choices
GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

class BaseApplicationForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES)
    age = forms.IntegerField(label='Age', min_value=1)  # ✅ Now shared by both
    email = forms.EmailField(label='Email Address')
    country = CountryField(blank_label='Select Country').formfield()
    contact_number = forms.CharField(label='Contact Number', max_length=20)

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        country = self.cleaned_data.get('country')

        try:
            parsed_number = phonenumbers.parse(contact_number, country.code)
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValidationError("Invalid phone number for selected country.")
        except phonenumbers.NumberParseException:
            raise ValidationError("Could not parse phone number. Please check the format.")

        return contact_number



class StudentApplicationForm(BaseApplicationForm):
    age = forms.IntegerField(label='Age', min_value=1)
    grade = forms.IntegerField(label='Desired Grade', min_value=1)  # Only positive integers

    # Rename contact number label
    contact_number = forms.CharField(label='Parent Contact', max_length=20)


class TeacherApplicationForm(BaseApplicationForm):
    subject = forms.CharField(label='Subject You Teach')
    qualification = forms.CharField(label='Qualification')
