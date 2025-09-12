from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schema import ProductCreate, ProductResponse, ProductUpdate
from typing import List
from crud import (
    create_product,
    get_product,
    get_products,
    delete_product,
    update_product
)

router = APIRouter()

# rota de buscar todos os items

@router.get('/products/', response_model=List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    products = get_products(db)
    return products

# rota de buscar 1 item

@router.get('/products/{product_id}', response_model=ProductResponse)
def read_one_product(product_id:int, db: Session = Depends(get_db)):
    db_product = get_product(db = db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail='Voce procurou um produto que nao existe')
    return db_product

# rota de adicionar item

@router.post('/products/', response_model=ProductResponse)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = create_product(product=product, db=db)
    return db_product

# rota de deletar item

@router.delete('/product/{product_id}', response_model=ProductResponse)
def delete_product_route(product_id:int, db: Session = Depends(get_db)):
    product_db = delete_product(product_id=product_id, db=db)
    if product_db is None:
        raise HTTPException(status_code=404, detail='Voce procurou um produto que nao existe')
    return product_db

# rota de update

@router.put('/product/{product_id}', response_model=ProductResponse)
def atualizar_product(product_id: int, product:ProductUpdate, db: Session = Depends(get_db)):
    product_db = update_product(db=db, product_id=product_id, product=product)
    if product_db is None:
        raise HTTPException(status_code=404, detail='Voce procurou um produto que nao existe')
    return product_db
