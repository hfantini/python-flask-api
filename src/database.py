from pymysql import NULL
from sqlalchemy_utils.functions import database_exists, create_database
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()

class Database:

    engine = NULL
    session = NULL

    @staticmethod
    def init_database(uri):

        if not database_exists(uri):
            create_database(uri)

        Database.engine = create_engine(uri)

    @staticmethod
    def init_schema():

        Base.metadata.create_all(Database.engine, checkfirst=True);


    @staticmethod
    def init_session():

        Database.session = Session(bind=Database.engine)

class User(Base):

    __tablename__ = 'User'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String(100), nullable=False)
    sobrenome = Column('sobrenome', String(100), nullable=False)
    descricao = Column('descricao', String(150), nullable=False)

    def to_json(self):

        return  {
                    "id": self.id, 
                    "nome": self.nome, 
                    "sobrenome": self.sobrenome,
                    "descricao": self.descricao,
                }
