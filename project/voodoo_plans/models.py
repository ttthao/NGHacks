# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Itinerary(models.Model):
	title = models.CharField(max_length=200)
	party = models.CharField(max_length=100)
	occasion = models.CharField(max_length=200)
	cost = models.IntegerField(default=0)
	duration = models.IntegerField(default=0)

	def __str__(self):
		return self.title

class Activity(models.Model):
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	rating = models.IntegerField(default=0)
	image_url = models.URLField(max_length=100)

	def __str__(self):
		return self.title

class Route(models.Model):
	itinerary = models.ForeignKey(
		Itinerary,
		on_delete=models.CASCADE,
		)
	activity = models.ForeignKey(
		Activity,
		on_delete=models.CASCADE,
		)
	order = models.IntegerField(default=0)
# Create your models here.
