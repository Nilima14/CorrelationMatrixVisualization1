import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load the dataset
    df = pd.read_csv("correlation.csv")

    # Keep only numeric columns for correlation
    numeric_df = df.select_dtypes(include=["number"])

    if numeric_df.empty:
        raise ValueError("No numeric columns found in correlation.csv for correlation matrix.")

    # Compute correlation matrix
    corr = numeric_df.corr()

    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", cbar=True)

    # Save the plot
    plt.title("Correlation Matrix Heatmap")
    plt.savefig("correlation_matrix.png", dpi=300, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    main()
