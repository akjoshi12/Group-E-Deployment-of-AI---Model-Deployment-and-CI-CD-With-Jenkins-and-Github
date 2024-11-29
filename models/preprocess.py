import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    data = df[['review_text', 'review_rating']].dropna()
    data['label'] = data['review_rating'].apply(lambda x: 'positive' if x >= 4 else 'negative' if x <= 2 else 'neutral')
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
    train_data.to_csv('train_data.csv', index=False)
    test_data.to_csv('test_data.csv', index=False)
    print("Preprocessing complete.")

if __name__ == "__main__":
    preprocess_data("../dataset/amazon_uk_shoes_products_dataset_2021_12.csv")
