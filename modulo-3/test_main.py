from main import get_temperature
from unittest.mock import patch


@patch("main.requests.get")
def test_get_temperature_by_lat_lng(mock_get):
    context = [
        {
            "latitude": -14.235004,
            "longitude": -51.92528,
            "currently": {"temperature": 62},
        },
        {
            "latitude": -9.973870,
            "longitude": -67.807541,
            "currently": {"temperature": 87.8},
        },
        {
            "latitude": -23.550520,
            "longitude": -46.633308,
            "currently": {"temperature": 71.6},
        },
        {
            "latitude": 51.500149,
            "longitude": -0.126240,
            "currently": {"temperature": 68},
        },
        {
            "latitude": 35.689487,
            "longitude": 139.691711,
            "currently": {"temperature": 77},
        },
    ]

    values = [16, 31, 21, 20, 25]

    for location, expected_temperature in zip(context, values):
        mock_get.return_value.json.return_value = location
        result = get_temperature(location["latitude"], location["longitude"])
        assert result == expected_temperature
