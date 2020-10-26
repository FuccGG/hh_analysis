from django.db import models


class Vacancy(models.Model):
    vacancy_name = models.CharField(max_length=200)
    employer_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    requirements = models.TextField()
    vacancy_link = models.CharField(max_length=200)
    key_skills = models.CharField(max_length=200)

    def __str__(self):
        return self.vacancy_name


