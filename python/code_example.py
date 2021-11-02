import os, uuid0
import pandas as pd
import numpy as np

print('Hello, World!')
print(f'My name is {os.environ.get("NAME")}')
print(f'Here\'s a UUID: {(uuid0.generate())}')
print(f'''This Vessel is named "{os.environ.get("SHIPYARD_VESSEL_NAME")}" \
and has an ID of {os.environ.get("SHIPYARD_VESSEL_ID")}''')

df = pd.DataFrame(np.random.randint(1,100,size=(100000,4)),columns=list('ABCD'))
df.to_csv('output.csv')
print(f'File output.csv successfully created.')
print(df)
