import pandas as pd
import financial_fundamentals.edgar as edgar
from financial_fundamentals.accounting_metrics import BookValuePerShare

date_range = pd.date_range('2019-10-18', '2019-10-18')
ticker = ["AMZN", "TSLA", "MSFT", "GOOG", "F", "ORCL", "AAPL", "WFC", "TOL", "BA", "NKE"]
# ticker = ["AMZN"]

required_data = pd.DataFrame(columns=ticker, index=date_range)
for each_symbol in ticker:
	print(each_symbol)
	filings = edgar.get_filings(symbol=each_symbol, filing_type='10-Q')[-1]
	book_value_per_share = BookValuePerShare.value_from_filing(filings)
	print(book_value_per_share)