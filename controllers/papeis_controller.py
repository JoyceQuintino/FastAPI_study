from fastapi import APIRouter

from models.papel import Papel


router = APIRouter()

database = []

@router.post('/')
def add_item(item: Papel):
    database.append(item)
    return item

@router.get('/')
def get_item():
    return database
