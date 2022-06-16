# Sensors Aggregation

## How to run

Create a new virtual environment and activate it

```sh
python -m venv .venv
source .venv/Scripts/activate
```

Install the required dependencies from `requirements.txt`

```sh
pip install -r requirements.txt
```

Run `main.py` with `sensor_data.json` as input

```sh
./main.py sensor_data.json agg_sensor_data.json
```
