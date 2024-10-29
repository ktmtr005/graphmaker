import streamlit as st
import pandas as pd

st.title('Graph Maker')

st.subheader('Input')
input_file = st.file_uploader('Upload a CSV or TSV file')
separator = st.radio('Separator', ['Comma', 'Tab', 'Space'])
comment = st.text_area('Comment Line')

st.subheader('Graph settings')
xlabel = st.text_area('X label')
ylabel = st.text_area('Y label')

def read_data(input_file, separator, comment):
    sep = ','
    if separator == 'Comma':
        sep = ','
    elif separator == 'Tab':
        sep = '\t'
    elif separator == 'Space':
        sep = '\s+'
    
    if len(comment) == 0:
        comment = None
    
    data = pd.read_csv(input_file, sep=sep, comment=comment, header=None, index_col=0)
    return data

def make_line_chart(data, xlabel, ylabel):
    st.line_chart(data=data, x_label=xlabel, y_label=ylabel)

if st.button('Make graph'):
    if input_file != None:
        data = read_data(input_file=input_file, separator=separator, comment=comment)
        st.subheader('Graph')
        make_line_chart(data=data, xlabel=xlabel, ylabel=ylabel)
        st.subheader('Raw Data')
        st.write(data)
    else:
        st.write('No file uploaded')