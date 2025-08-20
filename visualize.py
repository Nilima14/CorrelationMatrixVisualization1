import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load the dataset
    df = pd.read_csv("correlation.csv")

    # Compute the correlation matrix
    corr = df.corr()

    # Set up the matplotlib figure
    plt.figure(figsize=(10, 8))

    # Generate a heatmap with annotations
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", cbar=True)

    # Add title
    plt.title("Correlation Matrix Heatmap", fontsize=16)

    # Save the heatmap to a file
    plt.savefig("correlation_matrix.png", dpi=300, bbox_inches="tight")

    # Show the plot (optional)
    # plt.show()

if __name__ == "__main__":
    main()
