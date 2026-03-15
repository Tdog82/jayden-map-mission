import streamlit as st
import folium
from streamlit_folium import st_folium

# Mission-Zentrale für Jayden
st.set_page_config(page_title="Agent Jayden: Map-Mission", layout="centered")
st.title("🕵️ MISSION: BUNDESLAND-DETEKTIV")

# Punkte-System (XP)
if 'xp' not in st.session_state:
    st.session_state.xp = 0

# Status-Anzeige an der Seite
st.sidebar.markdown(f"### 🎖️ AGENT: JAYDEN\n### 🌟 XP: {st.session_state.xp}")

# Die interaktive Karte vorbereiten
st.subheader("📍 Zielsektor scannen")
m = folium.Map(location=[51.1657, 10.4515], zoom_start=6)

# Wir setzen einen Marker für die erste Mission: Bayern
folium.Marker(
    [48.1351, 11.5820], 
    popup="Welches Bundesland und welche Hauptstadt?", 
    tooltip="Hier klicken für Info"
).add_to(m)

# Karte in der App anzeigen
st_folium(m, width=700, height=450)

# Abfrage-Bereich für Jayden
st.info("Agent Jayden, erkenne den markierten Sektor im Süden!")

land = st.selectbox("Wähle das Bundesland:", ["...", "Bayern", "Baden-Württemberg", "Hessen"])
stadt = st.text_input("Wie heißt die Landeshauptstadt?")

if st.button("Sektor-Daten übermitteln"):
    if land == "Bayern" and stadt.strip().lower() == "münchen":
        st.balloons()
        st.success("🎯 Volltreffer! Sektor gesichert. +50 XP")
        st.session_state.xp += 50
    else:
        st.error("❌ Falsche Daten! Überprüfe die Map erneut.")
      
