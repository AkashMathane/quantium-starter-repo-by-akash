import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load processed data
df = pd.read_csv("pink_morsels_sales.csv")

# Convert date column to datetime and sort
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    title="Pink Morsels Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Sales ($)",
        "region": "Region"
    }
)

# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div(
    children=[
        html.H1(
            "Pink Morsels Sales Visualiser",
            style={"textAlign": "center"}
        ),
        dcc.Graph(figure=fig)
    ]
)

# Run app
if __name__ == "__main__":
    app.run(debug=True)

