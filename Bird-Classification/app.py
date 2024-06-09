from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pipeline import ONNXPipeline
import io
from PIL import Image


app =FastAPI()
onnx_pipeline = ONNXPipeline("./model/model.onnx")


@app.post("/predict")
async def get_prediction(file: UploadFile = File(...)):
    print("file is : ", file)
    if file.filename == '':
        raise HTTPException(status_code=400, detail="No selected file")
    
    try:
        image = Image.open(io.BytesIO(await file.read()))
        result = onnx_pipeline.predict(image)
        return  JSONResponse(content={"prediction":result})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return "<h1> hello world! </h1>"
