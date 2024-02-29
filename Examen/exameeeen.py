import json
import requests
import pandas as pd
import numpy as np
import os

path_base = "C:/Users/oscar.torresrodrigue/Downloads/"
os.path.join(path_base,"location.json")
df = pd.read_json(f"{path_base}location.json")
df