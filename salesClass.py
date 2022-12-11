from dataclasses import dataclass, asdict


@dataclass
class Sale:
    client: str
    employee: str
    product: str
    quantity: int

    def as_dict(self):
        return asdict(self)
