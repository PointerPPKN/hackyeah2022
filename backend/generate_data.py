import random
from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class Geopoint:
    pk: int
    tag_type: str
    cord_x: float
    cord_y: float


class TypePlace(Enum):
    EME = "establishment of municipal economy"
    PCP = "point of selective collection of municipal waste"
    RM = "recycling machines"
    SP = "scrap purchase"


def generate_data(n: int) -> list:
    list_of_geopoints: list = []
    for i in range(n):
       cord_x: float = random.uniform(15.0, 23.0)
       cord_y: float = random.uniform(51.0, 54.0)
       tag_type: str = random.choice(list(TypePlace)).value
       new_geopoint: Geopoint = Geopoint(pk=i+1, tag_type=tag_type, cord_x=cord_x, cord_y=cord_y)
       list_of_geopoints.append(new_geopoint)
    return list_of_geopoints



