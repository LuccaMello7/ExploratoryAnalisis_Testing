DATA_PATH = "https://raw.githubusercontent.com/carlosfab/dsnp2/master/datasets/ocorrencias_aviacao.csv"

#IMPORT RELEVANT PACKAGES
import pandas as pd
#IMPORT CSV FILE

df = pd.read_csv(DATA_PATH, engine = 'python')

#SEE THE FIRST INPUTS
df.head()

##DataFrame Summary
## Using the info() method in a variable you get the summary of all variables (columns) of your dataset. Its types are a valueble information to address to your Variable Dictionary

df.info()

df.ocorrencia_classificacao.unique()

df.ocorrencia_tipo.value_counts()

df.ocorrencia_tipo.value_counts() / df.shape[0] #percentage of relative values

df.index
"""
<h1>loc</h1>

loc`[<lines>, <columns>]`

This method can be used in these two situations:



1.   select **Lines** by **labels /index**
2.   select **Lines** based on a **boolean array**

suppose I need to extract the latitude and longitude of the place where I had the occurrence 201805021421302 or even "in-flight engine failure" (FALHA DO MOTOR EM VOO) event
"""

df["ocorrencia_tipo"] == "FALHA DO MOTOR EM VOO"

# check only the 5 first inputs

df.loc[df["ocorrencia_tipo"] == "FALHA DO MOTOR EM VOO"].head()

"""
<h1>iloc</h1>

The use of iloc is simpler, as one passes selects rows and columns using numbers, in the same order as they appear in the DataFrame:

loc`[<row_number>, <column_number>]`

I can select a range of interest. For example, to select the first 3 inputs and the first 4 columns, I would do it as follows:
"""

df.iloc[0:3, 0:4]