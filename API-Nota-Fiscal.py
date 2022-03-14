from fastapi import FastAPI
from pathlib import Path
from typing import Optional
from pydantic import BaseModel

empresa = [
    {
    'id': 1,
    'nome_empresa': 'Rod_Raff',
    'cnpj': 14797440000126
    },
    {
    'id': 2,
    'nome_empresa': 'Máximo',
    'cnpj': 14803029000116
    }
]

nota_fiscal = [
    {
    'id': 1,
    'nome_empresa': 'Rod_Raff',
    'série': 'SG8R44',
    'número': 545257,
    'nome': 'Salgadinho_Lays_98g',
    'peso': '1.68Kg',
    'cubagem': 300,
    'data': '10/03/2022'
    },
    {
    'id': 2,
    'nome_empresa': 'Rod_Raff',
    'série': 'WV64D8',
    'número': 46635,
    'nome': 'Café Pilão tradicional 500g',
    'peso': '6Kg',
    'cubagem': 300,
    'data': '10/03/2022'
    },
    {
    'id': 3,
    'nome_empresa': 'Máximo',
    'série': 'SDI548',
    'número': 811628,
    'nome': 'Salgadinho_Lays_98g',
    'peso': '1.68Kg',
    'cubagem': 300,
    'data': '10/03/2022'
    },
    {
    'id': 4,
    'nome_empresa': 'Máximo',
    'série': 'D5SE2D',
    'número': 843821,
    'nome': 'Café_Pilão_tradicional_500g',
    'peso': '6Kg',
    'cubagem': 300,
    'data': '10/03/2022'
    }
]
app = FastAPI()

@app.get('/get-empresa/{nome_empresa}')
def get_empresa(
    nome_empresa: str):

    search = list(filter(lambda x: x['nome_empresa'] == nome_empresa, empresa))
    searchNF = list(filter(lambda x: x['nome_empresa'] == nome_empresa, nota_fiscal))

    if search == []:
        return {'Erro': 'O item não existe'}

    if searchNF == []:
        return {'Erro': 'O item não existe'}

    return {'Empresa': search,
            'Notas fiscais registradas': searchNF}