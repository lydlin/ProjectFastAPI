# Libs imports
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
# Local imports
from internal.database import Base


class Entreprise(Base):
    __tablename__ = "entreprise"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    prenom = Column(String, index=True)
    email = Column(String, index=True)
    mdp = Column(String)
    id_entreprise = Column(Integer, ForeignKey("entreprise.id"))
    role = Column(String)

    entreprise = relationship("Entreprise", backref="users")


class Planning(Base):
    __tablename__ = "planning"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    id_entreprise = Column(Integer, ForeignKey("entreprise.id"))

    entreprise = relationship("Entreprise", backref="planning")


class Activite(Base):
    __tablename__ = "activite"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    lieu = Column(String)
    date_debut = Column(String)
    date_fin = Column(String)
    id_planning = Column(Integer, ForeignKey("planning.id"))
    id_createur = Column(Integer, ForeignKey("users.id"))
    nbr_participant = Column(Integer)

    planning = relationship("Planning", backref="activites")
    createur = relationship("User", backref="activites")


class Inscription(Base):
    __tablename__ = "inscription"

    id_Inscription = Column(Integer, primary_key=True, index=True)
    id_activite = Column(Integer, ForeignKey("activite.id"))
    id_user = Column(Integer, ForeignKey("users.id"))

    activite = relationship("Activite", backref="inscriptions")
    user = relationship("User", backref="inscriptions")
