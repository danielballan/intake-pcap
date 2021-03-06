import sys

import pandas as pd

from intake_pcap.stream import LiveStream


if __name__ == '__main__':
    pd.set_option('display.max_columns', 10)
    pd.set_option('display.width', 1000)

    lstream = LiveStream(sys.argv[1])
    if len(sys.argv) > 2:
        lstream.set_filter(sys.argv[2])
    while True:
        print(lstream.to_dataframe(n=10))
