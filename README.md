# Bootstrap Sampling for Collective Effort
 

Important:
The original data was already anonymized.

For each anonymized MRN folder, CSV files were present in the folder.
CSV Files include CT onRail H&N RX Treatment accumulated dose fraction.

If no CSV files are found for a given MRN, the loop continues to the next MRN.

**Synthetic MRN Generation:**
A nested while-loop is used to generate multiple synthetic MRNs from each original MRN until the total number of required MRNs (total_mrn_required) is reached.

**Bootstrap Sampling:**
For each CSV file under the current MRN, bootstrapping is performed. 
Bootstrapping here means that the code creates a synthetic dataset by sampling with a replacement from the original dataset.

**Saving Synthetic Data**:
The synthetic data is saved as a new CSV file in the corresponding synthetic MRN folder.

The expected amount of patients is **100000**.
