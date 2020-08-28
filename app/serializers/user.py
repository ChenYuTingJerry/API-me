from dataclasses import dataclass


@dataclass
class BlockUserSerializer:
    id: int
    name: str
    gender: bool
    age: int
    v_level: int = 0
