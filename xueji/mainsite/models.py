from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Nianji(models.Model):
    xiaoming=models.CharField(max_length=20)
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    nianji=models.ForeignKey(Nianji,on_delete=models.CASCADE)
    gonghao=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    xingbie=models.CharField(max_length=10)
    birthday=models.DateField()
    phone=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Banji(models.Model):
    nianji=models.ForeignKey(Nianji,on_delete=models.CASCADE)
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Student(models.Model):
    banji=models.ForeignKey(Banji,on_delete=models.CASCADE)
    xuehao=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    xingbie=models.CharField(max_length=10)
    birthday=models.DateField()
    jiguan=models.CharField(max_length=10)
    zhuzhi=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Chengji(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    yuwen=models.CharField(max_length=10)
    shuxue=models.CharField(max_length=10)
    yingyu=models.CharField(max_length=10)
    kexue=models.CharField(max_length=10)
    yinyue=models.CharField(max_length=10)
    meishu=models.CharField(max_length=10)
    tiyu=models.CharField(max_length=10)
    xinxi=models.CharField(max_length=10)

    def __str__(self):
        return self.yuwen

#class User(models.Model):
    #name=models.CharField(max_length=20,null=False)
    #email=models.EmailField()
    #password=models.CharField(max_length=20,null=False)
    #enabled=models.BooleanField(default=False)

    #def __str__(self):
        #return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    height=models.PositiveIntegerField(default=160)
    male=models.BooleanField(default=False)
    website=models.URLField(null=True)

    def __str__(self):
        return self.user.username