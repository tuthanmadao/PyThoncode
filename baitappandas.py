"""
        __Bài tập về nhà__
    Ý số 2 của bài trên
    1. khai báo function với def
    2. khai báo function lambda
    3. cách bí mật cực kì đơn giản :))
"""
import numpy as np
import pandas as pd
import math


def log_pandas():
    return np.log


area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area': area, 'pop': pop})
print(data)
print(data.applymap(np.log))
print(data.applymap(log_pandas()))  # Dùng function với def
print(data.applymap(lambda x: np.log(x)))  # Dùng với làm lambda
print(np.log(data))
