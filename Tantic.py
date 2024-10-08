
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Titanic App by Jiachong Wang')

data = pd.read_csv('train.csv')
st.write(data) 

fig, ax = plt.subplots(1, 3, figsize=(15, 5))
plt.style.use('seaborn')

sub_data_1 = data[data['Pclass'] == 1]['Fare']
sub_data_2 = data[data['Pclass'] == 2]['Fare']
sub_data_3 = data[data['Pclass'] == 3]['Fare']

ax[0].boxplot(sub_data_1)
ax[0].set_title('PClass = 1',verticalalignment='bottom')
ax[0].set_xlabel('Fare')
ax[0].set_ylabel('Fare')

ax[1].boxplot(sub_data_2)
ax[1].set_title('PClass = 2',verticalalignment='bottom')
ax[1].set_xlabel('Fare')

ax[2].boxplot(sub_data_3)
ax[2].set_title('PClass = 3',verticalalignment='bottom')
ax[2].set_xlabel('Fare')

st.pyplot(fig)
