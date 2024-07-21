from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from multiselectfield import MultiSelectField
#RegexValidator, MinLengthValidator, MaxLengthValidator: These are validators from django.core.validators used to enforce certain constraints on model fields.
SALESPERSON_CHOICES = [
    ('salesperson1', 'Salesperson 1'),
    ('salesperson2', 'Salesperson 2'),
    ('salesperson3', 'Salesperson 3'),
    
]
CITY_CHOICES = [
    ('city1', 'City 1'),
    ('city2', 'City 2'),
    ('city3', 'City 3'),
    ('city4', 'City 4'),
    
]

BRANCH_CHOICES = [
    ('branch1', 'Branch 1'),
    ('branch2', 'Branch 2'),
    ('branch3', 'Branch 3'),
    
]


class Customer(models.Model):
    salesperson = models.CharField(max_length=100, choices=SALESPERSON_CHOICES)
    name = models.CharField(max_length=100)
    tax_registration_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(regex=r'^.*00003$', message='Must end with 00003'),
            MinLengthValidator(15)
        ]
    )
    cr_number = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10), MaxLengthValidator(10)]
    )
    primary_contact = models.CharField(max_length=100)
    email = models.EmailField()
    branches = MultiSelectField(choices=BRANCH_CHOICES)
    tax_id = models.CharField(max_length=100, choices=[('Tax ID 1', 'Tax ID 1'), ('Tax ID 2', 'Tax ID 2')])
    status = models.BooleanField(default=True)
    id_number = models.CharField(max_length=100, unique=True)
    arabic_name = models.CharField(max_length=100)
    tax_registration_date = models.DateField()
    mobile_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{10}$', message='Must be 10 digits')]
    )
    website = models.URLField()
    payment_terms = models.CharField(max_length=100)
    country = models.CharField(max_length=100, choices=[('Country 1', 'Country 1'), ('Country 2', 'Country 2')])
    region = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    additional_number = models.CharField(
        max_length=4,
        validators=[RegexValidator(regex=r'^\d{4}$', message='Must be 4 digits')]
    )
    unit_number = models.CharField(
        max_length=4,
        validators=[MaxLengthValidator(4)]
    )
    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    street = models.CharField(max_length=100)
    additional_street = models.CharField(max_length=100)
    building_number = models.CharField(
        max_length=4,
        validators=[RegexValidator(regex=r'^\d{4}$', message='Must be 4 digits')]
    )
    postal_code = models.CharField(
        max_length=5,
        validators=[RegexValidator(regex=r'^\d{5}$', message='Must be 5 digits')]
    )

    def __str__(self):
        return self.name
