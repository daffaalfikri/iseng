import pickle
import streamlit as st

model = pickle.load(open('Income.sav', 'rb'))

st.title('Estimasi Income')

age = st.number_input('Masukan umur', step=0, max_value=100, min_value=1)
fnlwgt = st.number_input(
    'Masukan Gender,laki laki (Input1),perempuan (Input2)', step=0, max_value=2, min_value=1)
educationalnum = st.number_input(
    'Masukan atypical angina: nyeri dada tidak berhubungan dengan jantung', step=0, max_value=150, min_value=1)
capitalgain = st.number_input('Masukan chest pain type',
                              step=0, max_value=250, min_value=1)
capitalloss = st.number_input('Masukan tekanan darah %',
                              step=0, max_value=260, min_value=1)
hoursperweek = st.number_input('Masukan nomer serum cholestoral dalam mg/dl',
                               step=0, max_value=50, min_value=1)


predict = ''

if st.button(' Estimasi Klasifikasi Income'):
    predict = model.predict(
        [[age, fnlwgt, cp, educationalnum, capitalgain, capitalloss, hoursperweek]]
    )
    st.write('Estimasi Klasifikasi INCOME: ', predict)
    st.write('Estimasi Klasifikasi INCOME: ', predict*2000)
