import pandas as pd
import numpy as np

# pandas 字典形式的numpy


s = pd.Series([1, 3, 5, np.nan, 44, 1])
print(s)

dates = pd.date_range('20190308', periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])


