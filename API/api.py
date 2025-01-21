from fastapi import FastAPI, File, UploadFile
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import pandas as pd
import joblib

app = FastAPI()

def train(data):
    x_train=data.drop(["Target"],axis=1)
    y_train=data.Target
    rf_model=RandomForestClassifier(n_jobs=-1,random_state=42)
    rf_model.fit(x_train,y_train)
    acc=rf_model.score(x_train,y_train)
    y_pred=rf_model.predict(x_train)
    f1=f1_score(y_train,y_pred)
    dict={"Accuracy":acc,"f1_score":f1}
    joblib.dump(rf_model,"./model/rf_model.pkl")
    return dict

@app.post("/upload")
async def upload_file(file: UploadFile):
    file_location = f"uploaded_files/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())
    return {"info": f"File '{file.filename}' saved at '{file_location}'"}

@app.post("/train")
async def train_model(filename: str):
    file_loc=f"uploaded_files/{filename}"
    df=pd.read_csv(file_loc)
    dict=train(df)
    return dict

@app.post("/predict")
async def predict(data: dict[str,float]):
    df=pd.DataFrame([data])
    rf_model=joblib.load("./model/rf_model.pkl")
    downtime="Yes" if (rf_model.predict(df)==1) else "No"
    confidence=rf_model.predict_proba(df)
    return {"Downtime":downtime,"Confidence":confidence.max()}