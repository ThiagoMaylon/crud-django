from django.db import models

class Post(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    post = models.CharField('Postagem', max_length=100)

    def __str__(self):
        return self.titulo
