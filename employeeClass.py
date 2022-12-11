from dataclasses import dataclass, asdict


@dataclass
class Employee:
    name: str
    password: str
    office: str

    def as_dict(self):
        return asdict(self)
