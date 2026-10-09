# AQI Checker

Python CLI that shows the current air quality index (AQI) for your location and gives outdoor safety advice. Built for gig workers, such as delivery riders, who spend all day outside.

## Setup

1. Get a free API token at https://aqicn.org/data-platform/token/
2. Install the dependency: `pip install requests`
3. Create a file named `config.py` next to `aqi.py` with one line: `TOKEN = "your_token_here"`

## Run

`python aqi.py`

## Example output

```
The AQI for here: 185
Air quality is unhealthy, wear a mask and have a break indoors.
```

## Data source

World Air Quality Index Project (aqicn.org)
