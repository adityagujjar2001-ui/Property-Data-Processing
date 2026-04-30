import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "data")
RAW_FILE = os.path.join(DATA_PATH, "raw.csv")
CLEAN_FILE = os.path.join(DATA_PATH, "clean.csv")