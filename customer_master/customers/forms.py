# forms.py

from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'salesperson': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.RadioSelect(choices=[(True, 'Active'), (False, 'Inactive')]),
            'tax_id': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'branches': forms.SelectMultiple(attrs={'class': 'form-control'}),  
        }

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['tax_registration_date'].widget = forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'placeholder': 'YYYY-MM-DD'
        })

        self.fields['arabic_name'].widget.attrs.update({
            'pattern': '[\u0600-\u06FF]+',
            'title': 'Arabic characters only',
            'class': 'form-control'
        })
        self.fields['cr_number'].widget.attrs.update({
            'pattern': '\d+',
            'title': 'Numbers only',
            'class': 'form-control'
        })
        self.fields['mobile_number'].widget.attrs.update({
            'pattern': '\d+',
            'title': 'Numbers only',
            'class': 'form-control'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['additional_number'].widget.attrs.update({
            'pattern': '\d+',
            'title': 'Numbers only',
            'class': 'form-control'
        })
        self.fields['building_number'].widget.attrs.update({
            'pattern': '\d+',
            'title': 'Numbers only',
            'class': 'form-control'
        })
        self.fields['unit_number'].widget.attrs.update({
            'pattern': '\d+',
            'title': 'Numbers only',
            'class': 'form-control'
        })
        self.fields['postal_code'].widget.attrs.update({
            'pattern': '\d+',
            'title': 'Numbers only',
            'class': 'form-control'
        })

    def clean(self):
        cleaned_data = super().clean()
        country = cleaned_data.get('country')
        city = cleaned_data.get('city')

        # Perform custom validation to ensure city is valid for the selected country
        if country and city:
            valid_cities_by_country = {
                  'Country 1': ['city1', 'city2'],
                'Country 2': ['city3', 'city4'],
            }

            if city not in valid_cities_by_country.get(country, []):
                self.add_error('city', f'{city} is not a valid city for {country}')

        return cleaned_data
