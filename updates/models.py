from django.db import models


# Create your models here.

class Update(models.Model):
    title = models.CharField(max_length=50, help_text='Enter the Title')
    body = models.TextField(default='test')
    date_pub = models.DateTimeField(auto_now=True)
    
    def create(self):
        self.save()

    def __str__(self):
        return '{}{}{}'.format(self.title, self.body, self.date_pub)
        

    