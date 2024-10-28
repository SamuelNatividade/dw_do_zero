from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random 

app = FastAPI()
fake = Faker()


df = pd.read_csv(r'/Users/samuelnatividade/Desktop/Projetos/criando_um_dw_do_zero/back-end/fake-api/produtos.csv')
df['indice'] = range(1, len(df) + 1)
df.set_index('indice', inplace = True)


@app.get('/gerar_compra/{numero_registro}')
async def gerar_compra(numero_registro: int):
    if numero_registro < 1:
            return {'error: o número deve ser maior que 1'}
    else:
        respostas = []
        for _ in range(numero_registro):
            index = random.randint(1,len(df) - 1)
            tuple = df.iloc[index]
            compra = [{
                    'cliente': fake.name(),
                    'creditcard':fake.credit_card_provider(),
                    'product_name': tuple['Produto'],
                    'ean': tuple['EAN'].astype(str),
                    'price': tuple['Preço'].astype(str),
                    'store': 11,
                    'dateTime': fake.iso8601(),
                    'clientPosition': fake.location_on_land()  
            }]
            respostas.append(compra)

        return respostas