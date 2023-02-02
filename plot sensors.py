## first install requirements using 'pip install -r requirements.txt' in you terminal
# import the necessary packages
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


# read the csv file and put it into a variable
df = pd.read_csv('Occupancy.csv')

# check the shape of the dataset
df.shape

# check the statistical aspect of the dataset
df.describe()


# check if the dataset contains null values, check the columns and datatype
# ## float64 means decimal values with 64 bits of memory
df.info()

# if there is null values we could perform
df_nonull = df.dropna(axis='rows', how='any') # how = 'any' or 'all'. all means drop if all values are na

# let's start with the 'seaborn' package
sb.pairplot(df, hue= 'Occupancy', kind='scatter', diag_kind='hist', height=3)

# matplotlib library
fig, axs = plt.subplots(df.shape[1]-1, 1, figsize = (15, 8), sharex=False) # share x axis for all plots
fig.subplots_adjust(hspace=0.5)
plt.xlabel('Time')

df_date = pd.to_datetime(df['date']).dt.date
for col in range(df.shape[1]):
    axs[col].plot(df_date, df.iloc[:, col+1])
    axs[col].set_ylabel(df.columns[col+1])

# we could plot 2 sensors in 1 plot
fig, axs = plt.subplots(figsize = (30, 8))
plt.plot(df['date'])


# seperate the dataset into y and x. response and explanatory variables
X = df.iloc[:, :-1] # or df[df.columns[:-1]]
y = df.iloc[:, -1:]

X.shape
y.shape