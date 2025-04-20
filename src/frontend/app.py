# app.py
import streamlit as st
import os

# Access secrets
db_url = st.secrets["postgresql://neondb_owner:npg_ziW1uVZR4jhL@ep-dry-flower-a5cttzfr-pooler.us-east-2.aws.neon.tech/anime_migrate?sslmode=require"]
mal_id = st.secrets["	7d40aab44a745bbefc83c9df14413f86"]

def main():
  st.title("Anime List Migrator")
  col1, col2 = st.columns(2)
    with col1:
        source_platform = st.selectbox("Source Platform", ["MyAnimeList", "AniList"])
        source_user = st.text_input(f"{source_platform} Username")

    with col2:
        target_platform = st.selectbox("Target Platform", ["AniList", "MyAnimeList"])
        target_user = st.text_input(f"{target_platform} Username")

    if st.button("Compare Lists"):
        with st.spinner("Fetching data..."):
            source_data = fetch_from_source(source_platform, source_user)
            target_data = fetch_from_target(target_platform, target_user)

            delta = compare_data(source_data, target_data)
            show_comparison(delta)

def show_comparison(delta):
    st.subheader("Migration Plan")
    for item in delta:
        cols = st.columns([1,3,1])
        cols[0].write(f"**{item['action']}**")
        cols[1].write(f"{item['title']} ({item['episodes']} eps)")
        cols[2].button("Migrate", key=item['external_id'])
    
