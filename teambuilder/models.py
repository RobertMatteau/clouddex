from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	userid = models.IntegerField(default=0)
	email = models.CharField(max_length=200)
	fname = models.CharField(max_length=200)
	lname = models.CharField(max_length=200)
	
class Team(models.Model):
	teamname = models.CharField(max_length=200)
	owner = models.CharField(max_length=200, default="admin")
	comment = models.CharField(max_length=600, default="This team is terrible")
	rating = models.IntegerField(default=3)
	view = models.IntegerField(default=0)
	def __str__(self):
		return self.teamname
	
class TeamMember(models.Model):
	teamid = models.IntegerField(default=0)
	position = models.IntegerField(default=0)
	pname = models.CharField(max_length=50)
	pability = models.CharField(max_length=50)
	pitem = models.CharField(max_length=50)
	movea = models.CharField(max_length=50)
	moveb = models.CharField(max_length=50)
	movec = models.CharField(max_length=50)
	moved = models.CharField(max_length=50)
	def __str__(self):
		return self.pname
	
class Pokemon(models.Model):
	pnum = models.IntegerField(default=0)
	pname = models.CharField(max_length=50)
	primarytype = models.CharField(max_length=50)
	secondarytype = models.CharField(max_length=50)
	hp = models.IntegerField(default=0)
	attack = models.IntegerField(default=0)
	defense = models.IntegerField(default=0)
	spattack = models.IntegerField(default=0)
	spdefense = models.IntegerField(default=0)
	speed = models.IntegerField(default=0)
	
class Item(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=400)
	
class Move(models.Model):
	name = models.CharField(max_length=50)
	pors = models.CharField(max_length=10)
	type = models.CharField(max_length=50)
	power = models.IntegerField(default=0)
	accuracy = models.IntegerField(default=0)
	description = models.CharField(max_length=400)

class Comment(models.Model):
	username = models.CharField(max_length=200)
	teamid = models.IntegerField(default=0)
	message = models.CharField(max_length=600)
	rating = models.IntegerField(default=3)