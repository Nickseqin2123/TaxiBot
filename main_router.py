from aiogram import Router
from TarifPlan.tar import router as tar_router
from HelpUser.help import router as help_router
from UserOperation.taxi_ordering import router as ordering_router


router = Router(name=__name__)

router.include_routers(
    tar_router,
    help_router,
    ordering_router
)