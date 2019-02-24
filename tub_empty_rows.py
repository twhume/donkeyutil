import argparse
from donkeycar.parts.datastore import Tub
import numpy as np
import pandas as pd

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Plot a Donkey Car tub")
    parser.add_argument("tub_in", help="tub directory to read from")

    args = parser.parse_args()
    inputs = ["cam/image_array", "user/angle", "user/throttle", "user/mode", "timestamp"]
    types = ["image_array", "float", "float", "str", "str"]
    tub = Tub(path=args.tub_in, inputs=inputs, types=types)
    tub.get_df()
    print(np.where(pd.isnull(tub.df)))