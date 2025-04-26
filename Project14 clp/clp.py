# import pandas as pd
# import numpy as np
# import matplotlib as plt

# df = pd.read_csv(r"C:\Users\hp\Documents\Desktop\Project14 clp\data.csv") 
# df.head(10)
# df.tail(10)
# df.describe()
# df['Property_Area'].value_counts()
# import matplotlib.pyplot as plt
# df['ApplicantIncome'].hist(bins=50)
# plt.show()
# df.boxplot(column='ApplicantIncome')
# plt.show()
# df.boxplot(column='ApplicantIncome', by = 'Education')
# plt.show()
# df['LoanAmount'].hist(bins=50)
# plt.show()
# df.boxplot(column='LoanAmount')
# plt.show()

# temp1 = df['Credit_History'].value_counts(ascending=True)
# temp2 = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x: x.map({'Y':1,'N':0}).mean())
# print('Frequency Table for Credit History:')
# print(temp1)

# print('\nProbility of getting loan for each Credit History class:' )
# print(temp2)


# import matplotlib.pyplot as plt
# fig = plt.figure(figsize=(8,4))
# ax1 = fig.add_subplot(121)
# ax1.set_xlabel('Credit_History')
# ax1.set_ylabel('Count of Applicants')
# ax1.set_title("Applicants by Credit_History")
# temp1.plot(kind='bar')
# plt.show()

# ax2 = fig.add_subplot(122)
# temp2.plot(kind = 'bar')
# ax2.set_xlabel('Credit_History')
# ax2.set_ylabel('Probability of getting loan')
# ax2.set_title("Probability of getting loan by credit history/data.csv") 
# df.head(10)
# df.describe()
# df['Property_Area'].value_counts()


# temp1 = df['Credit_History'].value_counts(ascending=True)
# temp2 = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x: x.map({'Y':1,'N':0}).mean())
# print('Frequency Table for Credit History:')
# print(temp1)

# print('\nProbility of getting loan for each Credit History class:' )
# print(temp2)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r"C:\Users\hp\Documents\Desktop\Project14 clp\data.csv")

# Display data stats
print(df.head(10))
print(df.tail(10))
print(df.describe())
print(df['Property_Area'].value_counts())

# Close any existing plots before continuing
plt.close('all')

# === Income & LoanAmount Histograms and Boxplots ===

# 1. ApplicantIncome histogram & boxplot
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
df['ApplicantIncome'].hist(bins=50)
plt.title('Applicant Income Distribution')
plt.xlabel('Income')

plt.subplot(1, 2, 2)
df.boxplot(column='ApplicantIncome')
plt.title('Boxplot of Applicant Income')

plt.tight_layout()
plt.show()

# 2. ApplicantIncome by Education boxplot
plt.figure(figsize=(6, 4))
df.boxplot(column='ApplicantIncome', by='Education')
plt.title('Income by Education')
plt.suptitle('')  # Removes default suptitle
plt.xlabel('Education')
plt.ylabel('Income')
plt.tight_layout()
plt.show()

# 3. LoanAmount histogram & boxplot
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
df['LoanAmount'].hist(bins=50)
plt.title('Loan Amount Distribution')
plt.xlabel('Loan Amount')

plt.subplot(1, 2, 2)
df.boxplot(column='LoanAmount')
plt.title('Boxplot of Loan Amount')

plt.tight_layout()
plt.show()

# === Credit History Analysis ===

# Frequency and loan approval probability
temp1 = df['Credit_History'].value_counts(ascending=True)
temp2 = df.pivot_table(
    values='Loan_Status',
    index='Credit_History',
    aggfunc=lambda x: x.map({'Y': 1, 'N': 0}).mean()
)

print('Frequency Table for Credit History:')
print(temp1)

print('\nProbability of getting loan for each Credit History class:')
print(temp2)

# Bar plots side-by-side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1 - Applicant count by credit history
temp1.plot(kind='bar', ax=ax1)
ax1.set_xlabel('Credit_History')
ax1.set_ylabel('Count of Applicants')
ax1.set_title('Applicants by Credit History')

# Plot 2 - Loan approval probability by credit history
temp2.plot(kind='bar', ax=ax2)
ax2.set_xlabel('Credit_History')
ax2.set_ylabel('Probability of Getting Loan')
ax2.set_title('Loan Approval Probability')

plt.tight_layout()
plt.show()

