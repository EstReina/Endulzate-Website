from flask import Flask, render_template
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

# Cambiar el backend para evitar usar Tkinter
matplotlib.use('Agg')

app = Flask(__name__)

# Leer el archivo CSV
df = pd.read_csv('Estadisticas.csv', sep=';')
df.columns = df.columns.str.strip()


@app.route('/')
def show_charts():
    return render_template('Estadisticas.html')

# Seleccionar datos de ejemplo para graficar (modificar según lo que necesites)
ciudades = df['Ciudad'].value_counts().head()  # Top 5 ciudades con más registros
año = df['Año'].value_counts().sort_index()  # Actividad por año (ordenada)
productos = df['Producto'].value_counts().head()  # Top 5 productos más vendidos
genero = df['Género'].value_counts()  # Distribución de género
fechas = df['Fecha'].value_counts().sort_index()

colors = ['#b29fc5', '#f7bc81', '#f3a5bf', '#fdf39f', '#91c2a2']


# Gráfico de Barras (para distribución de género)

fig1, ax1 = plt.subplots()
ax1.bar(genero.index, genero.values, color='#bfe1f1')
ax1.set_xlabel('Género', fontweight='bold')
ax1.set_ylabel('Unidades Vendidas', fontweight='bold')
plt.tight_layout()
plt.savefig('static/img/barras.png')
plt.close(fig1)

#Gráfico de Torta (para ciudades con más registros)

fig2, ax2 = plt.subplots()
ax2.pie(ciudades.values, labels=ciudades.index, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.tight_layout()
plt.savefig('static/img/torta.png')
plt.close(fig2)

# Gráfico de Líneas (para actividad por fecha)

fig3, ax3 = plt.subplots()
ax3.plot(año.index, año.values, marker='o', color='#b29fc5')
ax3.set_xlabel('Año', fontweight='bold')
ax3.set_ylabel('Unidades Vendidas', fontweight='bold')
plt.tight_layout()
plt.savefig('static/img/lineas.png')
plt.close(fig3)


# Gráfico de Área (para productos más vendidos)
fig4, ax4 = plt.subplots()
ax4.fill_between(productos.index, productos.values, color="#f7bc81", alpha=0.6)
ax4.set_xlabel('Producto', fontweight='bold')
ax4.set_ylabel('Unidades Vendidas', fontweight='bold')
plt.tight_layout()
plt.savefig('static/img/area.png')
plt.close(fig4)


if __name__ == '__main__':
    app.run(debug=True)