
import streamlit as st
import importlib

TAB_REGISTRY = {
    "Zip Ingestor": "streamlit_tab_zip_ingestor",
    "Auto-Deploy Manager": "streamlit_tab_autodeploy_manager",
    "Assistant Registry": "streamlit_tab_assistant_registry"
}

def main():
    st.set_page_config(page_title="Ecosystem OS", layout="wide")

    st.sidebar.title("🧭 Navigation")
    tab_choice = st.sidebar.radio("Select Tab", list(TAB_REGISTRY.keys()))

    tab_module = TAB_REGISTRY[tab_choice]
    try:
        mod = importlib.import_module(tab_module)
        mod.render()
    except Exception as e:
        st.error(f"Failed to load tab: {tab_module}")
        st.exception(e)

if __name__ == "__main__":
    main()
