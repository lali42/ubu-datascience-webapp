from django.db import models

# Create your models here.
class PrimeMinister(models.Model):
    #fields
    #pip
    pip = models.AutoField(primary_key=True)
    #ชื่อ(name)
    name = models.CharField(max_length=500)
    #วันกิด(dob)
    dob = models.DateField()
    #วันที่รับตำแหน่ง(startdate)
    startdate = models.DateField()
    #วันที่พ้นตำแหน่ง(enddate)
    enddate = models.DateField()
    #รูป(imageurl)
    imgurl = models.CharField(max_length=500, default='')
    #พรรด(party)
    party = models.CharField(max_length=500, default='')
    #constructor
    
    #methods
    def __str__(self):
        return f'{self.name}จากพรรค{self.party}'
