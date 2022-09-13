import pandas as pd
import numpy as np
import os 
from pathlib import Path
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

# df = pd.read_excel(r'C:\Users\jwood\OneDrive\Desktop\Work Folder\Work Folder\Project_2\data\Trend_Full_Data_data (1).xlsx')
filepath1 = os.path.join(Path(__file__).parents[1], 'data\Trend_Full_Data_data (1).xlsx')

def run_app():
    

    pht = df[['Complete Date', 'Tech ID', 'PHT Result', 'Region', 'System']]
    wa_pht = pht[pht['Region'] == 'SEATTLE REGION']
    spokane_pht = wa_pht[wa_pht['System'] == "SPOKANE, WA"]
    sea_pht = wa_pht[wa_pht['System'] != "SPOKANE, WA"]


    test = sea_pht['PHT Result'].value_counts().sort_index()

    return test