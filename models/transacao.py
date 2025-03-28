# modulos/modelos.py
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Transacao:
    data: datetime
    descricao: str
    valor: float
    categoria: Optional[str] = None

    def e_despesa(self) -> bool:
        return self.valor < 0

    def e_receita(self) -> bool:
        return self.valor > 0

    def valor_absoluto(self) -> float:
        return abs(self.valor)