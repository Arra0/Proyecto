import streamlit as st
import re 

if "DB" not in st.session_state:
    st.session_state.DB = []

def agregar(nombre,app,apm,nT,correo,dir,cumple,notas):
     datos = {"Nombre":nombre,"Primer apellido":app,"Segundo apellido":apm,"Numero telefonico":nT,"Correo":correo,"Direccion":dir,"Cumpleaños":cumple,"Notas":notas}
     st.session_state.DB.append(datos)


def modificar_contacto(contactos, indice, nuevo_nombre, nuevo_app, nuevo_apm, nuevo_numeroT, nuevo_correo, nueva_dir, nuevo_cumple):
        contacto = contactos[indice]
        contacto["Nombre"] = nuevo_nombre
        contacto["Primer apellido"] = nuevo_app
        contacto["Segundo apellido"] = nuevo_apm
        contacto["Numero telefonico"] = nuevo_numeroT
        contacto["Correo"] = nuevo_correo
        contacto["Direccion"] = nueva_dir
        contacto["Cumpleaños"] = nuevo_cumple
        contacto["Notas"] = nuevo_nota
        
def borrar(indice):
    st.session_state.DB.pop(indice)
     

opcion = st.sidebar.selectbox("opciones",["Agregar contacto","Modificar contacto","Borrar contacto","Consultar contactos"])
nombres = [contacto.get("Nombre") for contacto in st.session_state.DB]

st.title("Agenda de contactos")
match opcion:
        case "Agregar contacto":
            st.header("Agregar nuevo contacto", )
            nombre = st.text_input("Nombre")
            apellidoP = st.text_input("Primer apellido")
            apellidoM = st.text_input("Segundo apellido")
            numeroT = st.number_input("Ingres seu numero de telefeono",value=312,step=1)
            email = st.text_input("Ingrese su correo electornico",value= "@hotmail.com")
            direccion = st.text_input("Ingrece su direccion")
            cumpleaños = st.date_input("fecha de cumpleaños",)
            Notas = st.text_input("Notas",value= "cosas que le gustan que no le gustan etc")
            if st.button("agregar"):
                 if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    agregar(nombre,apellidoP,apellidoM,numeroT,email,direccion,cumpleaños,Notas)
                    st.success("Se agrego el usuario corectamente")
                 else:
                    st.warning("el correo no es valido")
        case "Consultar contactos":
          st.header("Contactos", )
          if len(st.session_state.DB) > 0 :
              for e in st.session_state.DB:
                st.write("***************************************************************\n")
                for i in e :
                    st.write(f"{i}:  {e[i]}")
          else:
              st.warning("No tienes contactos :()")
        case "Modificar contacto":
            st.header("Modificar contacots")
            if len(st.session_state.DB) > 0:
                nombre_modificar = st.selectbox("Seleccione el contacto a modificar:", nombres)
                indice_modificar = nombres.index(nombre_modificar)
        
                nuevo_nombre = st.text_input("nombre:", value=st.session_state.DB[indice_modificar].get("Nombre"))
                nuevo_app = st.text_input("primer apellido:", value=st.session_state.DB[indice_modificar].get("Primer apellido"))
                nuevo_apm = st.text_input("segundo apellido:", value=st.session_state.DB[indice_modificar].get("Segundo apellido"))
                nuevo_numeroT = st.number_input("número de teléfono:", value=st.session_state.DB[indice_modificar].get("Numero telefonico"), step=1)
                nuevo_correo = st.text_input(" correo electrónico:", value=st.session_state.DB[indice_modificar].get("Correo"))
                nueva_dir = st.text_input("dirección:", value=st.session_state.DB[indice_modificar].get("Direccion"))
                nuevo_cumple = st.date_input("fecha de cumpleaños:", value=st.session_state.DB[indice_modificar].get("Cumpleaños"))
                nuevo_nota = st.text_input("Notas:", value=st.session_state.DB[indice_modificar].get("Notas"))

        
                if st.button("Modificar"):
                    if modificar_contacto(
                    st.session_state.DB, indice_modificar, nuevo_nombre, nuevo_app, nuevo_apm,
                    nuevo_numeroT, nuevo_correo, nueva_dir, nuevo_cumple):
                        st.success(f"Contacto modificado: {nombre_modificar}")
            else:
             st.warning("No tienes contactos :()")
        case "Borrar contacto":
            st.header("Borrar contactos")
            if len(st.session_state.DB) > 0:
                borrar_nombre = st.selectbox("Seleccione el contactoque borrara:", nombres)
                i = nombres.index(borrar_nombre)
                st.write("<h1 style='white:; font-size:36px';> Informacio del contacto", unsafe_allow_html=True)
                st.write("Nombre: ",st.session_state.DB[i].get("Nombre"))
                st.write("Primer apellido: ",st.session_state.DB[i].get("Primer apellido"))
                st.write("Segundo apellido: ",st.session_state.DB[i].get("Segundo apellido"))
                st.write("Numero:",st.session_state.DB[i].get("Numero telefonico"))
                st.write("Correo: ",st.session_state.DB[i].get("Correo"))
                st.write("Direccion",st.session_state.DB[i].get("Direccion"))
                st.write("Cumpleaños",st.session_state.DB[i].get("Cumpleaños"))
                st.write("Notas",st.session_state.DB[i].get("Notas"))
                if st.button("Borrar contacto"):
                    borrar(i)
                    st.success(" el contacto fue borrado ",)
            else :
                st.warning("No hay contactos que puedas eliminar ")

