from pydantic import BaseModel
from typing import Optional
from pydantic import ConfigDict

class WishlistItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    link: Optional[str] = None
    sort_order: Optional[int] = None

class WishlistItemUpdate(BaseModel):
    name: str
    description: Optional[str] = None
    link: Optional[str] = None
    sort_order: Optional[int] = None
    purchased: Optional[bool] = None

class WishlistItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    link: Optional[str] = None
    purchased: Optional[bool] = None
    sort_order: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)

class MultWishlistItemResponse(BaseModel):
    response: list[WishlistItemResponse]


