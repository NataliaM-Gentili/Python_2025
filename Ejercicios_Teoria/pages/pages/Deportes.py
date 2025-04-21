import streamlit as st

st.title("Mujeres destacas en el ámbito de Deportes")

st.divider()
with st.expander('Más información sobre Mujeres destacas en el ámbito de Deportes - Argentina'):
    st.markdown("""¿Sabías que hace poco más de 20 años de que las mujeres están oficialmente admitidas
    en los encuentros deportivos internacionales? Recién en 1991 la Federación Internacional de fútbol 
    (FIFA) hizo oficial las competencia femenina, y el Comité de organización de Juegos Olímpicos aceptó
    pruebas femeninas sistemáticas para cada disciplina deportiva. - BuenosAiresConnect \n
    A lo largo de la historia, mujeres argentinas han desafiado los límites del deporte, dejando huellas
    imborrables de talento, esfuerzo y coraje. Ellas nos enseñan que el verdadero triunfo no está solo 
    en las medallas, sino en abrir caminos, inspirar a otros y no rendirse jamás. Su legado vive en cada 
    mujer que hoy se anima a soñar en grande.""")



#separamos los elementos del diccionario, borrando la clave 'Deportes' que ya no es necesaria
SportWomen = ['Gabriela Sabatini','Luciana Aymar','Cecilia Carranza Saroli','Noemí Simoneto','Paula Pareto',
                 'Jeanette Campbell', 'Mary Terán']

Data = {'Gabriela Sabatini': "Tenis. Considerada una de las mejores tenistas argentinas de la historia. Ganó el US Open en 1990 y alcanzó la final de Wimbledon en 1991. Fue top 3 del ranking mundial. ",
        'Luciana Aymar': "Hockey sobre césped. Ícono de 'Las Leonas', fue elegida ocho veces como la mejor jugadora del mundo. Ganó múltiples medallas olímpicas y mundiales.",
        'Cecilia Carranza Saroli': "Vela. Campeona olímpica en Río 2016 en la clase Nacra 17, junto a Santiago Lange. Primera mujer argentina en ganar una medalla de oro olímpica en vela.",
        'Noemí Simoneto': "Atletismo. Ganó la medalla de plata en salto en largo en los Juegos Olímpicos de Londres 1948, siendo la primera mujer argentina en ganar una medalla olímpica.",
        'Paula Pareto': "Judo. Campeona olímpica en Río 2016 y medallista de bronce en Beijing 2008. Primera argentina en ganar una medalla de oro olímpica en judo. También es médica. ",
        'Jeanette Campbell': "Natación. Fue la primera mujer argentina en competir en los Juegos Olímpicos (Berlín 1936) y ganó la medalla de plata en los 100 m libres.",
        'Mary Terán': "Tenis. Pionera del tenis femenino argentino en los años 40 y 50. Fue perseguida por motivos políticos. Su legado fue reivindicado con el estadio de tenis que lleva su nombre."} 
        
        
 # Mostrar el selectbox con las mujeres en la lista
selected_women = st.selectbox('Selecciona una Mujer', SportWomen)
selected_women_data = Data[selected_women]

if selected_women:
            st.write(f'Has seleccionado: {selected_women}')
            st.write(f'Es reconocida en el deporte {selected_women_data}')