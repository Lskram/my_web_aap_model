from django.db import models

class Student(models.Model):
    std_id =    models.IntegerField()
    name=       models.CharField(max_length=255)
    lastname=   models.CharField(max_length=255)
    phone =     models.CharField(max_length=255)
    address=    models.TextField()
    

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
