from django.db import models

# Create your models here.

class Name_input(models.Model):
    name = models.CharField(max_length=200, blank=False)
    
    def __unicode__(self):
        return self.name


class Email_input(models.Model):
    email = models.EmailField()
    person = models.ForeignKey(Name_input, null=True)
    
    def __unicode__(self):
        return self.email

