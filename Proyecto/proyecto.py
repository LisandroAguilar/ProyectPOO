import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter.font import Font

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="Proyecto"
    )
    return conexion

def validar_ingreso():
    
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="Proyecto"
    )
    
    usuario = nombre_usuario.get()
    contrasena = password.get()
    
    if not usuario or not contrasena:
        mensaje_campos_inicio.config(text="Por favor, rellena todos los campos")
        ventana_inicio.after(3000, limpiar_mensaje_campos)
        return
    
    cursor = conexion.cursor()
    consulta = "SELECT * FROM acceso WHERE nombre=%s AND contrasena=%s"
    parametros = (usuario, contrasena)
    cursor.execute(consulta, parametros)
    resultado = cursor.fetchone()
    
    if resultado is None:
        mensaje_incorrecto_inicio.config(text="Nombre de usuario y/o contraseña incorrectos")
        ventana_inicio.after(3000, limpiar_mensaje_incorrecto)
        return
    
    else:
        ventana_inicio.destroy()
        abrir_ventana_principal()

def abrir_ventana_principal():
    
    ventana_principal = tk.Tk()
    ventana_principal.title("Principal")
    ventana_principal.geometry("600x600+350+80")
    ventana_principal.config(bg="#21A2F7") 

    def registrar():
    
        ventana_registro = tk.Toplevel(ventana_principal)
        ventana_registro.title("Registros")
        ventana_registro.geometry("600x600+350+80")
        ventana_registro.config(bg="#21A2F7") 
        
        def cerrar_ventana_actual():
            ventana_registro.destroy()
            ventana_principal.deiconify()
        
        def registrar_usuario():
        
            ventana_registro_usuario = tk.Toplevel(ventana_registro)
            ventana_registro_usuario.title("Registro de usuario")
            ventana_registro_usuario.geometry("600x600+350+80")
            ventana_registro_usuario.config(bg="#21A2F7")
        
            def cerrar_ventana_actual():
                ventana_registro_usuario.destroy()
                ventana_registro.deiconify()
            
            def limpiar_campos():
                entrada_Id.delete(0, tk.END)
                entrada_contrasena.delete(0, tk.END)
                entrada_nombre.delete(0, tk.END)
                entrada_paterno.delete(0, tk.END)
                entrada_materno.delete(0, tk.END)
                entrada_telefono.delete(0, tk.END)
                entrada_correo.delete(0, tk.END)
            
            etiqueta_Id = tk.Label(ventana_registro_usuario, text="Id:", font=("Arial", 20), bg="#DAF7A6", fg='black')
            etiqueta_Id.pack()
            etiqueta_Id.place(x=10, y=50, width=250, height=30)
            
            entrada_Id = tk.Entry(ventana_registro_usuario, font=("Arial", 14))
            entrada_Id.pack()
            entrada_Id.place(x=270, y=50, width=200, height=40)
            
            etiqueta_contrasena = tk.Label(ventana_registro_usuario, text="Contraseña:", font=("Arial", 20), bg="#DAF7A6", fg='black')
            etiqueta_contrasena.pack()
            etiqueta_contrasena.place(x=10, y=110, width=250, height=30)
            
            entrada_contrasena = tk.Entry(ventana_registro_usuario, show="*", font=("Arial", 14))
            entrada_contrasena.pack()
            entrada_contrasena.place(x=270, y=110, width=200, height=40)
            
            etiqueta_nombre = tk.Label(ventana_registro_usuario, text="Nombre:", font=("Arial", 20), bg="#DAF7A6", fg='black')
            etiqueta_nombre.pack()
            etiqueta_nombre.place(x=10, y=170, width=250, height=30)
            
            entrada_nombre = tk.Entry(ventana_registro_usuario, font=("Arial", 14))
            entrada_nombre.pack()
            entrada_nombre.place(x=270, y=170, width=200, height=40)
            
            etiqueta_paterno = tk.Label(ventana_registro_usuario, text="Apellido Paterno:", font=("Arial", 20), bg="#DAF7A6", fg='black')
            etiqueta_paterno.pack()
            etiqueta_paterno.place(x=10, y=230, width=250, height=30)
            
            entrada_paterno = tk.Entry(ventana_registro_usuario, font=("Arial", 14))
            entrada_paterno.pack()
            entrada_paterno.place(x=270, y=230, width=200, height=40)
            
            etiqueta_materno = tk.Label(ventana_registro_usuario, text="Apellido Materno:", font=("Arial", 20), bg="#DAF7A6", fg='black')
            etiqueta_materno.pack()
            etiqueta_materno.place(x=10, y=290, width=250, height=30)
            
            entrada_materno = tk.Entry(ventana_registro_usuario, font=("Arial", 14))
            entrada_materno.pack()
            entrada_materno.place(x=270, y=290, width=200, height=40)
            
            etiqueta_telefono = tk.Label(ventana_registro_usuario, text="Telefono:", font=("Arial", 20), bg="#DAF7A6", fg='black')
            etiqueta_telefono.pack()
            etiqueta_telefono.place(x=10, y=350, width=250, height=30)
            
            entrada_telefono = tk.Entry(ventana_registro_usuario, font=("Arial", 14))
            entrada_telefono.pack()
            entrada_telefono.place(x=270, y=350, width=200, height=40)
            
            etiqueta_correo = tk.Label(ventana_registro_usuario, text="Correo:", font=("Arial", 20), bg="#DAF7A6", fg='black')
            etiqueta_correo.pack()
            etiqueta_correo.place(x=10, y=410, width=250, height=30)
            
            entrada_correo = tk.Entry(ventana_registro_usuario, font=("Arial", 14))
            entrada_correo.pack()
            entrada_correo.place(x=270, y=410, width=200, height=40)
            
            def limpiar_mensaje():
                if mensaje_guardado.winfo_exists():
                    mensaje_guardado.config(text="")
                    
            def guardar_registro():
                
                conexion = conectar()
                cursor = conexion.cursor()
                
                Id = entrada_Id.get()
                contrasena = entrada_contrasena.get()
                nombre = entrada_nombre.get()
                paterno = entrada_paterno.get()
                materno = entrada_materno.get()
                telefono = entrada_telefono.get()
                correo = entrada_correo.get()
                
                consulta = "INSERT INTO Usuario (ID_Usuario, Contrasena, Nombre, Paterno, Materno, Telefono, Correo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                valores = (Id, contrasena, nombre, paterno, materno, telefono, correo)
                cursor.execute(consulta, valores)
                
                mensaje_guardado.config(text="Registro exitoso")
                ventana_registro_usuario.after(3000, limpiar_mensaje) 
                
                conexion.commit()
                conexion.close()
                
            boton_guardar = tk.Button(ventana_registro_usuario, text="Guardar", command=guardar_registro, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_guardar.pack()
            boton_guardar.place(x=250, y=500, width=120, height=50)
            
            regresar = tk.Button(ventana_registro_usuario, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            regresar.pack()
            regresar.place(x=100, y=500, width=120, height=50)
            
            boton_limpiar = tk.Button(ventana_registro_usuario, text="Limpiar", command=limpiar_campos, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_limpiar.pack()
            boton_limpiar.place(x=400, y=500, width=120, height=50)
            
            mensaje_guardado = tk.Label(ventana_registro_usuario, text="", fg="red", font=("Arial", 18), bg="#DAF7A6")
            mensaje_guardado.pack()
            mensaje_guardado.place(x=60, y=460)
            
            ventana_registro.withdraw()
            
            ventana_registro_usuario.mainloop()
            
        def registrar_recicladora():
            
            ventana_registro_recicladora = tk.Toplevel(ventana_registro)
            ventana_registro_recicladora.title("Registro de recicladora")
            ventana_registro_recicladora.geometry("600x600+350+80")
            ventana_registro_recicladora.config(bg="#21A2F7")
            
            def cerrar_ventana_actual():
                ventana_registro_recicladora.destroy()
                ventana_registro.deiconify()
            
            def limpiar_campos():
                entrada_Id.delete(0, tk.END)
                entrada_nombre.delete(0, tk.END)
                entrada_direccion.delete(0, tk.END)
                entrada_telefono.delete(0, tk.END)
                entrada_correo.delete(0, tk.END)
                entrada_tipo.delete(0,tk, END)
                
            etiqueta_Id = tk.Label(ventana_registro_recicladora, text="Id:", font=("Arial", 20), bg="#DAF7A6", fg='black')
            etiqueta_Id.pack()
            etiqueta_Id.place(x=10, y=50, width=250, height=30)
            
            entrada_Id = tk.Entry(ventana_registro_recicladora, font=("Arial", 14))
            entrada_Id.pack()
            entrada_Id.place(x=270, y=50, width=200, height=40)
            
            etiqueta_nombre = tk.Label(ventana_registro_recicladora, text="Nombre:", font=("Arial", 20), bg="#DAF7A6", fg='black')
            etiqueta_nombre.pack()
            etiqueta_nombre.place(x=10, y=110, width=250, height=30)
            
            entrada_nombre = tk.Entry(ventana_registro_recicladora, font=("Arial", 14))
            entrada_nombre.pack()
            entrada_nombre.place(x=270, y=110, width=200, height=40)
            
            etiqueta_direccion = tk.Label(ventana_registro_recicladora, text="Dirección:", font=("Arial", 20), bg="#DAF7A6", fg='black')
            etiqueta_direccion.pack()
            etiqueta_direccion.place(x=10, y=170, width=250, height=30)
            
            entrada_direccion = tk.Entry(ventana_registro_recicladora, font=("Arial", 14))
            entrada_direccion.pack()
            entrada_direccion.place(x=270, y=170, width=200, height=40)
            
            etiqueta_telefono = tk.Label(ventana_registro_recicladora, text="Telefono:", font=("Arial", 20), bg="#DAF7A6", fg='black')
            etiqueta_telefono.pack()
            etiqueta_telefono.place(x=10, y=230, width=250, height=30)
            
            entrada_telefono = tk.Entry(ventana_registro_recicladora, font=("Arial", 14))
            entrada_telefono.pack()
            entrada_telefono.place(x=270, y=230, width=200, height=40)
            
            etiqueta_correo = tk.Label(ventana_registro_recicladora, text="Correo:", font=("Arial", 20), bg="#DAF7A6", fg='black')
            etiqueta_correo.pack()
            etiqueta_correo.place(x=10, y=290, width=250, height=30)
            
            entrada_correo = tk.Entry(ventana_registro_recicladora, font=("Arial", 14))
            entrada_correo.pack()
            entrada_correo.place(x=270, y=290, width=200, height=40)
            
            etiqueta_tipo = tk.Label(ventana_registro_recicladora, text="Tipo:", font=("Arial", 20), bg="#DAF7A6", fg='black')
            etiqueta_tipo.pack()
            etiqueta_tipo.place(x=10, y=350, width=250, height=30)
            
            entrada_tipo = tk.Entry(ventana_registro_recicladora, font=("Arial", 14))
            entrada_tipo.pack()
            entrada_tipo.place(x=270, y=350, width=200, height=40)
            
            def limpiar_mensaje():
                mensaje_guardado.config(text="")
                
            def guardar_recicladora():
                
                conexion = conectar()
                cursor = conexion.cursor()
                
                Id = entrada_Id.get()
                nombre = entrada_nombre.get()
                direccion = entrada_direccion.get()
                telefono = entrada_telefono.get()
                correo = entrada_correo.get()
                tipo = entrada_tipo.get()
                
                consulta = "INSERT INTO Recicladora (ID_Recicladora, Nombre, Direccion, Telefono, Correo, Tipo) VALUES (%s, %s, %s, %s, %s, %s)"
                valores = (Id, nombre, direccion, telefono, correo, tipo)
                cursor.execute(consulta, valores)
                
                mensaje_guardado.config(text="Registro exitoso")
                ventana_registro_recicladora.after(3000, limpiar_mensaje) 
                
                conexion.commit()
                conexion.close()
                
            boton_guardar = tk.Button(ventana_registro_recicladora, text="Guardar", command=guardar_recicladora, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_guardar.pack()
            boton_guardar.place(x=250, y=500, width=120, height=50)
            
            regresar = tk.Button(ventana_registro_recicladora, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            regresar.pack()
            regresar.place(x=100, y=500, width=120, height=50)
            
            boton_limpiar = tk.Button(ventana_registro_recicladora, text="Limpiar", command=limpiar_campos, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_limpiar.pack()
            boton_limpiar.place(x=400, y=500, width=120, height=50)
            
            mensaje_guardado = tk.Label(ventana_registro_recicladora, text="", fg="red", font=("Arial", 18), bg="#DAF7A6")
            mensaje_guardado.pack()
            mensaje_guardado.place(x=60, y=460)
                
            ventana_registro.withdraw()
            
            ventana_registro_recicladora.mainloop()
                
        boton_usuario_usuario = tk.Button(ventana_registro, text="Nuevo usuario", command=registrar_usuario, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        boton_usuario_usuario.pack()
        boton_usuario_usuario.place(x=250, y=500, width=120, height=50)
        
        boton_recicladora_recicladora = tk.Button(ventana_registro, text="Nueva recicladora", command=registrar_recicladora, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        boton_recicladora_recicladora.pack()
        boton_recicladora_recicladora.place(x=400, y=500, width=120, height=50)
                        
        regresar_usuario = tk.Button(ventana_registro, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        regresar_usuario.pack()
        regresar_usuario.place(x=100, y=500, width=120, height=50)
                
        ventana_principal.withdraw()
        
        ventana_registro.mainloop()

    def eliminar():
        ventana_eliminar = tk.Toplevel(ventana_principal)
        ventana_eliminar.title("Eliminar registro")
        ventana_eliminar.geometry("600x600+350+80")
        ventana_eliminar.config(bg="#21A2F7") 
        
        def cerrar_ventana_actual():
                ventana_eliminar.destroy()
                ventana_principal.deiconify()
        
        def eliminar_usuario():
            ventana_eliminar_usuario = tk.Toplevel(ventana_eliminar)
            ventana_eliminar_usuario.title("Eliminar usuario")
            ventana_eliminar_usuario.geometry("600x600+350+80")
            ventana_eliminar_usuario.config(bg="#21A2F7") 
            
            def cerrar_ventana_actual():
                ventana_eliminar_usuario.destroy()
                ventana_eliminar.deiconify()

            etiqueta_id = tk.Label(ventana_eliminar_usuario, text="Id:", font=("Arial", 18), bg="#21A2F7", fg='black')
            etiqueta_id.pack()
            etiqueta_id.place(x=170, y=30, width=280, height=35)
            
            entrada_id = tk.Entry(ventana_eliminar_usuario)
            entrada_id.pack()
            entrada_id.place(x=170, y=100, width=280, height=35)
            
            etiqueta_nombre = tk.Label(ventana_eliminar_usuario, text="Nombre:", font=("Arial", 18), bg="#21A2F7", fg='black')
            etiqueta_nombre.pack()
            etiqueta_nombre.place(x=170, y=130, width=280, height=35)
            
            entrada_nombre = tk.Entry(ventana_eliminar_usuario)
            entrada_nombre.pack()
            entrada_nombre.place(x=170, y=200, width=280, height=35)

            def eliminar_registro():
                
                conexion = conectar()
                cursor = conexion.cursor()
                
                id = int(entrada_id.get())
                
                consulta = "DELETE FROM Usuario WHERE ID_Usuario = %s and Nombre = %s"
                valores = (id,)
                cursor.execute(consulta, valores)
                
                conexion.commit()
                conexion.close()
                
                cerrar_ventana_actual()
            
            boton_eliminar_usuario = tk.Button(ventana_eliminar_usuario, text="Guardar", command=eliminar_registro, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_eliminar_usuario.pack()
            boton_eliminar_usuario.place(x=400, y=350, width=200, height=20)
            
            regresar = tk.Button(ventana_eliminar_usuario, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            regresar.pack()
            regresar.place(x=400, y=10, width=350, height=50)
        
            ventana_eliminar.withdraw()
                
            ventana_eliminar_usuario.mainloop()
            
        def eliminar_recicladora():
            
            ventana_eliminar_recicladora = tk.Toplevel(ventana_eliminar)
            ventana_eliminar_recicladora.title("Eliminar usuario")
            ventana_eliminar_recicladora.geometry("600x600+350+80")
            ventana_eliminar_recicladora.config(bg="#21A2F7") 
            
            def cerrar_ventana_actual():
                ventana_eliminar_recicladora.destroy()
                ventana_eliminar.deiconify()
                
            def limpiar_campos():
                entrada_id.delete(0, tk.END)
                entrada_nombre.delete(0, tk.END)
            
            etiqueta_id = tk.Label(ventana_eliminar_recicladora, text="Id:")
            etiqueta_id.pack()
            etiqueta_id.place(x=170, y=30, width=280, height=35)
            
            entrada_id = tk.Entry(ventana_eliminar_recicladora)
            entrada_id.pack()
            entrada_id.place(x=170, y=100, width=280, height=35)
            
            etiqueta_nombre = tk.Label(ventana_eliminar_recicladora, text="Nombre:")
            etiqueta_nombre.pack()
            etiqueta_nombre.place(x=170, y=130, width=280, height=35)
            
            entrada_nombre = tk.Entry(ventana_eliminar_recicladora)
            entrada_nombre.pack()
            entrada_nombre.place(x=170, y=200, width=280, height=35)

            def eliminar_registro():
                
                conexion = conectar()
                cursor = conexion.cursor()
                
                id = int(entrada_id.get())
                
                consulta = "DELETE FROM Recicladora WHERE ID_Recicladora = %s and Nombre = %s"
                valores = (id, nombre)
                cursor.execute(consulta, valores)
                
                conexion.commit()
                conexion.close()
                
                cerrar_ventana_actual()
            
            boton_eliminar_recicladora = tk.Button(ventana_eliminar_recicladora, text="Guardar", command=eliminar_registro, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_eliminar_recicladora.pack()
            boton_eliminar_recicladora.place(x=150, y=400, width=120, height=50)
            
            regresar = tk.Button(ventana_eliminar_recicladora, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            regresar.pack()
            regresar.place(x=250, y=400, width=120, height=50)
            
            boton_limpiar = tk.Button(ventana_eliminar_recicladora, text="Limpiar", command=limpiar_campos, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
            boton_limpiar.pack()
            boton_limpiar.place(x=400, y=500, width=120, height=50)
        
            ventana_eliminar.withdraw()
                
            ventana_eliminar_recicladora.mainloop()
            
        boton_usuario_usuario = tk.Button(ventana_eliminar, text="Eliminar usuario", command=eliminar_usuario, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        boton_usuario_usuario.pack()
        boton_usuario_usuario.place(x=250, y=500, width=120, height=50)
        
        boton_recicladora_recicladora = tk.Button(ventana_eliminar, text="Eliminar recicladora", command=eliminar_recicladora, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        boton_recicladora_recicladora.pack()
        boton_recicladora_recicladora.place(x=400, y=500, width=120, height=50)
                        
        regresar_eliminar = tk.Button(ventana_eliminar, text="Regresar", command=cerrar_ventana_actual, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
        regresar_eliminar.pack()
        regresar_eliminar.place(x=100, y=500, width=120, height=50)
        
        ventana_principal.withdraw()
        
        ventana_eliminar.mainloop()
            
    def ver_registros():
        
        conexion = conectar()
        cursor = conexion.cursor()
        
        consulta = "SELECT * FROM Usuario"
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        
        ventana_registros = tk.Toplevel(ventana_principal)
        
        for resultado in resultados:
            etiqueta_resultado = tk.Label(ventana_registros, text=str(resultado))
            etiqueta_resultado.pack()
        
        conexion.close()

    registrar = tk.Button(ventana_principal, text="Registros", command=registrar, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
    registrar.pack()
    registrar.place(x=10, y=10, width=120, height=50)
    
    eliminar = tk.Button(ventana_principal, text="Eliminar", command=eliminar, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
    eliminar.pack()
    eliminar.place(x=150, y=10, width=120, height=50)
    
    ver_registro = tk.Button(ventana_principal, text="Ver registro", command=ver_registros, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
    ver_registro.pack()
    ver_registro.place(x=290, y=10, width=120, height=50)
    
    salir = tk.Button(ventana_principal, text="Salir", command=ventana_principal.destroy, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
    salir.pack()
    salir.place(x=430, y=10, width=120, height=50)
    
    ventana_principal.mainloop()

ventana_inicio = tk.Tk()
ventana_inicio.title("Inicio de sesión")
ventana_inicio.geometry("600x600+350+80")
ventana_inicio.config(bg="#21A2F7")

def limpiar_mensaje_incorrecto():
    if mensaje_incorrecto_inicio.winfo_exists():
        mensaje_incorrecto_inicio.config(text="")
        
mensaje_incorrecto_inicio = tk.Label(ventana_inicio, text="", fg="red", font=("Arial", 18), bg="#21A2F7")
mensaje_incorrecto_inicio.pack()
mensaje_incorrecto_inicio.place(x=60, y=460)
ventana_inicio.after(3000, limpiar_mensaje_incorrecto)

def limpiar_mensaje_campos():
    if mensaje_campos_inicio.winfo_exists():
        mensaje_campos_inicio.config(text="")
        
mensaje_campos_inicio = tk.Label(ventana_inicio, text="", fg="red", font=("Arial", 18), bg="#21A2F7")
mensaje_campos_inicio.pack()
mensaje_campos_inicio.place(x=110, y=460)
ventana_inicio.after(3000, limpiar_mensaje_campos)

iniciar_label = tk.Label(ventana_inicio, text="Iniciar sesión", font=("Arial", 35), bg="#21A2F7", fg='black')
iniciar_label.pack()
iniciar_label.place(x=170, y=30, width=280, height=35)

nombre_usuario_label = tk.Label(ventana_inicio, text="Nombre de usuario", font=("Arial", 18), bg="#21A2F7", fg='black')
nombre_usuario_label.pack()
nombre_usuario_label.place(x=10, y=140, width=250, height=30)

password_label = tk.Label(ventana_inicio, text="Contraseña", font=("Arial", 18), bg="#21A2F7", fg='black')
password_label.pack()
password_label.place(x=10, y=230, width=250, height=30)

nombre_usuario = tk.Entry(ventana_inicio, font=("Arial", 14))
nombre_usuario.pack()
nombre_usuario.place(x=270, y=140, width=200, height=40)

password = tk.Entry(ventana_inicio, show="*", font=("Arial", 20))
password.pack()
password.place(x=270, y=230, width=200, height=40)

iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar sesión", command=validar_ingreso, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
iniciar_sesion.pack()
iniciar_sesion.place(x=220, y=310, width=200, height=50)

salir = tk.Button(ventana_inicio, text="Salir", command=ventana_inicio.destroy, bg="#4CAF50", fg="white", font=("Arial", 12), relief="groove", borderwidth=0)
salir.pack()
salir.place(x=220, y=380, width=200, height=50)

ventana_inicio.mainloop()