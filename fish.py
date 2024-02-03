import pickle
import streamlit as st

model = pickle.load(open('ikan.sav', 'rb'))

st.title('Fish Weight Prediction')

Height = st.number_input('Input Tinggi Ikan')
Width = st.number_input('Input lebar Ikan')
Length1 = st.number_input('Input Panjang Baku Ikan')
Length2 = st.number_input('Input Panjang Cagak Ikan')
Length3 = st.number_input('Input Panjang Ikan Kesuluruhan')

predict = ''

if st.button('Perkiraan Berat Ikan'):
    predict = model.predict(
        [[Height, Width, Length1, Length2, Length3]]
    )
    st.write ('Perkiraan Berat Ikan : ', predict)
