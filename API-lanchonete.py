from fastapi import FastAPI
from pathlib import Path
from typing import Optional
from pydantic import BaseModel

menu = [
    {
    'id': 1,
    'nome': 'café',
    'preço':  2.5
    },
    {
    'id': 2,
    'nome': 'bolo',
    'preço': 10
    },
    {
    'id': 3,
    'nome': 'chá',
    'preço': 3.2
    },
    {
    'id': 4,
    'nome': 'croissant',
    'preço': 5.8
    }
]
app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None


@app.get('/get-item/{item_id}')
def get_item(
        item_id: int = Path(

            description="Fill with ID of the item you want to view")):
        search = list(filter(lambda x: x['id'] == item_id, menu))

        if search == []:
            return {'Error': 'Item does not exist'}

        return {'Item': search[0]}


@app.get('/list-menu')
def list_menu():
    return {'Menu': menu}


@app.post('/create-item/{item_id}')
def create_item(item_id: int, item: Item):
    search = list(filter(lambda x: x['id'] == item_id, menu))
    if search != []:
        return {'Error': 'Item exists'}
    item = item.dict()
    item['id'] = item_id
    menu.append(item)
    return item


@app.put('/update-item/{item_id}')
def update_item(item_id: int, item: UpdateItem):
    search = list(filter(lambda  x: x['id'] == item_id, menu))
    if search == []:
        return {'Item': "Does not exist"}

    if item.name is not None:
        search[0]['name'] = item.name

    if item.price is not None:
        search[0]['price'] = item.price

    return search


@app.delete('/delete-item/{item_id}')
def delete_item(item_id: int):
    search = list(filter(lambda x: x['id'] == item_id, menu))

    if search == []:
        return {'Item': 'Does not exist'}

    for i in range(len(menu)):
        if menu[i]['id'] == item_id:
            del menu[i]
            break
    return {'Message': 'Item deleted successfully'}