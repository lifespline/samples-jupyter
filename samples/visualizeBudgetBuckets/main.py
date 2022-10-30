import constants
from logic.clean import bank_28112019_30052021
import pandas as pd

def analyse():
    bank_28112019_30052021.compute()

def visualize(graph=None, how='dataset'):
    if how == 'dataset':
        df = pd.read_parquet(constants.data['clean']['bank']['28112019_30052021'], engine='pyarrow')

        print(df)
