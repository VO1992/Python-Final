
import pandas as pd
 
# intialise data of lists.
data = {'Symptom':['Sensory', 'Motor', 'Visual','Fatigue','Balance','Sexual Dys','Urinary','Pain','Cognitive'],
        'Percentage':[40, 39, 30, 30,24,20,17,15,10]}

data2 = {'Injected':['Copaxon','Extavia','Glatopa'],
		'Oral Medication':['Tecfidera','Gilenya','Aubagio'],
		'IV Infusion':['Tysabri','Ocrevus','Lemtrada']}

  
# Create DataFrame
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

# Print the output.

print(df1)
print()
print(df2)
print()
print('If you want to learn more about MS:https://www.nationalmssociety.org/What-is-MS')








