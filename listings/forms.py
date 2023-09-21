from django import forms
from realtors.models import Realtor
from .models import Listing
from django.forms import ModelForm

class PLForm(ModelForm):
    realtor = forms.ModelChoiceField(queryset=Realtor.objects.all())
    title = forms.CharField(required=True)
    intention=forms.CharField(required=True)

    # username who posts the add 
    user_id=forms.CharField(required=True)

    # location
    address = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    zipcode = forms.CharField(required=True)
    description = forms.CharField(required=False)

    # pricing
    price = forms.IntegerField(required=True)

    # measurement
    bedrooms = forms.IntegerField(required=True)
    bathrooms = forms.DecimalField()
    garage = forms.IntegerField()
    sqft = forms.IntegerField()
    lot_size = forms.IntegerField(required=False)

    # media
    photo_main = forms.ImageField(required=True)
    photo_1 = forms.ImageField(required=False)
    photo_2 = forms.ImageField(required=False)
    photo_3 = forms.ImageField(required=False)
    photo_4 = forms.ImageField(required=False)
    photo_5 = forms.ImageField(required=False)
    photo_6 = forms.ImageField(required=False)

    class Meta:
        model=Listing
        exclude = ('is_published','list_date',)
        fields=('realtor','user_id','title','intention','address','city','state','zipcode','description','price','bedrooms',
        'bathrooms','garage','sqft','lot_size','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6',)
        