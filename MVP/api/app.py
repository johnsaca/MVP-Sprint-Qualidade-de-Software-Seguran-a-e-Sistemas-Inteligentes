from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Paciente, Model
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
paciente_tag = Tag(name="Paciente", description="Adição, visualização, remoção e predição de pacientes com Diabetes")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de pacientes
@app.get('/pacientes', tags=[paciente_tag],
         responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_pacientes():
    """Lista todos os pacientes cadastrados na base
    Retorna uma lista de pacientes cadastrados na base.
    
    Args:
        nome (str): nome do paciente
        
    Returns:
        list: lista de pacientes cadastrados na base
    """
    session = Session()
    
    # Buscando todos os pacientes
    pacientes = session.query(Paciente).all()
    
    if not pacientes:
        logger.warning("Não há pacientes cadastrados na base :/")
        return {"message": "Não há pacientes cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d pacientes econtrados" % len(pacientes))
        return apresenta_pacientes(pacientes), 200


# Rota de adição de paciente
@app.post('/paciente', tags=[paciente_tag],
          responses={"200": PacienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: PacienteSchema):
    """Adiciona um novo paciente à base de dados
    Retorna uma representação dos pacientes e diagnósticos associados.
    
    Args:
        name (str): nome do paciente
        age (int): idade do paciente
        sex (int): genero do paciente (Homem = 0, Mulher = 1)
        chol (int): nivel de colesterol
        blup (int): pressão sanguinea superior (utilizar o numero superior ex. 148/88 utilizar 148) 
        bllow (int): pressão sanguinea inferior (utilizar o numero inferior ex. 148/88 utilizar 88) 
        rate (int): batimento cardiaco
        dia (int): se o paciente tem ou náo diabetes (Não = 0, Sim = 1)
        fam (int): se o paciente tem historico familiar de infarto (Não = 0, Sim = 1)
        smok (int): se o paciente é fumante (Não = 0, Sim = 1) 
        obes (int): se o paciente é obeso (Não = 0, Sim = 1)
        alco (int): se o paciente faz uso de alcool (Não = 0, Sim = 1)
        exer (float): horas de exercicio por semana
        diet (int): tipo de dieta do paciente (não saudável = -1, neutra = 0, saudável = 1)
        prev (int): histórico de problema cardíaco (Não = 0, Sim = 1)
        medi (int): se o apciente faz uso de algum medicamento contínuo (Não = 0, Sim = 1)
        stress (int): nível de stress (de 0 a 10)
        seden (float): horas de sedentarismo por semana
        income (float): salário anual em dolar (dividir valor por 1000)
        bmi (float): índice de massa corporal (peso em kg/(altura em m)^2)
        trigly (int): nivel de triglicerídio
        activity (int): numero de dias com atividade física na semana
        sleep (int): horas de sono em um dia
        
    Returns:
        dict: representação do paciente e diagnóstico associado
    """
    
    # Carregando modelo
    ml_path = 'ml_model/modelo_treinado.pkl'
    modelo = Model.carrega_modelo(ml_path)
    
    paciente = Paciente(
        name=form.name.strip(),
        age=form.age,
        sex=form.sex,
        chol=form.chol,
        blup=form.blup,
        bllow=form.bllow,
        rate=form.rate,
        dia=form.dia,
        fam=form.fam,
        smok=form.smok,
        obes=form.obes,
        alco=form.alco,
        exer=form.exer,
        diet=form.diet,
        prev=form.prev,
        medi=form.medi,
        stress=form.stress,
        seden=form.seden,
        income=form.income,
        bmi=form.bmi,
        trigly=form.trigly,
        activity=form.activity,
        sleep=form.sleep,
        outcome=Model.preditor(modelo, form)
    )
    logger.debug(f"Adicionando produto de nome: '{paciente.name}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se paciente já existe na base
        if session.query(Paciente).filter(Paciente.name == form.name).first():
            error_msg = "Paciente já existente na base :/"
            logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando paciente
        session.add(paciente)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado paciente de nome: '{paciente.name}'")
        return apresenta_paciente(paciente), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
        return {"message": error_msg}, 400
    

# Métodos baseados em nome
# Rota de busca de paciente por nome
@app.get('/paciente', tags=[paciente_tag],
         responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_paciente(query: PacienteBuscaSchema):    
    """Faz a busca por um paciente cadastrado na base a partir do nome

    Args:
        nome (str): nome do paciente
        
    Returns:
        dict: representação do paciente e diagnóstico associado
    """
    
    paciente_nome = query.name
    logger.debug(f"Coletando dados sobre produto #{paciente_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    paciente = session.query(Paciente).filter(Paciente.name == paciente_nome).first()
    
    if not paciente:
        # se o paciente não foi encontrado
        error_msg = f"Paciente {paciente_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{paciente_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Paciente econtrado: '{paciente.name}'")
        # retorna a representação do paciente
        return apresenta_paciente(paciente), 200
   
    
# Rota de remoção de paciente por nome
@app.delete('/paciente', tags=[paciente_tag],
            responses={"200": PacienteViewSchema, "404": ErrorSchema})
def delete_paciente(query: PacienteBuscaSchema):
    """Remove um paciente cadastrado na base a partir do nome

    Args:
        nome (str): nome do paciente
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    paciente_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre paciente #{paciente_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando paciente
    paciente = session.query(Paciente).filter(Paciente.name == paciente_nome).first()
    
    if not paciente:
        error_msg = "Paciente não encontrado na base :/"
        logger.warning(f"Erro ao deletar paciente '{paciente_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(paciente)
        session.commit()
        logger.debug(f"Deletado paciente #{paciente_nome}")
        return {"message": f"Paciente {paciente_nome} removido com sucesso!"}, 200