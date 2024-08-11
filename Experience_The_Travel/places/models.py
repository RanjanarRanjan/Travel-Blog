from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Typology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField

    class meta:
        db_table='places_typology'
        verbose_name=_('typology')
        verbose_name_plural=_('typologies')
        ordering=('id',)


    def __str__(self):
        return self.name

    
class Place(models.Model):
    DESTINATION_TYPES = (
        ('', 'All'),
        ('beach', 'Beach'),
        ('mountain', 'Mountain'),
        ('city', 'City'),
        ('forest', 'Forest'),
    )
    
    DIFFICULTY_LEVELS = (
        ('easy', 'Easy'),
        ('difficult','Difficult'),
        ('challenging','Challenging'),
        ('medium','Medium'),
    )

    DURATIONS = (
        ('5 days', '5 days'),
        ('10 days', '10 days'),
        ('15 days', '15 days'),
        ('1 week', '1 week'),
    )
    
    name = models.CharField(max_length=255)
    destination_type = models.CharField(max_length=50, choices=DESTINATION_TYPES)
    duration = models.CharField(max_length=50, choices=DURATIONS,null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_LEVELS,null=True, blank=True)
    description_heading = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField()
    country = models.CharField(max_length=100,null=True, blank=True)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)
    short_description=models.CharField(max_length=300,null=True, blank=True)
    typologies = models.ManyToManyField(Typology, related_name='places')
    
    class meta:
        db_table='places_place'
        verbose_name=_('place')
        verbose_name_plural=_('places')
        ordering=('id',)

    def __str__(self):
        return self.name
    
# class Placeimage(models.Model):
#     name = models.ForeignKey(Place,related_name='profile_image',on_delete=models.CASCADE)
#     class Meta:
#         db_table = 'places_placeimage'
#         verbose_name = _('place image')
#         verbose_name_plural = _('place images')
#         ordering = ('id',)

#     def __str__(self):
#         return f"Image for {self.place.name}"
