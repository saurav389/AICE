from django.db import models

# Create your models here.
class AddSite(models.Model):
    site = models.CharField(blank = False, max_length=150, verbose_name = 'Site')
    def __str__(self):
        return '{site}'.format(site=self.site)
class AddDepartment(models.Model):
    Department = models.CharField(blank = False, max_length=150, verbose_name = 'Department')
    def __str__(self):
        return '{Depart}'.format(Depart=self.Department)
class AddDesignation(models.Model):
    Designation = models.CharField(blank = False, max_length=150, verbose_name = 'Designation')
    def __str__(self):
        return '{Desig}'.format(Desig=self.Designation)
class AddCategory(models.Model):
    Category = models.CharField(blank = False, max_length=150, verbose_name = 'Category')
    def __str__(self):
        return '{Category}'.format(Category=self.Category)
class Rate(models.Model):
    site = models.ForeignKey(AddSite,on_delete=models.CASCADE)
    category = models.ForeignKey(AddCategory,on_delete=models.CASCADE,default=False)
    rate = models.IntegerField(blank=True,default=False)
    def __str__(self):
        return '{site}'.format(site =self.site)
    