from django.db import models
from datetime import datetime


class Client(models.Model):
	yfp_id = models.PositiveIntegerField(primary_key=True)
	mango_id = models.PositiveIntegerField()
	hub_url = models.CharField(max_length=125)
	first_name = models.CharField(max_length=125)
	last_name = models.CharField(max_length=125)
	fb_page = models.CharField(max_length=125, blank=True)
	fb_group = models.CharField(max_length=125, blank=True)
	is_active = models.BooleanField(default=True)
	date_added = models.DateTimeField(default=datetime.now)


	# def __str__(self):
	# 	return f'{self.first_name} {self.last_name}'

