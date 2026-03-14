import pandas as pd
from utils.feature_extraction import extract_url_features
import os

def process_large_dataset():
    raw_data_path = 'data/raw_urls.csv'
    processed_data_path = 'data/phishing_url.csv'
    
    if not os.path.exists(raw_data_path):
        print(f"Error: Could not find {raw_data_path}. Please download the dataset and place it in the data/ folder.")
        return

    print("Loading raw dataset (this might take a moment for large files)...")
    # We'll read just a subset (e.g., 50,000 rows) so it doesn't crash your computer on the first try
    df_raw = pd.read_csv(raw_data_path).sample(n=50000, random_state=42) 

    # Kaggle data usually uses 'good' and 'bad'. Let's convert that to 0 and 1.
    print("Normalizing labels...")
    if df_raw['Label'].dtype == object:
        df_raw['Label'] = df_raw['Label'].map({'good': 0, 'bad': 1})
    
    print("Extracting features from URLs (this will take a few minutes)...")
    
    # Create empty lists to store our extracted features
    url_lengths, has_ips, has_ats, dot_counts, has_hyphens = [], [], [], [], []
    
    # Iterate through the URLs and extract features
    for index, row in df_raw.iterrows():
        url = str(row['URL'])
        # Our function returns a nested list [[len, ip, at, dot, hyphen]], so we grab the first element [0]
        features = extract_url_features(url)[0] 
        
        url_lengths.append(features[0])
        has_ips.append(features[1])
        has_ats.append(features[2])
        dot_counts.append(features[3])
        has_hyphens.append(features[4])
        
    # Build the final processed DataFrame
    print("Building final dataset...")
    df_processed = pd.DataFrame({
        'url_length': url_lengths,
        'has_ip': has_ips,
        'has_at_symbol': has_ats,
        'dot_count': dot_counts,
        'has_hyphen_domain': has_hyphens,
        'label': df_raw['Label']
    })
    
    # Drop any rows where features couldn't be extracted properly
    df_processed.dropna(inplace=True)
    
    # Save the ready-to-use data
    df_processed.to_csv(processed_data_path, index=False)
    print(f"Success! Processed dataset saved to {processed_data_path} with {len(df_processed)} rows.")

if __name__ == "__main__":
    process_large_dataset()