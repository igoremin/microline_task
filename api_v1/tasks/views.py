from fastapi import APIRouter

from .schemas import (
    FibTaskPost, FibTaskResponse, UpperTaskPost, UpperTaskResponse
)
from .utils import (
    fib_sum, upper_text
)

router = APIRouter(tags=["Tasks"])


@router.post(
    "/fib_sum",
    responses={
        200: {"model": FibTaskResponse}
    },
    summary="Сумма четных числел в последовательности фибоначи",
)
async def fib_sum_view(data: FibTaskPost) -> FibTaskResponse:
    result = await fib_sum(**data.model_dump())
    return FibTaskResponse(result=result)


@router.post(
    "/upper_text",
    responses={
        200: {"model": UpperTaskResponse}
    },
    summary="Перевод текста в верхний регистр",
)
async def upper_text_view(data: UpperTaskPost) -> UpperTaskResponse:
    result = await upper_text(**data.model_dump())
    return UpperTaskResponse(text=result)
