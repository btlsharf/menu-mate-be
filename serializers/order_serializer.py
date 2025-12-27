from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

class OrderItemBase(BaseModel):
    menu_item_id: int
    quantity: int
    price_at_order: Decimal

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: int
    order_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    order_type: str
    notes: Optional[str] = None

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]
    total_price: Decimal

class Order(OrderBase):
    id: int
    user_id: int
    status: str
    total_price: Decimal
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class OrderWithItems(Order):
    order_items: List[OrderItem]

    class Config:
        from_attributes = True

class OrderStatusUpdate(BaseModel):
    status: str
