import pandas as pd
from keplergl_cli import Visualize

df: pd.DataFrame = pd.read_csv('../data/commute_data.csv')  # Explicitly annotate type
vis: Visualize = Visualize(data=df)  # Explicitly annotate type
vis.render('../dist/map.html', open_browser=False, read_only=False)
