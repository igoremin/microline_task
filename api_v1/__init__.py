from fastapi import APIRouter

from .tasks.views import router as task_router

router = APIRouter()
router.include_router(router=task_router, prefix="/tasks")
