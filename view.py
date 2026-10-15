import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from datetime import datetime

import style

ventana = ttk.Window(title='Bienvenido')
ventana.geometry(f"{style.VENTANA_ANCHO}x{style.VENTANA_ALTO}")
ventana.resizable(False, False)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.iconbitmap(bitmap='resources/libro-alt.png')

lblTitulo = ttk.Label(
    ventana,
    text=style.TEXTO_TITULO,
    font=style.FUENTE_TITULO,
    bootstyle=style.BOOTSTYLE_TITULO
)

lblTitulo.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=style.PAD_TITULO_Y
)

lblNombreEmpleado = ttk.Label(
    ventana,
    text='Nombre del Empleado',
    font=style.FUENTE_ETIQUETA,
    bootstyle=style.BOOTSTYLE_ETIQUETA
)

lblNombreEmpleado.grid(
    row = 1,
    column = 0,
    sticky='e',
    pady = 10
)

entryNombreEmpleado = ttk.Entry(

)

entryNombreEmpleado.grid(
    row = 1,
    column = 1,
    sticky= 'w',
    pady = 10
)



lblPagoPorHora = ttk.Label(
    ventana,
    text='Pago por hora(L)',
    font=style.FUENTE_ETIQUETA,
    bootstyle=style.BOOTSTYLE_ETIQUETA
)

lblPagoPorHora.grid(
    row = 2,
    column = 0,
    sticky='e',
    pady = 10
)

entryPagoPorHora = ttk.Entry(

)

entryPagoPorHora.grid(
    row = 2,
    column = 1,
    sticky = 'w',
    pady = 10
)



lblHorasTrabajadas = ttk.Label(
    ventana,
    text='Horas Trabajadas en el mes',
    font=style.FUENTE_ETIQUETA,
    bootstyle=style.BOOTSTYLE_ETIQUETA
)

lblHorasTrabajadas.grid(
    row = 3,
    column = 0,
    sticky = 'e',
    pady = 10
)

entryHorasTrabajadas = ttk.Entry(

)

entryHorasTrabajadas.grid(
    row = 3,
    column = 1,
    sticky = 'w',
    pady = 10
)

def calculos():
    nombre = entryNombreEmpleado.get().strip()
    pago_por_hora = float(entryPagoPorHora.get().strip())
    horas_trabajadas = float(entryHorasTrabajadas.get().strip())

    salario_bruto = pago_por_hora * horas_trabajadas

    techo = 11903.13
    ihss = min(salario_bruto, techo) * 0.025
    rap = max(salario_bruto - techo, 0) * 0.015

    if salario_bruto <= 22360.36:
        isr = 0
    elif salario_bruto <= 32346.18:
        isr = (salario_bruto - 22360.36) * 0.15
    elif salario_bruto <= 70805.06:
        isr = 1497.87 + (salario_bruto - 32346.18) * 0.20
    else:
        isr = 9189.65 + (salario_bruto - 70805.06) * 0.25

    salario_neto = salario_bruto - ihss - rap - isr

    Messagebox.show_info(title="Resultado del Cálculo", message=f"Nombre del Empleado: {nombre}\nPago por hora: L{pago_por_hora:.2f}\nHoras: {horas_trabajadas}\nSalario Bruto: L{salario_bruto:.2f}\nIHSS: L{ihss:.2f}\nRAP: L{rap:.2f}\nISR: L{isr:.2f}\nSalario Neto: L{salario_neto:.2f}", parent=ventana)

btnCalcular = ttk.Button(
    ventana,
    text='Calcular Salario',
    command=calculos
)


btnCalcular.grid(
    row = 4,
    column = 0,
    columnspan = 2,
    pady = 10
)

btnLimpiar = ttk.Button(
    ventana,
    text='Limpiar'
)

btnLimpiar.grid(
    row = 5,
    column = 0,
    columnspan = 2,
    pady = 10
)

btnSalir = ttk.Button(
    ventana,
    text='Salir',
    command=ventana.destroy
)

btnSalir.grid(
    row = 6,
    column = 0,
    columnspan = 2,
    pady = 10
)

ventana.mainloop()