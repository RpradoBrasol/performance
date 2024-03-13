from pydantic import BaseModel, PositiveFloat, PositiveInt
from datetime import datetime, time, date

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

    # @validator("Date", pre=True)
    # def parse_date(cls, value):
    #     return datetime.strptime(
    #         value,
    #         "%Y-%m-%d"

    #     ).date()

    Time: time

    # @validator("Time", pre=True)
    # def parse_time(cls, value):
    #     return datetime.strptime(
    #         value,
    #         "%H:%m"

    #     ).time()

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
