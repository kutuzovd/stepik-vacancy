from django.db import models



class Vacancy(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    speciality = models.ForeignKey('Speciality', on_delete=models.CASCADE, related_name='speciality', default=None, null=True, blank=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='company', default=None, null=True, blank=True)
    skills = models.CharField(max_length=128)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True)
    location = models.CharField(max_length=32, blank=True)
    logo = models.CharField(max_length=128, blank=True)
    desc = models.TextField(blank=True)
    employee_count = models.IntegerField(blank=True, null=True)
    vacancies = models.ForeignKey('Vacancy', on_delete=models.CASCADE, related_name='vacancy', default=None, null=True, blank=True)


class Speciality(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=128)
    title = models.CharField(max_length=32)
    picture = models.CharField(max_length=128, blank=True)

