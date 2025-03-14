import pandas as pd
import matplotlib.pyplot as math


data = pd.read_csv('survey_results_public.csv', usecols=['ConvertedCompYearly', 'Industry']) # Load the relevant columns


remove = data[(data['ConvertedCompYearly'] != 'N/A')  & (data['Industry'] != 'N/A')] 

remove['ConvertedCompYearly'] = pd.to_numeric(remove['ConvertedCompYearly'], errors='coerce')

remove = remove.dropna() #drop rows with missing values

# The .dropna() method drops the missing values it cannot drop N/A values only numeric values

# Gets average salaries per industry --------
salary = remove.groupby ('Industry') ['ConvertedCompYearly'].mean().sort_values(ascending=False) 
# Gets average salaries per industry -------- 


# Select top 10 industries
industries = salary.head(15)

# Plot horizontal bar graph
math.figure(figsize=(11, 7))
industries.sort_values().plot.barh()

math.title('Top 10 Industries') # Title
math.xlabel('Average Annual Salary') # The label for x-axis horizontal
math.ylabel('Industry Type') # the label for y-axis vertical

math.tight_layout()
math.show()