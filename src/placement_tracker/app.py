"""Streamlit interface. Run the command documented in docs/SETUP.md."""

import streamlit as st

from placement_tracker import database


def main():
    """Initialise local data and display the supplied sample applications."""
    st.set_page_config(page_title="Placement Application Tracker", layout="wide")
    database.init_db()
    st.title("Placement Application Tracker")
    st.caption("Local workshop project. All supplied records are fictional sample data.")
    st.caption("SUPPLIED STARTER")

    # Activity B2: add an entry form here after prompting foundations.
    st.info("Starter: inspect the code and sample table before adding features.")

    # Activity B4: add an edit form here.

    st.subheader("Applications")
    rows = database.list_applications()
    if rows:
        st.dataframe(rows, hide_index=True)
    else:
        st.info("No applications yet.")
    st.caption(f"Total applications: {len(rows)}")

    # Activity C2: add search, status filters and counts after the core works.


if __name__ == "__main__":
    main()
