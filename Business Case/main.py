from asyncio.windows_events import NULL
from fastapi import FastAPI
from database import Empresa, Vacante, database as connection
from schemas import *

app = FastAPI(title = 'Business Case')

# Se conecta a la Base de Datos
@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
    
    connection.create_tables([Vacante])
    connection.create_tables([Empresa])

# Se desconecta de la Base de Datos
@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

# Pantalla de Inicio
@app.get('/')
async def index():
    return 'Hola Mundo'

# Cargar nuevo vacante
@app.post('/nuevovacante')
async def nuevovacante(vacante_request: VacanteRequestModel):
    Vacante = Vacante.create(
        PositionName = vacante_request.PositionName,
        CompanyId = vacante_request.CompanyId,
        Salary = vacante_request.Salary,
        MaxExperience = vacante_request.MaxExperience,
        MinExperience = vacante_request.MinExperience,
        VacancyId = vacante_request.VacancyId,
        VacantyLink = vacante_request.VacantyLink,
        Skills = vacante_request.Skills
    )
    return vacante_request

# Cargar nueva empresa
@app.post('/nuevoempresa')
async def nuevoempresa(empresa_request: EmpresaRequestModel):
    Empresa = Empresa.create(
        Name = empresa_request.Name,
        Link = empresa_request.Link,
        City = empresa_request.City,
        DateAdded = empresa_request.DateAdded,
        ContactFirstName = empresa_request.ContactFirstName,
        ContactLastName = empresa_request.ContactLastName,
        ContactPhoneNumber = empresa_request.ContactPhoneNumber,
        ContactEmail = empresa_request.ContactEmail,
        CompanyId = empresa_request.CompanyId,
        Country = empresa_request.Country
    )
    return empresa_request

# Buscar vacante
@app.get('/vacante/{Vacante_Id}')
async def get_vacante(Vacante_Id):
    vacante = Vacante.select().where(Vacante.VacancyId == Vacante_Id).first()

    if vacante:
        return vacante
    else:
        return 'El vacante no existe'

# Buscar empresa
@app.get('/empresa/{Empresa_Id}')
async def get_empresa(Empresa_Id):
    empresa = Empresa.select().where(Empresa.CompanyId == Empresa_Id).first()

    if empresa:
        return empresa
    else:
        return 'La empresa no existe'

# Modificar un vacante
@app.put('/editvacante/{Vacante_Id}{Position_Name}{Company_Id}{Salary}{Max_Experience}{Min_Experience}{Vacanty_Link}{Skills}')
async def edit_vacatente(Vacante_Id, Position_Name, Company_Id, Salary, Max_Experience, Min_Experience, Vacanty_Link, Skills):
    vacante = Vacante.select().where(Vacante.VacancyId == Vacante_Id).first()

    if vacante:
        if Position_Name is not NULL:
            vacante.PositionName = Position_Name
        if Company_Id is not NULL:
            vacante.CompanyId = Company_Id
        if Salary is not NULL:
            vacante.Salary = Salary
        if Max_Experience is not NULL:
            vacante.MaxExperience = Max_Experience
        if Min_Experience is not NULL:
            vacante.MinExperience = Min_Experience
        if Vacanty_Link is not NULL:
            vacante.VacantyLink = Vacanty_Link
        if Skills is not NULL:
            vacante.Skills =Skills
        Vacante.delete().where(Vacante.VacancyId == Vacante_Id).first()
        Vacante.create(vacante)
        return vacante
    else:
        return 'El vacante no existe'  

# Modificar una empresa
@app.delete('/editempresa/{Empresa_Id}{Name}{Link}{City}{Date_Added}{Contact_FirstName}{Contact_LastName}{Contact_PhoneNumber}{Contact_Email}{Country}')
async def edit_empresa(Empresa_Id, Name, Link, City, Date_Added, Contact_FirstName, Contact_LastName, Contact_PhoneNumber, Contact_Email, Country):
    empresa = Empresa.select().where(Empresa.CompanyId == Empresa_Id).first()

    if empresa:
        if Name is not NULL:
            empresa.Name = Name
        if Link is not NULL:
            empresa.Link = Link
        if City is not NULL:
            empresa.City = City
        if Date_Added is not NULL:
            empresa.DateAdded = Date_Added
        if Contact_FirstName is not NULL:
            empresa.ContactFirstName = Contact_FirstName
        if Contact_LastName is not NULL:
            empresa.ContactLastName = Contact_LastName
        if Contact_PhoneNumber is not NULL:
            empresa.ContactPhoneNumber =Contact_PhoneNumber
        if Contact_Email is not NULL:
            empresa.ContactEmail = Contact_Email
        if Country is not NULL:
            empresa.Country = Country
        Empresa.delete().where(Empresa.CompanyId == Empresa_Id).first()
        Empresa.create(empresa)
        return empresa
    else:
        return 'La empresa no existe'  

# Eliminar una vacante
@app.delete('/deletevacante/{Vacante_Id}')
async def delete_vacante(Vacante_Id):
    vacante = Vacante.select().where(Vacante.VacancyId == Vacante_Id).first()

    if vacante:
        Vacante.delete().where(Vacante.VacancyId == Vacante_Id).first()
        return 'Vacante eliminado'
    else:
        return 'El vacante no existe'

# Eliminar una empresa
@app.delete('/deleteempresa/{Empresa_Id}')
async def delete_empresa(Empresa_Id):
    empresa = Empresa.select().where(Empresa.CompanyId == Empresa_Id).first()

    if empresa:
        Empresa.delete_by_id().where(Empresa.CompanyId == Empresa_Id).first()
        return 'Empresa eliminada'
    else:
        return 'La empresa no existe'