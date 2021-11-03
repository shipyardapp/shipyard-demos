import os
import pandas as pd
import numpy as np
import uuid
import ast
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--name',
        dest='name',
        default='Jane Doe',
        required=True,
        )
    parser.add_argument(
        '--min-int',
        dest='min_int',
        default='1',
        required=True,
        )
    parser.add_argument(
        '--max-int',
        dest='max_int',
        default='100',
        required=True,
        )
    parser.add_argument(
        '--num-rows',
        dest='num_rows',
        default='100',
        required=True,
        )
    parser.add_argument(
        '--column-names',
        dest='column_names',
        default='["A","B","C","D"]',
        required=True,
        )
    parser.add_argument(
        '--file-name',
        dest='file_name',
        default='output.csv',
        required=True,
        )
    
    args = parser.parse_args()
    
    return args

args = get_args()
name = args.name

print('Hello, World!')
print(f'My name is {os.environ.get("NAME")}')
print(f'Here\'s a UUID: {uuid.uuid4()}')
print(f'''This Vessel is named "{os.environ.get("SHIPYARD_VESSEL_NAME")}" \
and has an ID of {os.environ.get("SHIPYARD_VESSEL_ID")}''')

min_int = int(args.min_int)
max_int = int(args.max_int)
num_rows = int(args.num_rows)
column_names = ast.literal_eval(args.column_names)
num_columns = len(column_names)
file_name = args.file_name

df = pd.DataFrame(np.random.randint(min_int,max_int,size=(num_rows,num_columns)),columns=column_names)
df.to_csv(file_name,index=False)
print(f'File successfully created at {file_name}')
print(df)
