import pandas as pd
import seaborn as sns
import numpy as np
nobel = pd.read_csv('Examining Netflix Movies/nobel.csv')
nobel['sex'].value_counts()
# Display the number of prizes won by the top 10 nationalities.
nobel['birth_country'].value_counts().head(n=10)
nobel['usa_born_winner'] = nobel['birth_country']=="United States of America"
nobel['decade'] = np.floor(nobel['year']).astype(np.int64)
prop_usa_winners = nobel.groupby('decade',as_index=False)['usa_born_winner'].mean()
sns.set()
# and setting the size of all plots.
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [11, 7]

# Plotting USA born winners 
ax = sns.lineplot(x='decade',y='usa_born_winner',data=prop_usa_winners)

# Adding %-formatting to the y-axis
from matplotlib.ticker import PercentFormatter
# ... YOUR CODE FOR TASK 4 ...
ax.yaxis.set_major_formatter(PercentFormatter())
# Calculating the proportion of female laureates per decade
nobel['female_winner'] = nobel['sex']=='Female'
prop_female_winners = nobel.groupby(['decade','category'],as_index=False)['female_winner'].mean()

# Plotting USA born winners with % winners on the y-axis
# ... YOUR CODE FOR TASK 5 ...
sns.set()
# and setting the size of all plots.
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [11, 7]
ax = sns.lineplot(x='decade',y='female_winner',data=prop_female_winners,hue='category')
(nobel[nobel['female_winner']==True]).sort_values(by='female_winner').head(1)
nobel.groupby("full_name").filter(lambda x: len(x)>= 2)
# Converting birth_date from String to datetime
nobel['birth_date'] = pd.to_datetime(nobel['birth_date'])

# Calculating the age of Nobel Prize winners
nobel['age'] = nobel['year']-nobel['birth_date'].dt.year

# Plotting the age of Nobel Prize winners
sns.lmplot(x='year',y='age',data=nobel)
# The oldest winner of a Nobel Prize as of 2016
nobel.nlargest(1,columns='age')
# The youngest winner of a Nobel Prize as of 2016
nobel.nsmallest(1,columns='age')