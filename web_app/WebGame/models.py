from django.db import models

prefix_choices =(
    (1,"นาย"),
    (2,"นางสาว"),
    (3,"นาง"),
)

class Major(models.Model):
    
    name = models.CharField(max_length=255)
    
    class Meta:
            verbose_name = 'Major'
            verbose_name_plural = 'Majors'
    
    def __str__(self):
        return self.name


class Student(models.Model):
    std_id =    models.IntegerField()
    prefix = models.IntegerField(choices=prefix_choices,    default=1)
    name=       models.CharField(max_length=255)
    lastname=   models.CharField(max_length=255)
    phone =     models.CharField(max_length=255)
    address=    models.TextField()
    major = models.ForeignKey(Major, on_delete=models.CASCADE, default=1)
    

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return self.name + " " + self.lastname
