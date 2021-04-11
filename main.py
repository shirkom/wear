import uvicorn
from fastapi import FastAPI, Request
import what_should_wear_file

app = FastAPI(title='What should wear today?')


@app.get("/ip")
def read_root(request: Request):
    client_host = request.client.host
    return {"client_ip": client_host}


@app.get("/wear/{lat}/{lon}")
def wear(lat: str, lon: str):
    temp_celsuis, weather_description, wear_res = what_should_wear_file.what_should_wear(lat, lon)
    return {
        'lat': lat,
        'lon': lon,
        'temp_celsuis': temp_celsuis,
        "weather description": weather_description,
        "appropriate_clothe": wear_res
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
