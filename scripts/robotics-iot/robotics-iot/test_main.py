import main
from unittest.mock import patch, mock_open

def test_log_temperature_and_humidity():
    with patch("main.Adafruit_DHT.read", return_value=(30.0, 20.0)):
        with patch("builtins.open", mock_open()) as mock_file:
            main.log_temperature_and_humidity()

        mock_file.assert_called_once_with('sensor_data.log', 'a')
        mock_file().write.assert_called_once_with("Temp=20.0*  Humidity=30.0%\n")