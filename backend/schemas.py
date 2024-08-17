from pydantic import BaseModel, PositiveFloat, EmailStr, Field, model_validator
from enum import Enum
from datetime import datetime
from typing import Optional


class CategoriaBase(Enum):
    categoria1 = "Eletrônico"
    categoria2 = "Eletrodoméstico"
    categoria3 = "Móveis"
    categoria4 = "Roupas"
    categoria5 = "Calçados"


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

    # @model_validator(mode="before")
    # def check_categoria(cls, values):
    #     categoria = values.get('categoria')
    #     if categoria is not None and categoria not in [item.value for item in CategoriaBase]:
    #         raise ValueError("Categoria inválida")
    #     return values


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    categoria: Optional[str] = None
    email_fornecedor: Optional[EmailStr] = None

    # @model_validator(mode="before")
    # def check_categoria(cls, values):
    #     categoria = values.get('categoria')
    #     if categoria is not None and categoria not in [item.value for item in CategoriaBase]:
    #         raise ValueError("Categoria inválida")
    #     return values