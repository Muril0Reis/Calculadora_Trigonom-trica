import tkinter as tk
from tkinter import messagebox
from calculos import calcular_distancia, calcular_angulos

def executar_calcular_distancia():
    try:
        cateto1 = float(entry_cateto1.get())
        cateto2 = float(entry_cateto2.get())

        if cateto1 <= 0 or cateto2 <= 0:
            raise ValueError("Os valores devem ser positivos!")

        hipotenusa = (cateto1**2 + cateto2**2) ** 0.5
        messagebox.showinfo("Resultado", f"Comprimento da hipotenusa: {hipotenusa:.2f}")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def executar_calcular_angulos():
    try:
        lado = float(entry_lado.get())
        angulo_graus = float(entry_angulo.get())

        if lado <= 0 or angulo_graus <= 0 or angulo_graus >= 90:
            raise ValueError("Lado deve ser positivo e o ângulo entre 0 e 90 graus!")

        import math
        angulo_radianos = math.radians(angulo_graus)
        hipotenusa = lado / math.sin(angulo_radianos)
        outro_lado = (hipotenusa**2 - lado**2) ** 0.5

        messagebox.showinfo("Resultado",
                            f"Lados: {lado:.2f}, {outro_lado:.2f}, {hipotenusa:.2f}\n"
                            f"Ângulos: {angulo_graus:.2f}°, {90 - angulo_graus:.2f}°, 90°")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def criar_interface():
    root = tk.Tk()
    root.title("Calculadora Trigonométrica")

    # Frame para cálculo de distância
    frame_distancia = tk.LabelFrame(root, text="Cálculo de Distância (Teorema de Pitágoras)", padx=10, pady=10)
    frame_distancia.pack(padx=10, pady=5, fill="both", expand=True)

    tk.Label(frame_distancia, text="Cateto 1:").grid(row=0, column=0, pady=5, sticky="w")
    tk.Label(frame_distancia, text="Cateto 2:").grid(row=1, column=0, pady=5, sticky="w")

    global entry_cateto1, entry_cateto2
    entry_cateto1 = tk.Entry(frame_distancia)
    entry_cateto2 = tk.Entry(frame_distancia)
    entry_cateto1.grid(row=0, column=1, pady=5, padx=5)
    entry_cateto2.grid(row=1, column=1, pady=5, padx=5)

    btn_distancia = tk.Button(frame_distancia, text="Calcular Hipotenusa", command=executar_calcular_distancia)
    btn_distancia.grid(row=2, column=0, columnspan=2, pady=10)

    # Frame para cálculo de ângulos
    frame_angulos = tk.LabelFrame(root, text="Cálculo de Ângulos", padx=10, pady=10)
    frame_angulos.pack(padx=10, pady=5, fill="both", expand=True)

    tk.Label(frame_angulos, text="Lado conhecido:").grid(row=0, column=0, pady=5, sticky="w")
    tk.Label(frame_angulos, text="Ângulo (em graus):").grid(row=1, column=0, pady=5, sticky="w")

    global entry_lado, entry_angulo
    entry_lado = tk.Entry(frame_angulos)
    entry_angulo = tk.Entry(frame_angulos)
    entry_lado.grid(row=0, column=1, pady=5, padx=5)
    entry_angulo.grid(row=1, column=1, pady=5, padx=5)

    btn_angulos = tk.Button(frame_angulos, text="Calcular Lados e Ângulos", command=executar_calcular_angulos)
    btn_angulos.grid(row=2, column=0, columnspan=2, pady=10)

    # Botão para sair
    btn_sair = tk.Button(root, text="Sair", command=root.quit)
    btn_sair.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    criar_interface()
