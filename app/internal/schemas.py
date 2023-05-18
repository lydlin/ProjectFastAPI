# Libs imports
from pydantic import BaseModel


class EntrepriseBase(BaseModel):
    nom: str


class EntrepriseCreate(EntrepriseBase):
    pass


class EntrepriseUpdate(EntrepriseBase):
    pass


class Entreprise(EntrepriseBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    nom: str
    prenom: str
    email: str
    mdp: str
    id_entreprise: int
    role: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class PlanningBase(BaseModel):
    nom: str
    id_entreprise: int


class PlanningCreate(PlanningBase):
    pass


class PlanningUpdate(PlanningBase):
    pass


class Planning(PlanningBase):
    id: int

    class Config:
        orm_mode = True


class ActiviteBase(BaseModel):
    nom: str
    lieu: str
    date_debut: str
    date_fin: str
    id_planning: int
    id_createur: int
    nbr_participant: int


class ActiviteCreate(ActiviteBase):
    pass


class ActiviteUpdate(ActiviteBase):
    pass


class Activite(ActiviteBase):
    id: int

    class Config:
        orm_mode = True


class InscriptionBase(BaseModel):
    id_activite: int
    id_user: int


class InscriptionCreate(InscriptionBase):
    pass

class InscriptionUpdate(InscriptionBase):
    pass
class Inscription(InscriptionBase):
    id_Inscription: int

    class Config:
        orm_mode = True
