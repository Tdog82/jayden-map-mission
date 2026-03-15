import streamlit as st
import folium
from streamlit_folium import st_folium

# Mission-Zentrale Setup
st.set_page_config(page_title="Agent Jayden: Bundesländer-Check", layout="centered")
st.title("🕵️ MISSION: DEUTSCHLAND-SCANNER")

# Speicher für Fortschritt
if 'runde' not in st.session_state:
    st.session_state.runde = 0
if 'xp' not in st.session_state:
    st.session_state.xp = 0

# Alle 16 Bundesländer
missionen = [
    {"land": "Bayern", "stadt": "München", "coords": [48.1351, 11.5820], "optionen": ["München", "Stuttgart", "Nürnberg"]},
    {"land": "Berlin", "stadt": "Berlin", "coords": [52.5200, 13.4050], "optionen": ["Berlin", "Potsdam", "Magdeburg"]},
    {"land": "Baden-Württemberg", "stadt": "Stuttgart", "coords": [48.7758, 9.1829], "optionen": ["Stuttgart", "Karlsruhe", "Mannheim"]},
    {"land": "Brandenburg", "stadt": "Potsdam", "coords": [52.3906, 13.0645], "optionen": ["Potsdam", "Cottbus", "Berlin"]},
    {"land": "Bremen", "stadt": "Bremen", "coords": [53.0793, 8.8017], "optionen": ["Bremen", "Bremerhaven", "Oldenburg"]},
    {"land": "Hamburg", "stadt": "Hamburg", "coords": [53.5511, 9.9937], "optionen": ["Hamburg", "Lübeck", "Bremen"]},
    {"land": "Hessen", "stadt": "Wiesbaden", "coords": [50.0782, 8.2398], "optionen": ["Wiesbaden", "Frankfurt", "Kassel"]},
    {"land": "Mecklenburg-Vorpommern", "stadt": "Schwerin", "coords": [53.6333, 11.4167], "optionen": ["Schwerin", "Rostock", "Wismar"]},
    {"land": "Niedersachsen", "stadt": "Hannover", "coords": [52.3759, 9.7320], "optionen": ["Hannover", "Braunschweig", "Osnabrück"]},
    {"land": "Nordrhein-Westfalen", "stadt": "Düsseldorf", "coords": [51.2277, 6.7735], "optionen": ["Düsseldorf", "Köln", "Dortmund"]},
    {"land": "Rheinland-Pfalz", "stadt": "Mainz", "coords": [49.9929, 8.2473], "optionen": ["Mainz", "Koblenz", "Trier"]},
    {"land": "Saarland", "stadt": "Saarbrücken", "coords": [49.2333, 7.0000], "optionen": ["Saarbrücken", "Homburg", "Saarlouis"]},
    {"land": "Sachsen", "stadt": "Dresden", "coords": [51.0504, 13.7373], "optionen": ["Dresden", "Leipzig", "Chemnitz"]},
    {"land": "Sachsen-Anhalt", "stadt": "Magdeburg", "coords": [52.1333, 11.6167], "optionen": ["Magde
                                                                                                
