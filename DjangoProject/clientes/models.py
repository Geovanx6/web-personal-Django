from django.db import models

# Create your models here.
from django.db import models

class Type(models.Model):
    Name = models.CharField(max_length=150, verbose_name="Nombre")

    def __str__(self):
        return self.Name
    class Meta:
        db_table = "Type"
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = ['id']

class Category(models.Model):
    Name = models.CharField(max_length=150, verbose_name="Categoria", unique=True)

    def __str__(self):
        return self.Name
    class Meta:
        db_table = "Category"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['id']

class Person(models.Model):
    category = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Tipo")
    DNI = models.CharField(max_length=10, unique=True, verbose_name="cedula")
    Name = models.CharField(max_length=50, verbose_name="nombre")
    Lastname = models.CharField(max_length=50, verbose_name="apellido")
    Age = models.PositiveIntegerField(default=0,verbose_name="edad")
    Salary = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name="salario")
    CreatedDate = models.DateTimeField(auto_now_add=True, verbose_name="fecha_creacion")
    UpdatedDate = models.DateTimeField(auto_now=True, verbose_name="fecha_modificacion")

    def __str__(self):
        return self.Name
    class Meta:
        db_table = "person"
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ['id']