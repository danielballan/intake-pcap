import sys

import pandas as pd

from intake_pcap.stream import OfflineStream


if __name__ == '__main__':
    pd.set_option('display.max_columns', 10)
    pd.set_option('display.width', 1000)

    ostream = OfflineStream(sys.argv[1])
    if len(sys.argv) > 2:
        ostream.set_filter(sys.argv[2])
    print(ostream.to_dataframe())
