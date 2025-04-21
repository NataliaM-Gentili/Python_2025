import streamlit as st

st.title("Mujeres destacas en el ámbito de Ciencia")

st.divider()
with st.expander('Apartado sobre Mujeres destacas en el ámbito de Ciencia - Argentina'):
    st.markdown("""En la «historia oficial» de la ciencia siempre predominaron los logros de los hombres, invisibilizando la participación y el sacrificio de las mujeres. 
                Necesitamos compartir las experiencias profesionales y personales de las investigadoras científicas argentinas, así como los obstáculos y prejuicios que tuvieron y tienen que sortear solo por ser mujeres.
                 - Educ.ar""")


#separamos los elementos del diccionario, borrando la clave 'Ciencia' que ya no es necesaria
Cswomen = ['Eugenia Sacerdote de Lustig', 'Carolina Vera', 'Emma Perez Ferreira', 'Silvia Braslavky',
                'Emilia Ferreiro', 'Cecilia Grierson', 'Julieta Lanteri']

Data = {'Eugenia Sacerdote de Lustig': "ser una de las primeras médicas en Argentina en trabajar con cultivos celulares. Investigadora pionera en estudios sobre el cáncer, su trabajo fue clave para introducir la vacunación contra la poliomielitis en el país.",
        'Carolina Vera': "haberse especializado en ciencias de la atmósfera y cambio climático. Ha contribuido de forma significativa al estudio del clima en América del Sur y fue parte del Panel Intergubernamental de Cambio Climático (IPCC).",
        'Emma Perez Ferreira': "haber sido bioquímica e investigadora destacada en nutrición infantil y salud pública. Tuvo un rol clave en el desarrollo de políticas de nutrición para niños en situación de vulnerabilidad.",
        'Silvia Braslavky': "haber sido doctora en química, reconocida internacionalmente por sus estudios en fotoquímica y fotobiología. Fue directora del Instituto Max Planck de Química Biofísica y presidenta de la Sociedad Internacional de Fotobiología.",
        'Emilia Ferreiro': "haber sido psicóloga y pedagoga argentina, discípula de Jean Piaget. Revolucionó la manera de entender cómo los niños aprenden a leer y escribir, desarrollando la teoría de los procesos de alfabetización.",
        'Cecilia Grierson': "ser la primera médica argentina, pionera en la educación médica femenina. Fundó la primera escuela de enfermería del país. También fue activista por los derechos de las mujeres en salud y educación.",
        'Julieta Lanteri': "farmacéutica, médica y precursora en el movimiento feminista. Julieta Lanteri fue la primera mujer incorporada al padrón nacional y la primera en votar en la Argentina y América Latina. Fundadora del Partido Feminista Nacional, fue un estandarte en la lucha por la reivindicación de los derechos de la mujer. Fue la primera mujer que pudo ingresar y recibirse de bachiller en el Colegio Nacional de La Plata"}
        
        
        
 # Mostrar el selectbox con las mujeres en la lista
selected_women = st.selectbox('Selecciona una Mujer', Cswomen)
selected_women_data = Data[selected_women]

if selected_women:
            st.write(f'Has seleccionado: {selected_women}')
            st.write(f'Es reconocida por {selected_women_data}')