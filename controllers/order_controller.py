from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from serializers import Order, OrderCreate, OrderWithItems, OrderStatusUpdate
from models import Order as OrderModel, OrderItem as OrderItemModel, User
from dependencies import get_db, get_current_user

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("", response_model=List[OrderWithItems])
def get_orders(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.role == "admin":
        return db.query(OrderModel).all()
    return db.query(OrderModel).filter(OrderModel.user_id == current_user.id).all()

@router.post("", response_model=Order)
def create_order(
    order: OrderCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_order = OrderModel(
        user_id=current_user.id,
        order_type=order.order_type,
        status="pending",
        total_price=order.total_price,
        notes=order.notes
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    for item in order.items:
        db_order_item = OrderItemModel(
            order_id=db_order.id,
            menu_item_id=item.menu_item_id,
            quantity=item.quantity,
            price_at_order=item.price_at_order
        )
        db.add(db_order_item)

    db.commit()
    db.refresh(db_order)
    return db_order

@router.put("/{order_id}/status", response_model=Order)
def update_order_status(
    order_id: int,
    status_update: OrderStatusUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    db_order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")

    db_order.status = status_update.status
    db.commit()
    db.refresh(db_order)
    return db_order
