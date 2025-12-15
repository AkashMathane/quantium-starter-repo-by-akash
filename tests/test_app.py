import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def app():
    # Import the Dash app from app.py
    return import_app("app")


def test_header_present(dash_duo, app):
    dash_duo.start_server(app)

    # Check that the header text exists
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsels Sales Visualiser"


def test_graph_present(dash_duo, app):
    dash_duo.start_server(app)

    # Check that a graph component exists
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None


def test_region_picker_present(dash_duo, app):
    dash_duo.start_server(app)

    # Check that the radio button container exists
    radio_items = dash_duo.find_element("#region-selector")
    assert radio_items is not None
