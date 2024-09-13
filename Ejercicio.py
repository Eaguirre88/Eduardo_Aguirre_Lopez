import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ingreso estudiantes Escuela InnovadoresX")

def registrar_datos():
    nombre_estudiante = entry_nombre.get()
    apellido_del_estudiante = entry_apellido_del_estudiante.get()
    edad = entry_edad.get()
    condicion = var_tipo_datos.get()
    materias_opcionales = [var_materia_1.get(), var_materia_2.get()]
    comentarios = text_comentarios.get("1.0", tk.END).strip()
    situacion_ = var_situacion.get()
    
    mensaje = (f"Pedido registrado:\n"
           f"Nombre del estudiante: {nombre_estudiante}\n"
           f"Apellido: {apellido_del_estudiante}\n"
           f"Edad: {edad}\n"
           f"condicion: {condicion}\n"
           f"Materias Opcionales: {materias_opcionales}\n"
           f"Comentarios: {comentarios}\n"
           f"Situacion: {situacion_}")

    messagebox.showinfo("Registro Exitoso", mensaje)

def limpiar_formulario():
    entry_nombre.delete(0, tk.END)
    entry_apellido_del_estudiante.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    var_tipo_datos.set(None)
    var_materia_1.set(0)
    var_materia_2.set(0)
    text_comentarios.delete("1.0", tk.END)

# Frames
frame_estudiante = tk.Frame(ventana)
frame_estudiante.pack(pady=10)

frame_datos = tk.Frame(ventana)
frame_datos.pack(pady=10)

frame_condicion = tk.Frame(ventana)
frame_condicion.pack(pady=10)

frame_materias_opcionales = tk.Frame(ventana)
frame_materias_opcionales.pack(pady=10)

frame_comentarios = tk.Frame(ventana)
frame_comentarios.pack(pady=10)

# Información del Estudiante
label_nombre = tk.Label(frame_estudiante, text="Nombre del Estudiante:")
label_nombre.grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(frame_estudiante)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)
label_apellido_del_estudiante = tk.Label(frame_datos, text="Apellido:")
label_apellido_del_estudiante.grid(row=0, column=0, padx=5, pady=5)
entry_apellido_del_estudiante = tk.Entry(frame_datos)
entry_apellido_del_estudiante.grid(row=0, column=1, padx=5, pady=5)
label_edad = tk.Label(frame_datos, text="Edad:")
label_edad.grid(row=1, column=0, padx=5, pady=5)
entry_edad = tk.Entry(frame_datos)
entry_edad.grid(row=1, column=1, padx=5, pady=5)

# Extras
var_tipo_datos = tk.StringVar()
label_tipo_datos = tk.Label(frame_datos, text="Apellido:")
label_tipo_datos.grid(row=0, column=0, padx=5, pady=5)
radio_condicion = tk.Radiobutton(frame_condicion, text="Inscrito", 
variable=var_tipo_datos, value="Inscrito")
radio_condicion.grid(row=0, column=1, padx=5, pady=5)
radio_condicion = tk.Radiobutton(frame_condicion, text="No Inscrito", 
variable=var_tipo_datos, value="No Inscrito")
radio_condicion.grid(row=0, column=2, padx=5, pady=5)

var_situacion = tk.StringVar() # Definir la variable var_situacion


# Materias Opcionales
var_materia_1 = tk.IntVar()
var_materia_2 = tk.IntVar()
label_materias_opcionales = tk.Label(frame_materias_opcionales, text="Materias Opcionales:")
label_materias_opcionales.grid(row=0, column=0, padx=5, pady=5)
check_Materia_1 = tk.Checkbutton(frame_materias_opcionales, text="Materia 1", variable=var_materia_1)
check_Materia_1.grid(row=0, column=1, padx=5, pady=5)
check_materia_2 = tk.Checkbutton(frame_materias_opcionales, text="Materia 2", variable=var_materia_2)
check_materia_2.grid(row=0, column=2, padx=5, pady=5)

# Comentarios Adicionales
label_comentarios = tk.Label(frame_comentarios, text="Comentarios:")
label_comentarios.grid(row=0, column=0, padx=5, pady=5)
text_comentarios = tk.Text(frame_comentarios, height=4, width=30)
text_comentarios.grid(row=0, column=1, padx=5, pady=5)

# Menú Desplegable para Categoría de Cliente
label_nivel_escolar = tk.Label(frame_estudiante, text="Nivel escolar:")
label_nivel_escolar.grid(row=1, column=0, padx=5, pady=5)
nivel_escolar = ["Primaria", "Secundaria"]
var_nivel_escolar = tk.StringVar()
var_nivel_escolar.set(nivel_escolar[0])
menu_nivel_escolar = tk.OptionMenu(frame_estudiante, var_nivel_escolar, 
*nivel_escolar)
menu_nivel_escolar.grid(row=1, column=1, padx=5, pady=5)

# Botones de Acción
btn_registrar = tk.Button(ventana, text="Registrar Estudiante", command=registrar_datos)
btn_registrar.pack(pady=10)

btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_formulario)
btn_limpiar.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()