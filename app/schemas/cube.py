from pydantic import BaseModel, ConfigDict

from app.schemas.base import Color


class Face3x3(BaseModel):
    model_config = ConfigDict(extra="forbid")

    row1: tuple[Color, Color, Color]
    row2: tuple[Color, Color, Color]
    row3: tuple[Color, Color, Color]


class Face2x2(BaseModel):
    model_config = ConfigDict(extra="forbid")

    row1: tuple[Color, Color]
    row2: tuple[Color, Color]


class Cube3x3State(BaseModel):
    model_config = ConfigDict(extra="forbid")

    U: Face3x3
    D: Face3x3
    L: Face3x3
    R: Face3x3
    F: Face3x3
    B: Face3x3


class Cube2x2State(BaseModel):
    model_config = ConfigDict(extra="forbid")

    U: Face2x2
    D: Face2x2
    L: Face2x2
    R: Face2x2
    F: Face2x2
    B: Face2x2
