import pandas as pd
import matplotlib.pyplot as plt

# Load the correlation matrix
df = pd.read_csv("correlation.csv", index_col=0)

# Plot the heatmap
plt.figure(figsize=(8, 6))
plt.imshow(df, cmap="coolwarm", interpolation="nearest")
plt.colorbar(label="Correlation")
plt.xticks(range(len(df.columns)), df.columns, rotation=45, ha="right")
plt.yticks(range(len(df.index)), df.index)
plt.title("Correlation Matrix Heatmap")
plt.tight_layout()

# Save the figure
plt.savefig("correlation_matrix.png")
plt.show()
