import pandas as pd

def read_txt(*args, **kwargs):
    return pd.read_fwf(*args, **kwargs)
