from pydantic import BaseModel, Field, model_validator


class FibTaskPost(BaseModel):
    stop_value: int = Field(
        default=7_000_000,
        description="Максимальное значение элемента последовательности",
        gt=4,
        le=7_000_000
    )
    prev_value: int = Field(
        default=3,
        description="Первый элемент последовательности",
        gt=0,
        lt=7_000_000
    )
    next_value: int = Field(
        default=4,
        description="Второй элемент последовательности",
        gt=0,
        lt=7_000_000
    )

    @model_validator(mode='after')
    def validate_prev_value(self):
        if self.prev_value >= self.next_value:
            raise ValueError("prev_value не может быть больше чем next_value")
        if self.next_value >= self.stop_value:
            raise ValueError("next_value не может быть больше чем stop_value")
        return self


class FibTaskResponse(BaseModel):
    result: int


class UpperTaskPost(BaseModel):
    text: str


class UpperTaskResponse(UpperTaskPost):
    pass
