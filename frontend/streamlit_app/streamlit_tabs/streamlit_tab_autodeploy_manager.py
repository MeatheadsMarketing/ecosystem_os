
import streamlit as st

def render():
    st.title("🛠️ Auto-Deploy Manager")
    if st.button("🌀 Run Git Auto-Commit"):
        st.code("Running: auto_git_committer.commit_and_tag()")
    if st.button("🚀 Push to Cloud (GitHub Release)"):
        st.code("Running: push_to_cloud.sh")
    if st.button("📡 Push to Server"):
        st.code("Running: push_to_server.sh")
    if st.button("🧠 Run Assistant Self-Healer"):
        st.code("Running: assistant_self_healer.heal_skipped_files()")
