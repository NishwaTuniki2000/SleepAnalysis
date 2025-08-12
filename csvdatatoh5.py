import pandas as pd
import h5py

def csv_to_h5(csv_file, h5_file):
    # Read data from CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    # Drop rows with missing values
    df.dropna(inplace=True)
    # Open HDF5 file for writing
    with h5py.File(h5_file, 'w') as hf:
        # Convert DataFrame to HDF5 dataset
        hf.create_dataset('data', data=df)

csv_file = r'C:\Users\nishw\Desktop\convert\csv_output_folder\1.csv'
h5_file = 'output.h5'   # Replace with the desired path for the HDF5 file
csv_to_h5(csv_file, h5_file)
