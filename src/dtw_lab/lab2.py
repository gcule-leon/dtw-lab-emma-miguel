import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
import toml
from dtw_lab.lab1 import (
    read_csv_from_google_drive,
    visualize_data,
    calculate_statistic,
    clean_data,
)
import matplotlib
matplotlib.use("Agg")  # backend sin GUI

import matplotlib.pyplot as plt

# Initialize FastAPI application instance
# This creates our main application object that will handle all routing and middleware
app = FastAPI()

# Server deployment configuration function. We specify on what port we serve, and what IPs we listen to.
def run_server(port: int = 80, reload: bool = False, host: str = "127.0.0.1"):
    uvicorn.run("dtw_lab.lab2:app", port=port, reload=reload, host=host)

# Wrapper functions for script entry points
def run_server_dev():
    """Development server with hot reload on port 8000"""
    run_server(port=8000, reload=True)

def run_server_prod():
    """Production server on all interfaces"""
    run_server(reload=False, host='0.0.0.0')

# Define an entry point to our application.
@app.get("/")
def main_route():
    return {"message": "Hello world"}

@app.get("/statistic/{measure}/{column}")
def get_statistic(measure: str, column: str):

    df = read_csv_from_google_drive('1eKiAZKbWTnrcGs3bqdhINo1E4rBBpglo')
    df = clean_data(df)

    if column not in df.columns:
        return {"error": f"Column {column} not found"}

    result = calculate_statistic(measure, df[column])

    return {
        "measure": measure,
        "column": column,
        "value": result
    }

@app.get("/visualize/{graph_type}")
def get_visualization(graph_type: str):

    df = read_csv_from_google_drive('1eKiAZKbWTnrcGs3bqdhINo1E4rBBpglo')
    df = clean_data(df)

    visualize_data(df)

    file_path = Path("graphs") / f"{graph_type}.png"

    if not file_path.exists():
        return {"error": "Graph not found"}

    return FileResponse(file_path, media_type="image/png")

@app.get("/version")
def get_visualization_version():
    pyproject_path = Path("pyproject.toml")

    if not pyproject_path.exists():
        return {"error": "pyproject.toml not found"}

    data = toml.load(pyproject_path)

    # Adjust depending on structure
    version = data.get("project", {}).get("version", "unknown")

    return {"version": version}