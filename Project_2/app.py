import streamlit as st
import pandas as pd
import numpy as np
from src import pht


st.title('Seattle PHT Metrics')
r,s,t = pht.run_app()
st.write(f'PHT fails {r}')
st.write(f'PHT Pass {s}')
st.write(f'PHT Pass w/ Warnings {t}')

try:
    r,s,t = pht.run_app()
    st.write(f'PHT fails {r}')
    st.write(f'PHT Pass {s}')
    st.write(f'PHT Pass with Warnings {t}')
