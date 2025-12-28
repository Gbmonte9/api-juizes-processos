from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Juiz(Base):
    __tablename__ = "juizes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(200), nullable=False)
    email = Column(String(200), unique=True, index=True, nullable=False)
    senha_hash = Column(String(256), nullable=False)
    processos = relationship("Processo", back_populates="juiz")

class Processo(Base):
    __tablename__ = "processos"
    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String(100), unique=True, index=True, nullable=False)
    parte = Column(String(200))
    status = Column(String(50), default="em andamento")
    descricao = Column(Text)
    pdf_filename = Column(String(200), nullable=True)
    criado_em = Column(DateTime, default=datetime.datetime.utcnow)
    juiz_id = Column(Integer, ForeignKey("juizes.id"))
    juiz = relationship("Juiz", back_populates="processos")
