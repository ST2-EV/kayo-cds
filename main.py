import json
from datetime import datetime, timedelta

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with a list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # You can replace "*" with a list of allowed HTTP methods
    allow_headers=["*"],  # You can replace "*" with a list of allowed headers
)


@app.get("/initiate/")
async def initiate():
    data = {"initiated": True}
    with open("initiated.json", "w") as f:
        f.write(json.dumps(data))

    current_timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("running.json", "w") as file:
        file.write(json.dumps({"timestamp": current_timestamp_str}))
    return {"message": "Initiate endpoint"}


@app.get("/heartbeat/")
async def heartbeat():
    current_timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("running.json", "w") as file:
        file.write(json.dumps({"timestamp": current_timestamp_str}))
    return {"message": "Heartbeat endpoint"}


@app.get("/finalize/")
async def finalize():
    data = {"initiated": False}
    with open("initiated.json", "w") as f:
        f.write(json.dumps(data))
    with open("running.json", "w") as file:
        file.write(json.dumps({"timestamp": ""}))
    return {"message": "Finalize endpoint"}
