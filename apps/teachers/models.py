from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-mail', max_length=100)
    
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering =['id']

    def __str__(self):
        return self.name