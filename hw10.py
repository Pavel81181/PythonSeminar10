import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
print(lst)
print()
data = pd.DataFrame({'whoAmI':lst})

data.loc[data['whoAmI'] == 'robot', 'robots'] = '1'
data.loc[data['whoAmI'] != 'robot', 'robots'] = '0'
data.loc[data['whoAmI'] == 'human', 'humans'] = '1'
data.loc[data['whoAmI'] != 'human', 'humans'] = '0'

print(data.head(n=20))

# Альтернативное решение

# unique_val = data['whoAmI'].unique()
# one_hot_data = pd.DataFrame()
# for val in unique_val:
#     one_hot_data[val] = (data['whoAmI'] == val).astype(int)
# print(one_hot_data.head(20))
