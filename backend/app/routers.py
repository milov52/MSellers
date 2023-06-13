from fastapi import APIRouter

from backend.app.user.router import router as user_router


main_router = APIRouter()

# main_router.include_router(
#     donations_router, prefix='/donation', tags=['Donations']
# )
# main_router.include_router(
#     charity_project_router, prefix='/charity_project', tags=['Charity projects']
# )

main_router.include_router(user_router)