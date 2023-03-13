from fastapi import APIRouter

from models.papel import Papel


router = APIRouter()

database = []

@router.post('/')
async def add_item(papel: Papel):
    await papel.save()
    return papel

@router.get('/')
async def get_item():
    return await Papel.objects.all()
