from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    adult = models.TextField(blank=True)
    original_language = models.TextField(blank=True)
    original_title = models.TextField(blank=True)
    title = models.TextField(blank=True)
    overview = models.TextField(blank=True)
    release_date = models.DateField(blank=True)
    genres = models.TextField(blank=True)
    production_countries = models.TextField(blank=True)
    videos = models.TextField(blank=True)
    images = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('movies detail', kwargs={'pk':self.id})

    class Meta:
        app_label = "movies_crud"
        db_table = "movies_nonhegemony"
        managed = False