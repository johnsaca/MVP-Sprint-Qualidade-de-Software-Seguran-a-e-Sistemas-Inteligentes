from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
import json
import numpy as np

class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    name: str = "Maria"
    age: int = 67
    sex: int = 1
    chol: int = 208
    blup: int = 158
    bllow: int = 88
    rate: int = 72
    dia: int = 0
    fam: int = 0
    smok: int = 1
    obes: int = 0
    alco: int = 0
    exer: float = 4.17 
    diet: int = 0
    prev: int = 0
    medi: int = 0
    stress: int = 9
    seden: float = 6.6
    income: float = 261.404
    bmi: float =  31.25
    trigly: int = 286
    activity: int = 0
    sleep: int = 6

class PacienteViewSchema(BaseModel):
    """Define como um paciente será retornado
    """
    id: int = 1
    name: str = "Maria"
    age: int = 67
    sex: int = 1
    chol: int = 208
    blup: int = 158
    bllow: int = 88
    rate: int = 72
    dia: int = 0
    fam: int = 0
    smok: int = 1
    obes: int = 0
    alco: int = 0
    exer: float = 4.17 
    diet: int = 0
    prev: int = 0
    medi: int = 0
    stress: int = 9
    seden: float = 6.6
    income: float = 261.404
    bmi: float =  31.25
    trigly: int = 286
    activity: int = 0
    sleep: int = 6
    outcome: int = None
    
class PacienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do paciente.
    """
    name: str = "Maria"

class ListaPacientesSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    pacientes: List[PacienteSchema]

    
class PacienteDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    name: str = "Maria"
    
# Apresenta apenas os dados de um paciente    
def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": paciente.id,
        "name": paciente.name,
        "age": paciente.age,
        "sex": paciente.sex,
        "chol": paciente.chol,
        "blup": paciente.blup,
        "bllow": paciente.bllow,
        "rate": paciente.rate,
        "dia": paciente.dia,
        "fam": paciente.fam,
        "smok": paciente.smok,
        "obes": paciente.obes,
        "alco": paciente.alco,
        "exer": paciente.exer, 
        "diet": paciente.diet,
        "prev": paciente.prev,
        "medi": paciente.medi,
        "stress": paciente.stress,
        "seden": paciente.seden,
        "income": paciente.income,
        "bmi": paciente.bmi,
        "trigly": paciente.trigly,
        "activity": paciente.activity,
        "sleep": paciente.sleep,
        "outcome": paciente.outcome,
    }
    
# Apresenta uma lista de pacientes
def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    result = []
    for paciente in pacientes:
        result.append({
            "id": paciente.id,
        "name": paciente.name,
        "age": paciente.age,
        "sex": paciente.sex,
        "chol": paciente.chol,
        "blup": paciente.blup,
        "bllow": paciente.bllow,
        "rate": paciente.rate,
        "dia": paciente.dia,
        "fam": paciente.fam,
        "smok": paciente.smok,
        "obes": paciente.obes,
        "alco": paciente.alco,
        "exer": paciente.exer, 
        "diet": paciente.diet,
        "prev": paciente.prev,
        "medi": paciente.medi,
        "stress": paciente.stress,
        "seden": paciente.seden,
        "income": paciente.income,
        "bmi": paciente.bmi,
        "trigly": paciente.trigly,
        "activity": paciente.activity,
        "sleep": paciente.sleep,
        "outcome": paciente.outcome,
        })

    return {"pacientes": result}

