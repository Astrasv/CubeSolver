from pydantic import BaseModel, ConfigDict

from app.schemas.base import Algorithm
from app.schemas.cube import Cube2x2State, Cube3x3State


class Solve3x3Request(BaseModel):
    model_config = ConfigDict(extra="forbid")

    algorithm: Algorithm
    state: Cube3x3State


class Solve2x2Request(BaseModel):
    model_config = ConfigDict(extra="forbid")

    algorithm: Algorithm
    state: Cube2x2State
