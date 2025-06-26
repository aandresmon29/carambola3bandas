import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Nuevas dimensiones reales en cm
height = 302.8       # Largo total de la mesa (área de juego)
width = 152.4        # Ancho total de la mesa (área de juego)
band_grosor = 5    # Grosor de la banda (margen externo)

fig, ax = plt.subplots()
fig.patch.set_facecolor('white')  # Fondo fuera de la banda
ax.set_aspect('equal')
ax.set_xlim(-band_grosor, height + band_grosor)
ax.set_ylim(-band_grosor, width + band_grosor)
ax.set_facecolor('black')  # Banda visible

# Dibujar la superficie verde (área de juego)
table_surface = patches.Rectangle(
    (0, 0), height, width,
    linewidth=0,
    facecolor='lightgray'
)
ax.add_patch(table_surface)

# Borde exterior (opcional, decorativo)
outer_border = patches.Rectangle(
    (-band_grosor, -band_grosor),
    height + 2 * band_grosor,
    width + 2 * band_grosor,
    linewidth=2,
    edgecolor='black',
    facecolor='none'
)
ax.add_patch(outer_border)

# Dibujar diamantes numerados
def draw_diamonds_with_numbers():
    # Lado inferior (horizontal de 0 a 8)
    for i in range(9):
        x = i * height / 8
        ax.plot(x, 0 - band_grosor / 2, 'wo', markersize=4)
        ax.text(x, -5, f"{i}", color='darkgreen', ha='center', va='top', fontsize=8)

    # Lado izquierdo (vertical de 0 a 4)
    for j in range(5):
        y = j * width / 4
        ax.plot(0 - band_grosor / 2, y, 'wo', markersize=4)
        ax.text(-5, y, f"{j}", color='darkgreen', ha='right', va='center', fontsize=8)

    # Lado superior
    for i in range(9):
        x = i * height / 8
        ax.plot(x, width + band_grosor / 2, 'wo', markersize=4)
        ax.text(x, width + 5, f"{i}", color='darkgreen', ha='center', va='bottom', fontsize=8)

    # Lado derecho
    for j in range(5):
        y = j * width / 4
        ax.plot(height + band_grosor / 2, y, 'wo', markersize=4)
        ax.text(height + 5, y, f"{j}", color='darkgreen', ha='left', va='center', fontsize=8)


draw_diamonds_with_numbers()

# Dibujar bolas
def draw_ball(pos, color):
    ball = plt.Circle(pos, 5, color=color, ec='black', zorder=3)
    ax.add_patch(ball)

draw_ball((30, 70), 'white')
draw_ball((220, 100), 'red')
draw_ball((220, 40), 'yellow')

# Estética general
plt.title('Mesa 3 Bandas', color='green', pad=20, fontsize=16)
ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
for spine in ax.spines.values():
    spine.set_visible(False)

plt.show()
