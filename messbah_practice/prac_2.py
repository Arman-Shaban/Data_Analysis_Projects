import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


df = sns.load_dataset("titanic")

print('Dataset dimensions, rows and columns:')
print(df.shape)

print('First five rows:')
print(df.head())

print('Number of missing values:')
print(df.isnull().sum())

# Handle missing values
df['age'] = df['age'].fillna(df['age'].median())

df_clean = df.drop(columns=['deck'])

print('\nSurvival rate by sex:')
print(df_clean.groupby('sex')['survived'].mean())

print('\nSurvival rate by ticket class:')
print(df_clean.groupby('pclass')['survived'].mean())


print('\nCombined survival rate:')
print(df_clean.pivot_table(
    values='survived',
    index='sex',
    columns='pclass'
))

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.barplot(
    data=df_clean,
    x='pclass',
    y='survived',
    hue='sex',
    ax=axes[0],
    palette='viridis'
)

axes[0].set_title('Survival Rate by Ticket Class and Sex')
axes[0].set_ylabel('Probability of Survival')
axes[0].set_xlabel('Ticket Class')

# Second plot: Age distribution by survival status
sns.histplot(
    data=df_clean,
    x='age',
    hue='survived',
    kde=True,
    bins=30,
    ax=axes[1],
    palette='coolwarm'
)

axes[1].set_title('Age Distribution by Survival Status')
axes[1].set_xlabel('Age')
axes[1].set_ylabel('Number of Passengers')

plt.tight_layout()
plt.show()
