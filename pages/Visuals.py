# This creates the page for displaying data visualizations.

import streamlit as st
import json
import pandas as pd
import altair as alt

# PAGE CONFIGURATION
st.set_page_config(page_title="Visuals")

# PAGE TITLE
st.title("Data Visualizations")

# PART 1: GRAPHS FROM data.json

infile=open("data.json")
data=json.load(infile)
infile.close()
table=pd.DataFrame(data["data_points"])
table.columns=["Contestant", "Score"]
st.subheader(data["chart_title"])
st.dataframe(table)
bars=alt.Chart(table, title="Judges Scores").mark_bar().encode(x="Contestant", y="Score")
st.altair_chart(bars)
st.subheader("Scores Above Minimum")
cutoff=st.slider("Minimum Score", 13, 25, 13,)
small_table=table[table["Score"] >= cutoff]
line=alt.Chart(small_table).mark_line(point=True).encode(x="Contestant",y="Score")
st.altair_chart(line)
