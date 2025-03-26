import pyarrow.parquet as pq
import pandas as pd
import os

DATA_DIR = "HybridMalwareDetector/data/processed"
OUTPUT_CSV = "HybridMalwareDetector/data/sampled_dataset.csv.gz"  # Compressed CSV

FEATURE_COLUMNS = [
    "label", "general", "header", "section", "imports", "exports"
]  # Keeping only necessary fields

MALWARE_COUNT = 1000  
SAFE_COUNT = 1000  

def sample_parquet_files():
    malware_samples = []
    safe_samples = []

    for file in os.listdir(DATA_DIR):
        if file.endswith(".parquet"):
            file_path = os.path.join(DATA_DIR, file)
            print(f"Processing: {file}")

            parquet_file = pq.ParquetFile(file_path)

            for batch in parquet_file.iter_batches(batch_size=5000):  # Read in chunks
                df = batch.to_pandas()
                df = df[FEATURE_COLUMNS]  # Drop huge fields

                malware_samples.append(df[df["label"] == 1])  # Malware
                safe_samples.append(df[df["label"] == 0])  # Safe files

                if sum(len(x) for x in malware_samples) >= MALWARE_COUNT and \
                   sum(len(x) for x in safe_samples) >= SAFE_COUNT:
                    break  # Stop once we have enough samples

    # Combine & sample
    malware_df = pd.concat(malware_samples).sample(n=MALWARE_COUNT, random_state=42)
    safe_df = pd.concat(safe_samples).sample(n=SAFE_COUNT, random_state=42)
    final_df = pd.concat([malware_df, safe_df]).sample(frac=1).reset_index(drop=True)  # Shuffle

    # Save compressed
    final_df.to_csv(OUTPUT_CSV, index=False, compression="gzip")
    print(f"Sampled dataset saved at: {OUTPUT_CSV} (Compressed)")

sample_parquet_files()
