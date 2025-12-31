import pandas as pd
print(pd.__version__)
data = [100,200,300,400]
series = pd.Series(data, index = [a*2 for a in range(len(data))])
print(series)