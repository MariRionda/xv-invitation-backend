from fastapi import FastAPI
from routers.guests import router as gust_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://xv-invitation-front.vercel.app",
    "https://wedding-invitation-front.vercel.app",
    "https://wedding-invitation-front-2.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(gust_router,prefix="/guest", tags=["Guests"])

@app.get("/")
async def root():
    return {"message": "Hola Mundo"}
