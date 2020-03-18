from django.db import models

# Create your models here.

# class Road(models.Model):

#     road = models.CharField(blank=False, max_length=120)
#     zone_code = models.CharField(blank=True, max_length=5)
#     zone = models.CharField(blank=True, max_length=30)
#     borough = models.CharField(blank=True, max_length=30)
#     suspension_href = models.TextField(blank=True, null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['-updated', '-created']
#         unique_together = ['road', 'borough', 'zone']

#     def get_absolute_url(self):  # get_absolute_url

#         return reverse('roads:detail', kwargs={'pk': self.pk})

#     def __str__(self):
#         return '%s' % self.road
    