# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(0, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Alumnos: Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos
    fig = plt.figure()
    fig.suptitle("Line plot funciones", fontsize=16)
    ax1 = fig.add_subplot(2, 2, 1)  # 1 fila, 2 columnas, axes nº1
    ax2 = fig.add_subplot(2, 2, 2)  # 1 fila, 2 columnas, axes nº2
    ax3 = fig.add_subplot(2, 2, 3)  # 1 fila, 2 columnas, axes nº3
    ax4 = fig.add_subplot(2, 2, 4)  # 1 fila, 2 columnas, axes nº4
 
    # Se debe colocar en la leyenda la función que representa
    # cada gráfico
    # Cada gráfico realizarlo con un color distinto
    # a su elección
    # Colocar una grilla a elección
    ax1.plot(x, y1, c='green', marker='.', label="y=x^2")
    ax1.set_facecolor("whitesmoke")
    ax1.legend()
    ax1.grid()
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")

    ax2.plot(x, y2, c='red', marker='.', label="y=x^3")
    ax2.set_facecolor("whitesmoke")
    ax2.legend()
    ax2.grid()
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")

    ax3.plot(x, y3, c='blue', marker='.', label="y=x^2")
    ax3.set_facecolor("whitesmoke")
    ax3.legend()
    ax3.grid()
    ax3.set_xlabel("X")
    ax3.set_ylabel("Y")

    ax4.plot(x, y4, c='black', marker='.', label="y=sqrt(x)")
    ax4.set_facecolor("whitesmoke")
    ax4.legend()
    ax4.grid()
    ax4.set_xlabel("X")
    ax4.set_ylabel("Y")
  
    # Crear acá su gráfico
    plt.show()
    print("terminamos")
