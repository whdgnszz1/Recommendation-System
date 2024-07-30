# 사용자 u.user 파일을 DataFrame으로 읽기
import os
import pandas as pd

base_src = '../machine_learning_data'
u_user_src = os.path.join(base_src, 'u.user')
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv(u_user_src,
                    sep='|',
                    names=u_cols,
                    encoding='latin-1')
users = users.set_index('user_id')
print(users.head())