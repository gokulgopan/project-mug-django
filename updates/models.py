from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Update(models.Model):
    title = models.CharField(max_length=100, help_text='Enter the Title')
    body = models.TextField()
    date_pub = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete='CASCADE', default="None")
    
    def create(self):
        self.save()

    def __str__(self):
        return '{}{}{}'.format(self.title, self.body, self.date_pub)
        
    def snippet(self):
        return self.body[:50] + '...'
    

    