import os
import pandas as pd
import numpy as np
import uuid
import ast

print('Hello, World!')
print(f'My name is {os.environ.get("NAME")}')
print(f'Here\'s a UUID: {uuid.uuid4()}')
print(f'''This Vessel is named "{os.environ.get("SHIPYARD_VESSEL_NAME")}" \
and has an ID of {os.environ.get("SHIPYARD_VESSEL_ID")}''')

min_int = int(os.environ.get('MIN_INT',1))
max_int = int(os.environ.get('MAX_INT',100))
num_rows = int(os.environ.get('NUM_ROWS',100))
column_names = ast.literal_eval(os.environ.get('COLUMN_NAMES',"['A','B','C','D']"))
num_columns = len(column_names)
file_name = os.environ.get('FILE_NAME','output.csv')

df = pd.DataFrame(np.random.randint(min_int,max_int,size=(num_rows,num_columns)),columns=column_names)
df.to_csv(file_name,index=False)
print(f'File successfully created at {file_name}')
print(df)
