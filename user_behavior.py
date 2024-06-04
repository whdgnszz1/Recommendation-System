import os
import pandas as pd
import numpy as np

base_src = 'machine_learning_data'
behavior_src = os.path.join(base_src, 'behavior.csv')

behavior_df = pd.read_csv(behavior_src, encoding='utf-8')

print(behavior_df[behavior_df['GA_SESSION_ID' == '1715752116']])