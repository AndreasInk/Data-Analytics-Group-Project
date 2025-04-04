import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataset import load_voice_dataset

# Method taken from professor's in-class example
# Takes a dataframe and plots it as a boxplot
def show_plot(df):
  #
  plt.rcParams['figure.figsize'] = [14, 6]
  # Create a boxplot to visualize the distribution of the data
  sns.boxplot(data=df, orient='v')
  plt.title("Outlier Distributiion")
  plt.ylabel("Range")
  plt.xlabel("Attributes")
  plt.tight_layout()
  plt.show()

df = load_voice_dataset()
show_plot(df)