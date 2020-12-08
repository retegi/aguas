from django.db import models
from applications.company.models import Company
from applications.users.models import User

class Employee(models.Model):
    name_employee = models.CharField('Nombre', max_length=50)
    lastName1_employee = models.CharField('Apellido1', max_length=50,null=True, blank=True)
    lastName2_employee = models.CharField('Apellido2', max_length=50,null=True, blank=True)
    company_employee = models.ForeignKey(Company, on_delete=models.CASCADE,null=True, blank=True)
    user_employee = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['name_employee']

    def __str__(self):
        return str(self.name_employee) + ' ' + str(self.lastName1_employee)