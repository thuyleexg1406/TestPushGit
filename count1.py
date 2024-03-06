import numpy as np
import pandas as pd
from tqdm import tqdm
from matplotlib import pyplot as plt
import os

classes = {}
dataset_dir = "train_npy/PET/autoPET"
for _, sub_dirs, files in os.walk(dataset_dir):
    for file in files:
        if file.endswith(".npy"):
            if _.split('/')[-1] == 'imgs':
                continue
            file_path = os.path.join(_, file)
            data = np.load(file_path)

            cls = np.unique(data)
            for i in range(len(cls)):
                classes.setdefault(int(cls[i]), 0)  # Convert class labels to integers
                classes[int(cls[i])] += 1

print(classes)
# Save to CSV
sub_dirs = str(dataset_dir.split('/')[-1])
pd.DataFrame(list(classes.items()), columns=['Class', 'Count']).to_csv(f'count_class_{sub_dirs}.csv', index=False)