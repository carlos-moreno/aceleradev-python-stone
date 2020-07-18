import os
import time
from datetime import datetime, timedelta

os.environ["TZ"] = "America/Sao_Paulo"
time.tzset()

MINUTE = 1
SECONDS = 60
SIX_HOUR = 6
TWENTY_TWO_HOURS = 22
CALL_RATE = 0.09
PERMANENT_RATE = 0.36
DAY_CALL = "DAY_CALL"
NIGHT_CALL = "NIGHT_CALL"


records = [
    {
        "source": "48-996355555",
        "destination": "48-666666666",
        "end": 1564610974,
        "start": 1564610674,
    },
    {
        "source": "41-885633788",
        "destination": "41-886383097",
        "end": 1564506121,
        "start": 1564504821,
    },
    {
        "source": "48-996383697",
        "destination": "41-886383097",
        "end": 1564630198,
        "start": 1564629838,
    },
    {
        "source": "48-999999999",
        "destination": "41-885633788",
        "end": 1564697158,
        "start": 1564696258,
    },
    {
        "source": "41-833333333",
        "destination": "41-885633788",
        "end": 1564707276,
        "start": 1564704317,
    },
    {
        "source": "41-886383097",
        "destination": "48-996384099",
        "end": 1564505621,
        "start": 1564504821,
    },
    {
        "source": "48-999999999",
        "destination": "48-996383697",
        "end": 1564505721,
        "start": 1564504821,
    },
    {
        "source": "41-885633788",
        "destination": "48-996384099",
        "end": 1564505721,
        "start": 1564504821,
    },
    {
        "source": "48-996355555",
        "destination": "48-996383697",
        "end": 1564505821,
        "start": 1564504821,
    },
    {
        "source": "48-999999999",
        "destination": "41-886383097",
        "end": 1564610750,
        "start": 1564610150,
    },
    {
        "source": "48-996383697",
        "destination": "41-885633788",
        "end": 1564505021,
        "start": 1564504821,
    },
    {
        "source": "48-996383697",
        "destination": "41-885633788",
        "end": 1564627800,
        "start": 1564626000,
    },
]


def is_day_call(start: datetime) -> bool:
    return SIX_HOUR <= start.hour < TWENTY_TWO_HOURS


def call_value(start: datetime, end: datetime) -> float:
    call_duration = end - start
    call_duration = call_duration.seconds // SECONDS
    minutes = 0
    type_call = NIGHT_CALL
    while start <= end and call_duration > 0:
        if is_day_call(start):
            minutes += MINUTE
            type_call = DAY_CALL
        call_duration -= 1
        start += timedelta(minutes=1)
    d = {
        DAY_CALL: minutes * CALL_RATE + PERMANENT_RATE,
        NIGHT_CALL: PERMANENT_RATE,
    }
    return d[type_call]


def generate_dict(records: dict) -> dict:
    d = {}
    for call in records:
        d[call["source"]] = d.get(call["source"], 0) + call_value(
            datetime.fromtimestamp(call["start"]),
            datetime.fromtimestamp(call["end"])
        )
    return d


def classify_by_phone_number(records: dict) -> list:
    d = generate_dict(records)
    result = []
    for call in d.items():
        result.append({"source": call[0], "total": round(call[1], 2)})
    result = sorted(result, key=lambda k: -k["total"])
    return result
