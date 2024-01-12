from fastapi import FastAPI
from tradingview_ta import TA_Handler, Exchange, Interval
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/predict")
async def get_prediction():
    eurusd = TA_Handler(
        symbol='EURUSD',
        screener='forex',
        exchange='FX_IDC',
        interval=Interval.INTERVAL_1_MINUTE
    )
    analysis_summary = eurusd.get_analysis().summary

    return {"prediction": analysis_summary}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
