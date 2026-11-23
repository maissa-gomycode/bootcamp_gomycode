
from fastapi import APIRouter
from app.services.course_service import get_course_categories

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.get("/categories")
def course_categories():

    categories = get_course_categories()

    return {
        "categories": categories
    }
