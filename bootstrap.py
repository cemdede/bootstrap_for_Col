import os
import glob
import pandas as pd
import numpy as np

# Set your source and destination folders
source_folder = '/home/input/'
dest_folder = '/home/output/'

# Keep track of the synthetic MRNs to ensure uniqueness
synthetic_mrns = set()

# Initialize MRN folder counter
mrn_folder_counter = 0

# Initialize total MRNs required
total_mrn_required = 10000

# Loop through each patient MRN folder
for patient_mrn in os.listdir(source_folder):
    # Stop if the required MRN folders are generated
    if mrn_folder_counter >= total_mrn_required:
        break

    # Get the list of CSV files for this patient
    csv_files = glob.glob(os.path.join(source_folder, patient_mrn, 'RD.*.csv'))

    # Skip if no CSV files are found
    if not csv_files:
        print(f'No CSV files found for {patient_mrn}')
        continue

    # Loop to generate multiple synthetic MRNs from each original MRN
    while mrn_folder_counter < total_mrn_required:
        # Generate a unique synthetic MRN
        while True:
            new_mrn = np.random.randint(10000000, 99999999)
            if new_mrn not in synthetic_mrns:
                synthetic_mrns.add(new_mrn)
                break

        # Create a new folder for the synthetic patient data
        new_folder = os.path.join(dest_folder, str(new_mrn))
        os.makedirs(new_folder, exist_ok=True)

        # Increment the MRN folder counter
        mrn_folder_counter += 1

        # Loop through each CSV file for bootstrapping
        for csv_file in csv_files:
            try:
                # Read the CSV file
                csv_data = pd.read_csv(csv_file, on_bad_lines='skip')

                # Perform bootstrapping
                csv_syn = csv_data.sample(len(csv_data), replace=True)

                # Save the synthetic CSV file
                csv_name = os.path.basename(csv_file).replace('.csv', '_synthetic.csv')
                csv_syn.to_csv(os.path.join(new_folder, csv_name), index=False)

            except Exception as e:
                # Log any errors
                print(f"Error while processing {csv_file}: {e}")

# Bootstrap process is complete
print(f'Bootstrap complete! Total MRN folders generated: {mrn_folder_counter}')
