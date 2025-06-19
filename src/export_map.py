import pandas as pd
from keplergl_cli import Visualize

def main():
    
    df = pd.read_csv('../data/commute_data.csv')
    vis = Visualize(data=df)
    vis.render('../dist/map.html', open_browser=False, read_only=False)

if __name__ == '__main__':
    main()