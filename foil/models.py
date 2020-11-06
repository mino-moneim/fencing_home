from django.db import models
from django.utils.text import slugify

# Create your models here.

Size = (
    ('normal','normal'),
    ('mini','mini')
)

class Foil(models.Model):
    
    title = models.CharField(max_length=50)
    weapon_name = models.CharField(max_length=50)
    size = models.CharField(max_length=50, choices=Size)
    slug = models.SlugField(blank=True, null=True)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        
    
    def __str__(self):
        return self.title