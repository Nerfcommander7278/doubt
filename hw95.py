import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as cns
import streamlit as st
def load_data():
    df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
    df.head()
    column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race', 'gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
    for i in range(df.shape[1]):
        df.rename(columns={i:column_name[i]},inplace=True)
    df.head()
    df['native-country'] = df['native-country'].replace(' ?',np.nan)
    df['workclass'] = df['workclass'].replace(' ?',np.nan)
    df['occupation'] = df['occupation'].replace(' ?',np.nan)
    df.dropna(inplace=True)
    df.drop(columns='fnlwgt',axis=1,inplace=True)
    return df
adf  =  load_data()
st.write("# Census Data Web App")
st.sidebar.write("""# Interface""")
if st.checkbox("Display Raw Data"):
    st.write("## Raw Data")
    st.dataframe(adf)
    st.write(f"{adf.shape}")
st.sidebar.write("""## Plots""")
st.sidebar.subheader('Select your plot')
ig = "Income Group"
g = "Gender"
hpwig = "Hours Per Week for different income groups"
hpwg = "Hours Per Week for different genders"
cow = "Count of Workclass"
list2 = [ig,g,hpwig,hpwg,cow]
while True:
    d = st.sidebar.multiselect('Which chart do you want select',options=list2)
    break
if d == g:
    plt.figure(figsize=(10,6)) 
    plt.pie(adf['gender'].value_counts() , labels = adf['gender'].unique(), labeldistance = 0.5 )
    plt.show()
    st.pyplot()    