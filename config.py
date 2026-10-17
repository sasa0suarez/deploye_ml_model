from pathlib import Path

# Automatically find the root directory where config.py lives
ROOT_DIR = Path(__file__).resolve().parent

# Define core project paths
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_PATH = DATA_DIR / "cleaned_data.csv"
MODEL_PATH = ROOT_DIR / "model.pkl"

