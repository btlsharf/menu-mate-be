from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import Base, engine
from controllers import users, category_controller, menu_item_controller, order_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MenuMate API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(category_controller.router)
app.include_router(menu_item_controller.router)
app.include_router(order_controller.router)

@app.get("/")
def read_root():
    return {"message": "MenuMate API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
