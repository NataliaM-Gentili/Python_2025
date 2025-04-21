import streamlit as st

st.title("Mujeres destacas en el ámbito Cantantes")

st.divider()
with st.expander('Apartado sobre Mujeres destacas en el ámbito de Cantantes - Argentina'):
    st.markdown("""Las voces femeninas argentinas han marcado generaciones, cada una con su propio estilo, 
    pero con la misma pasión indomable. Mercedes Sosa nos enseñó que cantar es también resistir, que la 
    música puede abrazar a los pueblos. Gilda convirtió la cumbia en esperanza, y Mariana Bianchini rompió 
    moldes con su arte experimental y valiente. Estas mujeres no solo cantaron: transformaron, inspiraron,
    sanaron. Demostraron que la voz de una mujer, cuando nace del alma, puede cambiar el mundo. """)


st.divider()
with st.expander('Opinión personal - Gentili Natalia María'):
    st.markdown("""Tita Merello es de las mejores artistas que escuché en mi vida, junto con (aunque no de procedencia argentina), Amy Winehouse""")


#separamos los elementos del diccionario, borrando la clave 'Cantante' que ya no es necesaria
femaleSinger = ['Mariana Bianchini', 'Gilda','Mercedes Sosa','Tita Merello ♡' ,'Lali Espósito']

Data = {'Mariana Bianchini': "Rock alternativo, experimental. Cantante, compositora y artista visual. Conocida por su originalidad y versatilidad, fue parte de la banda Panza y también tiene una sólida carrera solista. ",
        'Gilda': "Música tropical. Se convirtió en un ícono popular por sus letras sentidas y su carisma. Su vida se truncó en un accidente en 1996, pero su figura sigue viva como símbolo de fe y esperanza.",
        'Mercedes Sosa': "Folklore argentino y latinoamericano. 'La Voz de América Latina', fue una figura fundamental del Nuevo Cancionero. Su canto fue resistencia, identidad y puente entre culturas.",
        'Tita Merello ♡': "Tango y música popular. Artista multifacética, pionera del tango cantado por mujeres. Fue una de las primeras cantantes de tango surgidas en la década de 1920 que crearon la modalidad vocal femenina en el rubro.​También fue actriz y símbolo de la cultura popular argentina.",
        'Lali Espósito': "Pop, urbano, dance. Cantante, actriz y performer de proyección internacional. Con una carrera sólida y en constante crecimiento, es referente de empoderamiento femenino en la música actual."}
        
 # Mostrar el selectbox con las mujeres en la lista
selected_women = st.selectbox('Selecciona una Mujer', femaleSinger)
selected_women_data = Data[selected_women]

if selected_women:
            st.write(f'Has seleccionado: {selected_women}')
            st.write(f'Es reconocida en el género {selected_women_data}')