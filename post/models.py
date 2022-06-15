from django.db import models

class Nursery(models.Model):
    name = models.CharField('Название', max_length=50)
    descr = models.TextField('Описание')

    def get_absolute_url(self):
        return f'/post/{self.id}/update'

    def str(self):
        return self.name
