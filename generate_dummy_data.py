import pandas as pd
import random

fields = [
    {
        "name": "City",
        "type": "categorical",
        "categories": ["Mumbai", "Pune", "Chennai", "Kolkata", "Bangalore", "Nagpur"],
    },
    {
        "name": "Pincode",
        "type": "categorical",
        "categories": [
            "400074",
            "400065",
            "560095",
            "53000",
            "410038",
            "410054",
            "410067",
        ],
    },
    {"name": "Gender", "type": "categorical", "categories": ["Male", "Female"]},
    {
        "name": "Age Group",
        "type": "categorical",
        "categories": ["20-40", "40-60", "60-80", "80+"],
    },
    {"name": "COVID-19 like symptoms", "type": "categorical", "categories": [0, 1]},
    {"name": "COVID-19 Diagnosed", "type": "categorical", "categories": [0, 1]},
]


NUM_DATAPOINTS = 2000
FILENAME = "cope_dummy_data.csv"

data = []

for i in range(NUM_DATAPOINTS):
    l = []
    for m in fields:
        print(m["name"])
        if m["type"] == "categorical":
            l.append(random.choice(m["categories"]))
        elif m["type"] == "number":
            l.append(random.randint(m["min"], m["max"]))

    data.append(l)

df = pd.DataFrame(data)

df.columns = [x["name"] for x in fields]

df.to_csv(FILENAME, index=False)
