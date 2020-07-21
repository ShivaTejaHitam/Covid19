from django.db import models
from django.utils import timezone

class Hospital(models.Model):
    email=models.CharField(max_length=100,primary_key=True,default=0)
    hospital_name=models.CharField(max_length=500,default=None,null=False,verbose_name="Hospital")
    Address=models.CharField(max_length=500,default=None,null=False,verbose_name="Address")
    GLink=models.CharField(max_length=500,default=None,null=False,verbose_name="GLink")
    contact_number=models.CharField(max_length=15,default=None,null=False,verbose_name="Contact Number")
    h_type=models.CharField(max_length=5,default=None,null=False,verbose_name="Hospital Type")
    iw_occupied=models.IntegerField(default=0,null=True,blank=True,verbose_name="Occupied Isolation Wards")
    iw_vacant=models.IntegerField(default=0,null=True,blank=True,verbose_name="Vacant Isolation Wards")
    total_iw=models.IntegerField(default=0,null=True,blank=True,verbose_name="Total Isolation Wards")
    beds_occupied=models.IntegerField(default=0,null=True,blank=True,verbose_name="Occupied beds")
    beds_vacant=models.IntegerField(default=0,null=True,blank=True,verbose_name="Vacant beds")
    total_beds=models.IntegerField(default=0,null=True,blank=True,verbose_name="Total Beds")
    ventilators_occupied=models.IntegerField(default=0,null=True,blank=True,verbose_name="Occupied Ventilators")
    ventilators_vacant=models.IntegerField(default=0,null=True,blank=True,verbose_name="Vacant Ventilators")
    total_ventilators=models.IntegerField(default=0,null=True,blank=True,verbose_name="Total Ventilators")
    last_updated=models.DateTimeField(verbose_name="Last Updated",blank=True,default=timezone.now)
    password=models.CharField(max_length=20,default=None,blank=False)


    def __str__(self):
        return self.hospital_name
    


