from peewee import *
from fastapi import Depends


database = PostgresqlDatabase(
    'BusinesCaseDataBase'
)

# Clase de Vacantes y sus atributos
class Vacante(Model):
    PositionName = CharField(max_length = 25, null = False)
    CompanyId = IntegerField(null = False)
    Salary = IntegerField(null = False)
    MaxExperience = IntegerField(null = False)
    MinExperience = IntegerField(null = False)
    VacancyId = IntegerField(null = False)
    VacantyLink = CharField(max_length = 255, null = False)
    Skills = CharField(max_length = 255, null = True)

    class Meta:
        database = database
        table_name = "Vacantes"

# Clase de Empresa y sus atributos
class Empresa(Model):
    Name = CharField(max_length = 25, null = False)
    Link = CharField(max_length = 255, null = False)
    City = CharField(max_length = 25, null = False)
    DateAdded = DateField(null = False)
    ContactFirstName = CharField(max_length = 25, null = False)
    ContactLastName = CharField(max_length = 25, null = False)
    ContactPhoneNumber = IntegerField(null = False)
    ContactEmail = CharField(max_length = 255, null = False)
    CompanyId = IntegerField(null = False)
    Country = CharField(max_length = 25, null = False)

    class Meta:
        database = database
        table_name = "Empresas"