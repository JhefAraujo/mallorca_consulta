from fastapi import FastAPI, requests
import json
import requests
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


class Item(BaseModel):
    input: int


class Order(BaseModel):
    businessPartner: str


class Botorder(BaseModel):
    id: str


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://127.0.0.1:50136",
    "*"
]


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/client/")
async def create_item(item: Item):
    base = item
    searchKey = base.__getattribute__("input")
    url = (f"https://mallorca8.openbravo.com.br/openbravo/org.openbravo.service.json.jsonrest/"
           f"BusinessPartner?l=botUser&p=1qaz%23EDC5tgb%26UJM&_where=searchKey=" + f"'{searchKey}'" +
           "&_selectedProperties=name&_startRow=0&_endRow=1")
    response = requests.get(url)
    data = response.json()
    jdata = json.dumps(data)
    return jdata


@app.get("/client/")
async def search_item():
    retorno = await create_item()
    print(retorno)
    return retorno


@app.post("/order/")
async def create_order(order: Order):
    baseorder = order
    bpartner =  baseorder.__getattribute__("businessPartner")
    print(bpartner)
    url = (f"https://mallorca8.openbravo.com.br/openbravo/org.openbravo.service.json.jsonrest/"
           f"Order?l=botUser&p=1qaz%23EDC5tgb%26UJM&_startRow=0&_endRow=5&_where=businessPartner="
           f"'{bpartner}'&_selectedProperties=orderDate,documentNo&_orderBy=orderDate desc")
    resposta = requests.get(url)
    dadopedido = resposta.json()
    jadata = json.dumps(dadopedido)
    print(jadata)
    return jadata

@app.get("/order/")
async def search_item():
    retorna = await create_order()
    print(retorna)
    return retorna

@app.post("/botorder/")
async def create_botitem(botorder: Botorder):
    botbase = botorder
    id = botbase.__getattribute__("id")
    url = (f"https://mallorca8.openbravo.com.br/openbravo/org.openbravo.service.json.jsonrest/"
           f"mall_botorders_v?l=botUser&p=1qaz%23EDC5tgb%26UJM&_selectedProperties=rastreio"
           f"&_startRow=0&_endRow=5&_where=documentno='{id}'")
    botresponse = requests.get(url)
    botdata = botresponse.json()
    jbdata = json.dumps(botdata)
    print(jbdata)
    return jbdata


@app.get("/botorder/")
async def search_botitem():
    retornar = await create_botitem()
    print(retornar)
    return retornar
