# Create your models here.
from django.db import models


class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Instructor(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE,
        related_name='cursos'
    )
    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name='cursos'
    )

    def __str__(self):
        return self.titulo


class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    cursos = models.ManyToManyField(
        Curso,
        through='Inscripcion',
        related_name='estudiantes'
    )
    # Relación M2M con Tarea a través de Entrega
    tareas = models.ManyToManyField(
        'Tarea',
        through='Entrega',
        related_name='+'  # sin reverse para evitar conflictos
    )

    def __str__(self):
        return self.nombre


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('estudiante', 'curso')

    def __str__(self):
        return f"{self.estudiante} inscrito en {self.curso}"


class Tarea(models.Model):
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='tareas'
    )
    titulo = models.CharField(max_length=200)
    fecha_entrega = models.DateTimeField()
    # Relación M2M con Estudiante a través de Entrega; no crea reverse en Estudiante
    estudiantes = models.ManyToManyField(
        'Estudiante',
        through='Entrega',
        related_name='+'
    )

    def __str__(self):
        return f"{self.titulo} ({self.curso})"


class Entrega(models.Model):
    tarea = models.ForeignKey(
        Tarea,
        on_delete=models.CASCADE,
        related_name='entregas'
    )
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name='entregas'
    )
    fecha_envio = models.DateTimeField()
    calificacion = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        unique_together = ('tarea', 'estudiante')

    def __str__(self):
        return f"Entrega de {self.estudiante} para {self.tarea}"
