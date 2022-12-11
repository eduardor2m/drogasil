from dataclasses import dataclass, asdict


@dataclass
class Client:
    name: str
    phone: str
    email: str

    def as_dict(self):
        return asdict(self)
