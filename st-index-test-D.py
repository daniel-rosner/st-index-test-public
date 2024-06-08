import streamlit as st

page_title = 'st Index Test D'
title = 'Streamlit Site Index Test D'
header = 'Streamlit Site Index Test D'
description = 'Testing to determine what may prevent a Streamlit app from being indexed by the main search sites.'
test_A_desc = 'Test A has a private Github repo and begins as a public Streamlit app'
test_B_desc = 'Test B has a private Github repo, begins as a private Streamlit app and converts to a public app'
test_C_desc = 'Test C has a public Github repo and begins as a public Streamlit app'
test_D_desc = 'Test D has a private Github repo, begins as a private Streamlit app and converts to a public app'

st.set_page_config(page_title=page_title)
st.title(title)
st.header(header)
st.text(test_A_desc)
st.text(test_B_desc)
st.text(test_C_desc)
st.text(test_D_desc)