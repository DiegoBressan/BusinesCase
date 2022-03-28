from datetime import datetime
import imp
from re import S
from pydantic import BaseModel

class VacanteRequestModel(BaseModel):
    PositionName: str
    CompanyId: int
    Salary: int
    MaxExperience: int
    MinExperience: int
    VacancyId: int
    VacantyLink: str
    Skills: str

class EmpresaRequestModel(BaseModel):
    Name: str
    Link: str
    City: str
    DateAdded: datetime
    ContactFirstName: str
    ContactLastName: str
    ContactPhoneNumber: int
    ContactEmail: str
    CompanyId: int
    Country: str