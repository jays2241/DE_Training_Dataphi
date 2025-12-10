from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("untitled.csv")

# Replace NaN with None so JSON can handle it
df = df.where(pd.notnull(df), None)

@app.get("/data")
def get_all_data():
    return df.to_dict(orient="records")
