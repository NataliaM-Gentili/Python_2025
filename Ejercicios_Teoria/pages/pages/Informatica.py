import streamlit as st

st.title("Mujeres destacas en el ámbito de la Informática")

st.divider()
with st.expander('Más información sobre Mujeres destacas en el ámbito de la Informática - Argentina'):
    st.markdown("""
    Aunque 6 de cada 10 universitarias en la Argentina son mujeres, representan solo el 25 % del total de quienes estudian 
    ingeniería y ciencias aplicadas, y el 15 % de las inscripciones en la carrera de programación. \n
    
    Los comienzos de la informática en la Argentina están marcados por acontecimientos simultáneos, que se produjeron en 1961.
    Por un lado, se instaló la computadora Mercury de la empresa británica Ferranti, una iniciativa convertida en éxito de la mano de Manuel Sadosky, 
    entonces vicedecano de la Facultad de Ciencias Exactas de la UBA. 
    La máquina formó parte del Instituto de Cálculo dentro de la universidad, creado también por Sadosky, que albergó a numerosos grupos de 
    investigación que pronto alcanzaron prestigio internacional, abriendo el primer surco por donde desarrollarían su camino las ciencias de 
    la computación en América Latina. La Mercury, rebautizada con el nombre de Clementina, fue la primera computadora de gran porte utilizada 
    con fines científicos en la Argentina. A comienzos de ese mismo año y también en Buenos Aires, se instaló la primera IBM 1401, que fue 
    elegida por numerosas empresas del país, tanto del ámbito privado como del público, que la utilizaban para aplicaciones fundamentalmente 
    administrativas y comerciales. En esos tiempos, hubo mujeres pioneras que sobresalieron en este despegue informático. Fueron profesionales 
    que por su protagonismo y relevancia han sido reconocidas por sus pares, a partir de sus sobresalientes trayectorias.
    \n
    FUENTE: Educ.ar""")


#separamos los elementos del diccionario, borrando la clave 'Informatica' que ya no es necesaria
Infwomen = ['Cecilia Berdichevsky', 'Rebeca Cherep De Guber', 'Victoria Raquel Bajar', 'Noemí García',
                    'Ida Holz','Gladys Beatriz Rizzo','Ida Bianchi']

Data = {'Cecilia Berdichevsky': "convertirse en la primera programadora de la primera computadora científica que tuvo Argentina: Clementina, que dio inicio a la programación en dicho país",
        'Rebeca Cherep De Guber': "formar a los primeros computadores científicos en la UBA, y creó la primera empresa privada argentina orientada al desarrollo de programas de computación. En la posición de Secretaria Ejecutiva en el Instituto de Cálculo, contribuyó en el proceso de instalación y detarrollo de la célebre Clementina. Además, fue una de las directoras de ACT, empresa que desarrolló importantes modelos matemáticos computacionales.",
        'Victoria Raquel Bajar':"ser la primer mujer graduada de la carrera de Computador Científico (siendo Computadora Científica) en Argentina. Formó parte del grupo de Lingüística Computacional, aprendiendo a programar en Autocode.",
        'Noemí García': "graduarse entre las primeras Computadoras Científicas, en Ciencias Exactas de la UBA (1966). Formó parte del grupo de programadoras que desarrolló con éxito el compilador COMIC. Se especializó en el Desarrollo de Sistemas relacionados con la Salud y Seguridad Social",
        'Ida Bianchi': "destacarse en numerosos temas técnicos, incluyendo COBOL, LINC, los equipos Sorter y el software asociado que utilizaban los bancos. Fue la primera mujer profesional de Burroughs, y trabajó con equipos de todos los proveedores que protagonizaron el arranque de la informática en la Argentina",
        'Gladys Beatriz Rizzo': "convertirse en la Ingeniera de Sistemas más prestigiosa del sector Gobierno. Ingresó a IBM y se destacó enormemente con la característica de ser, por años, la única mujer entre todos los profesionales.",
        'Ida Holz': "ser la <<madre de internet>>. Lideró el desarrollo de Internet en Uruguay, instalando el primer nodo de Internet allí. Obtuvo el Premio a la Trayectoria 2009, otorgado por el Registro de Direcciones de Internet para América Latina y el Caribe (LACNIC)."}

 # Mostrar el selectbox con las mujeres en la lista
selected_women = st.selectbox('Selecciona una Mujer', Infwomen)
selected_women_data = Data[selected_women]

if selected_women:
            st.write(f'Has seleccionado: {selected_women}')
            st.write(f'Es reconocida por {selected_women_data}')