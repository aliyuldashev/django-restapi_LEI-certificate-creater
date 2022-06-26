from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class LEI_user(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    country = models.CharField(max_length=350)
    applicant_first_name= models.CharField(max_length=450)
    applicant_last_name= models.CharField(max_length=450)
    email = models.EmailField(unique=True)
    entity_name = models.CharField(max_length=250)
    phone = PhoneNumberField(unique = True, null = False, blank = False)
    company_number = models.CharField(max_length=250)
    vat_number = models.CharField(max_length=250)
    address = models.ManyToManyField('Address',related_name='company_address',blank=True,null=True)
    parent_company = models.ForeignKey('Parent_companies',on_delete=models.DO_NOTHING,related_name='related_company',blank=True,null=True)
    reason_unprovide = models.TextField(blank=True)
    billing_type = models.ForeignKey('Billing_data',on_delete=models.DO_NOTHING,related_name='billing',blank=True,null=True)
    total_money = models.BigIntegerField(blank=True,null=True)

    def __str__(self):
        return self.applicant_full_name


class Address(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    entity_address = models.TextField()
    city = models.TextField()
    code = models.BigIntegerField()
    is_headquarter = models.BooleanField(default=False)
    def __str__(self):
        return str(self.code)
class Parent_companies(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    company_number = models.CharField(max_length=250)
    entity_name = models.CharField(max_length=250)
    address = models.ManyToManyField('Address',related_name='parent_company_address',blank=True)
    from_date = models.DateField()
    to_date = models.DateField()
    latest_date_relation = models.DateField()
    def __str__(self):
        return f'{self.entity_name} - {self.id}'

class Billing_data(models.Model):
    CHOICES = [
        ['72','one year'],
        ['189','three year'],
        ['262','five year']
    ]
    PAYMENT_CHOICES =[
        ['1','Instant Bank Payment'],
        ['2','Bank transfer'],
        ['3','Card'],
        ['4','PayPal']
    ]
    plan = models.CharField(choices=CHOICES,max_length=150)
    is_tagged = models.BooleanField(default=False)
    is_added_hardcopy = models.BooleanField(default=False)
    payment_type = models.CharField(choices=PAYMENT_CHOICES,max_length=150)






