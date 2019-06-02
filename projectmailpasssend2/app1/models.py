from django.db import models
class Student_Modle(models.Model):
    idno=models.IntegerField()
    name=models.CharField(max_length=30)
    cno=models.IntegerField()
    gender=models.CharField(max_length=20)
    image=models.ImageField(upload_to='emp/',default=False)
    email=models.EmailField(max_length=30,primary_key=True)
    password=models.CharField(max_length=20)

