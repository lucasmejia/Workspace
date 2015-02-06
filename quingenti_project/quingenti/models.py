from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Gig(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	price = models.IntegerField(default=0)
	description = models.CharField(max_length=7000)
	views = models.IntegerField(default=0)
	

	def __unicode__(self):
		return self.title
