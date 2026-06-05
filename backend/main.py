from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow GitHub Pages to call your API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for testing; later restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
def hello():
    return {"message": "Hello Vinoth!!!!! Welcome to first web hosting!!!!"}
