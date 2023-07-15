from django.db import models

class AnimeImage(models.Model):
    image = models.ImageField(upload_to='anime_imagenes/')
    generated_image = models.ImageField(upload_to='anime_imagenes/generated/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AnimeImage {self.id}"

        