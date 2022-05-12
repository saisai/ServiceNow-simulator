from django.db import models

# Registration Form for Coordinator
class CoordinatorRegistration(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "coordinator"
