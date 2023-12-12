from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = Age,	Sex,	Cholesterol,	BloodPressure(Upper),	BloodPressure(Lower),	HeartRate,	Diabetes,	FamilyHistory,	Smoking,	
# Obesity,	AlcoholConsumption,	ExerciseHoursPerWeek,	Diet,	PreviousHeartProblems,	MedicationUse,	StressLevel,	SedentaryHoursPerDay,	
# Income, BMI,	Triglycerides,	PhysicalActivityDaysPerWeek,	SleepHoursPerDay,	Diagnostic

class Paciente(Base):
    __tablename__ = 'pacientes'
    
    id = Column(Integer, primary_key=True)
    name= Column("Name", String(50))
    age = Column("Age", Integer)
    sex = Column("Sex", Integer)
    chol = Column("Cholesterol", Integer)
    blup = Column("BloodPressure(Upper)", Integer)
    bllow = Column("BloodPressure(Lower)", Integer)
    rate = Column("HeartRate", Integer)
    dia = Column("Diabetes", Integer)
    fam = Column("FamilyHistory", Integer)
    smok = Column("Smoking", Integer)
    obes = Column("Obesity", Integer)
    alco = Column("AlcoholConsumption", Integer)
    exer = Column("ExerciseHoursPerWeek", Float)
    diet = Column("Diet", Integer)
    prev = Column("PreviousHeartProblems", Integer)
    medi = Column("MedicationUse", Integer)
    stress = Column("StressLevel", Integer)
    seden = Column("SedentaryHoursPerDay", Float)
    income = Column("Income", Float)
    bmi = Column("BMI", Float)
    trigly = Column("Triglycerides", Integer)
    activity = Column("PhysicalActivityDaysPerWeek", Integer)
    sleep = Column("SleepHoursPerDay", Integer)
    outcome = Column("Diagnostic", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, name: str, age: int, sex: int, chol: int, blup: int, bllow: int, rate: int,
    dia: int, fam: int, smok: int, obes: int, alco: int, exer: float, diet: int, prev: int,
    medi: int, stress: int,seden: float, income: float, bmi: float, trigly: int, activity: int,
    sleep: int, outcome:int, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Paciente

        Arguments:
        name: nome do paciente
            age: idade do paciente
            sex: genero do paciente (Homem = 0, Mulher = 1)
            chol: nivel de colesterol
            blup: pressão sanguinea superior (utilizar o numero superior ex. 148/88 utilizar 148) 
            bllow: pressão sanguinea inferior (utilizar o numero inferior ex. 148/88 utilizar 88) 
            rate: batimento cardiaco
            dia: se o paciente tem ou náo diabetes (Não = 0, Sim = 1)
            fam: se o paciente tem historico familiar de infarto (Não = 0, Sim = 1)
            smok: se o paciente é fumante (Não = 0, Sim = 1) 
            obes: se o paciente é obeso (Não = 0, Sim = 1)
            alco: se o paciente faz uso de alcool (Não = 0, Sim = 1)
            exer: horas de exercicio por semana
            diet: tipo de dieta do paciente (não saudável = -1, neutra = 0, saudável = 1)
            prev: histórico de problema cardíaco (Não = 0, Sim = 1)
            medi: se o apciente faz uso de algum medicamento contínuo (Não = 0, Sim = 1)
            stress: nível de stress (de 0 a 10)
            seden: horas de sedentarismo por semana
            income: salário anual em dolar (dividir valor por 1000)
            bmi: índice de massa corporal (peso em kg/(altura em m)^2)
            trigly: nivel de triglicerídio
            activity: numero de dias com atividade física na semana
            sleep: horas de sono em um dia
            outcome: diagnóstico
            data_insercao: data de quando o paciente foi inserido à base
        """
        self.name=name
        self.age=age
        self.sex=sex
        self.chol=chol
        self.blup=blup
        self.bllow=bllow
        self.rate=rate
        self.dia=dia
        self.fam=fam
        self.smok=smok
        self.obes=obes
        self.alco=alco
        self.exer=exer
        self.diet=diet
        self.prev=prev
        self.medi=medi
        self.stress=stress
        self.seden=seden
        self.income=income
        self.bmi=bmi
        self.trigly=trigly
        self.activity=activity
        self.sleep=sleep
        self.outcome = outcome

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao