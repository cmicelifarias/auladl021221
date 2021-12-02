import streamlit as st
import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris 

st.write("""
Predicao do dataset do Iris

""")

st.sidebar.header("Vamos colocar coisas aqui")

def usuario():
    sepal_length = st.sidebar.slider("Tamanho do sepal", 4,6,8) 
    sepal_width = st.sidebar.slider("Largura do sepal", 4,6,8)
    petal_length = st.sidebar.slider("Tamando da petala", 1,4,8)
    petal_width = st.sidebar.slider("Largura da Petala", 1,4,8)
    data = {"sepal_length":sepal_length,
            "sepal_width":sepal_width,
            "petal_length":petal_length,
            "petal_width":petal_width
    }
    features = pd.DataFrame(data,index=[0])
    return features

df = usuario()

st.subheader("Input do usuario")
st.write(df)

iris = load_iris()
X = iris.data
Y = iris.target

cls = LogisticRegression()
cls.fit(X,Y)

predicao = cls.predict(df)

st.subheader("Predicao")
st.write(iris.target_names[predicao])