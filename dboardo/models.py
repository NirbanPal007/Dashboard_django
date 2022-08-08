from django.db import models

# Create your models here.

# Topic table.
class Topic(models.Model):
    topic_name=models.CharField(max_length=30)


#Subtopic table 
class Report(models.Model):
    report_name=models.CharField(max_length=30)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)


#Component Type table
class ComponentType(models.Model):
    type_name=models.CharField(max_length=50)

#Components table
class Component(models.Model):
    order_no=models.IntegerField(unique=True)
    report=models.ForeignKey(Report,on_delete=models.CASCADE)
    type=models.ForeignKey(ComponentType,on_delete=models.CASCADE)


