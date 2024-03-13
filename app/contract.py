from pydantic import BaseModel, PositiveFloat, PositiveInt
from datetime import time, date

class Files(BaseModel):
    """
    Modelo de dados para as vendas.

    Args:
        email (str): email do comprador
        data (datetime): data da compra
        valor (int): valor da compra
        produto (str): nome do produto
        quantidade (int): quantidade de produtos
        categoria (str): categoria do produto

    """
    Date: date
    Time: time
    GHI: PositiveInt
    DIF: PositiveInt
    DNI: PositiveInt
    GTI: PositiveInt
    SE: float
    SA: float
    TEMP: PositiveFloat
    WS: PositiveFloat
    WD: PositiveInt
    PVOUT: PositiveFloat
