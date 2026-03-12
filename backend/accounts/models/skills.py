from django.db import models


class Skills(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


    class Meta:
        verbose_name = "Competences"

    def __str__(self):
        return f"{self.name} - {self.description}"
    
