import pandas as pd


def load_data():
    """
    Load IMDb dataset.
    """

    df = pd.read_csv("data/IMDB Dataset.csv")

    return df


if __name__ == "__main__":
    df = load_data()

    print(df.head())
    print("\nDataset Shape:")
    print(df.shape)