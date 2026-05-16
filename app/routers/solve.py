from fastapi import APIRouter, HTTPException

from app.schemas import Solve2x2Request, Solve3x3Request, SolveResponse
from app.services import solve_cube, state_to_dict

router = APIRouter(prefix="/solve", tags=["solve"])


@router.post("/3x3", response_model=SolveResponse)
def solve_3x3(request: Solve3x3Request):
    try:
        state = state_to_dict(request.state)
        solution, time_taken = solve_cube(state, "3x3", request.algorithm)
        return SolveResponse(solution=solution, time_taken=time_taken)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/2x2", response_model=SolveResponse)
def solve_2x2(request: Solve2x2Request):
    try:
        state = state_to_dict(request.state)
        solution, time_taken = solve_cube(state, "2x2", request.algorithm)
        return SolveResponse(solution=solution, time_taken=time_taken)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
