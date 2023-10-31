from typing import Annotated
from fastapi import FastAPI, File, UploadFile
import numpy as np
app = FastAPI()
@app.get("/Hello")
async def hello():
    return "Welcome Fast API learning"



@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


# def read_file_as_image() -> np.ndarray():