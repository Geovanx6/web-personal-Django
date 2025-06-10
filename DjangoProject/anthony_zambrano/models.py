
# Create your models here.
from django.db import models

class Departament(models.Model):
    Name = models.CharField(max_length=150, verbose_name="Departamento")

    def __str__(self):
        return self.Name
    class Meta:
        db_table = "departament"
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ['id']

class Job(models.Model):
    Name = models.CharField(max_length=150, verbose_name="Cargo", unique=True)

    def __str__(self):
        return self.Name
    class Meta:
        db_table = "job"
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        ordering = ['id']

class Employed(models.Model):
    Name = models.CharField(max_length=50, verbose_name="Nombre")
    Lastname = models.CharField(max_length=50, verbose_name="Apellido")
    Salary = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name="Salario")
    Email = models.EmailField(max_length=50,verbose_name="Email")
    Direction = models.CharField(max_length=100, verbose_name="Direccion")
    Birthdate = models.DateField(verbose_name="Fecha de nacimento")
    Cellphone = models.CharField(max_length=50, verbose_name="Celular")
    Job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="Cargo")
    Departament = models.ManyToManyField(Departament)

    def __str__(self):
        return self.Name
    class Meta:
        db_table = "employed"
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['id']
