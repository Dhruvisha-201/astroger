from django import forms
from astroakshat.models import *

class Daily_Horoscopeform(forms.ModelForm):
    class Meta:
        model = Daily_Horoscope
        fields = ["sign_id","horoscope_date","horoscope_title","horoscope_description"]

