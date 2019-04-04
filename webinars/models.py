from django.conf import settings
from django.db import models

from clients.models import Client

class Wealthy(models.Model):
	assigned_va = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)
	wealthy_client = models.OneToOneField(
		Client,
		on_delete=models.CASCADE,
		)
	promotion_type = models.CharField(
		max_length=25, 
		choices=(
		('FULL', 'Full Promotion'),
		('MINI', 'Mini Promotion'),
		('MICRO', 'Micro Promotion'),
		),
		default='FULL',		
	)
	will_promote = models.BooleanField(default=True)
	notes = models.TextField(blank=True)

	class Meta:
		verbose_name_plural = 'Wealthy'


	# def __str__(self):
	# 	return f'{self.wealthy_client.first_name} {self.wealthy_client.last_name}'