import os
import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, create_engine
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    mail = Column(String(100), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    contraseña = Column(String(100), nullable=False)

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    color = Column(String(100), nullable=False) 
    tamaño = Column(Integer, nullable=False)

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    color = Column(String(100), nullable=False)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    usuarioId = Column(Integer, ForeignKey('usuario.id'), nullable=True)
    planetasId = Column(Integer, ForeignKey('planetas.id'), nullable=True)
    personajesId = Column(Integer, ForeignKey('personajes.id'), nullable=True)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
