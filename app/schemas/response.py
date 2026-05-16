from pydantic import BaseModel, ConfigDict


class SolveResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    solution: list[str]
    time_taken: float
