from flask import json
from sqlalchemy import select
from flask import Blueprint
from flask import request
from factory import api, db
from schemas import WishlistItemCreate, WishlistItemResponse, DefaultResponses, MultWishlistItemResponse, WishlistItemUpdate
from spectree import Response
from models import WishlistItem

WishBlueprint = Blueprint(name = "WishBlueprint", import_name = __name__, url_prefix = "/api")

@WishBlueprint.post("/wishlist")
@api.validate(json = WishlistItemCreate, resp = Response(HTTP_201 = DefaultResponses), tags = ["Wishes"])

def post_wish():
    data = request.json

    wish = WishlistItem(
        name = data["name"],
        description = data.get("description"),
        link = data.get("link"),
        sort_order = data.get("sort_order")
    )

    db.session.add(wish)
    db.session.commit()

    return {"msg" : "Desejo adicionado com sucesso"}, 201

@WishBlueprint.get("/wishlist")
@api.validate(resp = Response(HTTP_200 = MultWishlistItemResponse, HTTP_404 = DefaultResponses), tags = ["Wishes"])

def get_wishes():
    query = db.session.scalars(select(WishlistItem)).all()
    if not query: 
        return {"msg" : "Não existe nenhum desejo em sua lista"}, 404

    else:
        response = MultWishlistItemResponse(
            response = [WishlistItemResponse.model_validate(wish) for wish in query]
        )

    return response, 200

@WishBlueprint.get("/wishlist/<int:wish_id>")
@api.validate(resp = Response(HTTP_200 = WishlistItemResponse, HTTP_404 = DefaultResponses), tags = ["Wishes"])

def get_wish(wish_id):
    query = db.session.scalars(select(WishlistItem).filter_by(id = wish_id)).first()
    if query is None:
        return {"msg" : "Desejo não encontrado"}, 404

    else:
        response = WishlistItemResponse.model_validate(query).model_dump(mode = "json")

    return response, 200

@WishBlueprint.put("/wishlist/<int:wish_id>")
@api.validate(json = WishlistItemUpdate, resp = Response(HTTP_200 = DefaultResponses, HTTP_404 = DefaultResponses), tags = ["Wishes"])

def put_wish(wish_id):
    query = db.session.scalars(select(WishlistItem).filter_by(id = wish_id)).first() 
    if query is None:
        return {"msg" : "Desejo não encontrado"}, 404

    else:
        data = request.json
        query.name = data["name"]
        query.description = data.get("description")
        query.link = data.get("link")
        query.sort_order = data.get("sort_order")
        query.purchased= data.get("purchased")
        
    db.session.commit()
    return {"msg" : "Desejo atualizado com sucesso"}, 200

@WishBlueprint.delete("/wishlist/<int:wish_id>")
@api.validate(resp = Response(HTTP_200 = DefaultResponses, HTTP_404 = DefaultResponses), tags = ["Wishes"])
    
def delete_wish(wish_id):
    query = db.session.scalars(select(WishlistItem).filter_by(id = wish_id)).first() 
    if query is None:
        return {"msg" : "Desejo não encontrado"}, 404

    else:
        db.session.delete(query)

    db.session.commit()

    return {"msg" : "Desejo removido com sucesso"}




