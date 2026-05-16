from app.schemas.cube import Cube2x2State, Cube3x3State

FACES = ("U", "D", "L", "R", "F", "B")


def state_to_dict(state: Cube3x3State | Cube2x2State) -> dict[str, list[list[str]]]:
    return {
        face: [list(row) for row in getattr(state, face).model_dump().values()]
        for face in FACES
    }
