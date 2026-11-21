"""Placement Application Tracker. Run with: uv run --locked streamlit run app.py"""

import streamlit as st

import db

st.set_page_config(page_title="Placement Application Tracker", layout="wide")
db.init_db()
st.title("Placement Application Tracker")
st.caption("Local workshop project. All supplied records are fictional sample data.")
if "flash" in st.session_state:
    st.success(st.session_state.pop("flash"))

st.caption("SUPPLIED STARTER")

# Activity B2: add an entry form here after prompting foundations.
st.info("Starter: inspect the code and sample table before adding features.")

# Activity B3: add an edit form here.

st.subheader("Applications")
rows = db.list_applications()
if rows:
    st.dataframe(rows, hide_index=True)
else:
    st.info("No applications yet.")
st.caption(f"Total applications: {len(rows)}")

# Activity C2: add search, status filters and counts after the core works.
