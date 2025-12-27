from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = ""
    price: Decimal
    category_id: Optional[int] = None
    is_available: bool = True
    image_url: Optional[str] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItem(MenuItemBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
