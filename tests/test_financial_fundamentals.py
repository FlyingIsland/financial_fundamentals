import pandas as pd
from financial_fundamentals import accounting_metrics
date_range = pd.date_range('2018-12-1', '2018-12-31')
ticker = ["AMZN", "TSLA", "MSFT", "GOOG", "F", "ORCL", "AAPL", "WFC", "TOL", "BA", "NKE"]

required_data = pd.DataFrame(columns=ticker, index=date_range)
print accounting_metrics.earnings_per_share(required_data)
