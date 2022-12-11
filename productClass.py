from dataclasses import dataclass, asdict


@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def as_dict(self):
        return asdict(self)
