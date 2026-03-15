import streamlit as st
import folium
from streamlit_folium import st_folium

# Mission-Zentrale Setup
st.set_page_config(page_title="Agent Jayden: Bundesländer-Check", layout="centered")
st.title("🕵️ MISSION: DEUTSCHLAND-SCANNER")

# Speicher für Fortschritt (Runde) und XP
if 'runde' not in st.session_state:
    st.session_state.runde = 0
if 'xp' not in st.session_state:
    st.session_state.xp = 0

# Datenbank der Missionen (Bundesländer & Hauptstädte)
# Hier können wir später alle 16 Länder eintragen
missionen = [
    {"land": "Bayern", "stadt": "München", "coords": [48.1351, 11.5820], "optionen": ["Stuttgart", "München", "Nürnberg"]},
    {"land": "Berlin", "stadt": "Berlin", "coords": [52.5200, 13.4050], "optionen": ["Potsdam", "Berlin", "Magdeburg"]},
    {"land": "Schleswig-Holstein", "stadt": "Kiel", "coords": [54.3233, 10.1228], "optionen": ["Kiel", "Hamburg", "Schwerin"]},
    {"land": "Nordrhein-Westfalen", "stadt": "Düsseldorf", "coords": [51.2277, 6.7735], "optionen": ["Köln", "Dortmund", "Düsseldorf"]}
]

# Status-Anzeige in der Seitenleiste
st.sidebar.markdown(f"### 🎖️ AGENT: JAYDEN\n### 🌟 XP: {st.session_state.xp}")
st.sidebar.progress(st.session_state.runde / len(missionen))

# Prüfen, ob noch Missionen offen sind
if st.session_state.runde < len(missionen):
    aktuelle_mission = missionen[st.session_state.runde]
    
    st.subheader(f"📍 Sektor {st.session_state.runde + 1} scannen")
    
    # Die interaktive Karte mit Marker
    m = folium.Map(location=[51.1657, 10.4515], zoom_start=6)
    folium.Marker(
        aktuelle_mission["coords"], 
        popup="Zielsektor",
        icon=folium.Icon(color="red", icon="search")
    ).add_to(m)
    
    st_folium(m, width=700, height=400)

    # Quiz-Bereich
    st.info(f"Identifiziere die Hauptstadt für diesen Sektor!")
    wahl = st.radio("Welche Stadt ist die richtige Landeshauptstadt?", aktuelle_mission["optionen"])

    if st.button("Antwort an Zentrale senden 📡"):
        if wahl == aktuelle_mission["stadt"]:
            st.success("🎯 Volltreffer! +50 XP")
            st.session_state.xp += 50
            st.session_state.runde += 1
            st.rerun()
        else:
            st.error("❌ Alarm! Falsche Koordinaten. Versuche es noch einmal!")
else:
    # Finale Belohnung
    st.balloons()
    st.header("🏆 MISSION ERFÜLLT!")
    st.write(f"Agent Jayden hat alle Sektoren gesichert und {st.session_state.xp} XP gesammelt.")
    if st.button("Neue Mission starten 🔄"):
        st.session_state.runde = 0
        st.session_state.xp = 0
        st.rerun()
        
