from django import forms
from .import models


class UserLoginForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField()

class changepasswordForm(forms.Form):
    cp=forms.CharField(required=False)
    np=forms.CharField(required=False)
    cnp=forms.CharField(required=False)

class HospitalForm(forms.Form):
    email=forms.CharField()
    hospital_name=forms.CharField()
    Address=forms.CharField()
    GLink=forms.CharField()
    contact_number=forms.CharField()
    h_type=forms.CharField()
    iw_occupied=forms.IntegerField(required=False)
    iw_vacant=forms.IntegerField()
    total_iw=forms.IntegerField()
    beds_occupied=forms.IntegerField(required=False)
    beds_vacant=forms.IntegerField()
    total_beds=forms.IntegerField()
    ventilators_occupied=forms.IntegerField(required=False)
    ventilators_vacant=forms.IntegerField()
    total_ventilators=forms.IntegerField()
    last_updated=forms.DateTimeField(required=False)
    password=forms.CharField()
