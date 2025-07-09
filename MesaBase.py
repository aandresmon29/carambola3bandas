import matplotlib.pyplot as plt
import matplotlib.patches as patches

## Carom Table Parameters
# This code defines a class for creating a carom table with specified dimensions and appearance.
class CarambolaTable():
    def __init__(self, height=302.8, width=152.4, band_thickness=5, system="standar"):
        self.height = height
        self.width = width 
        self.band_thickness = band_thickness
        self.system = system
        self.fig, self.ax = plt.subplots()
        self.systems = self.define_system()
        self.setup_table()

    # Table setup method
    # This method sets up the table with the specified dimensions and appearance.
    def setup_table(self):
        # Set the figure size and aspect ratio
        self.fig.patch.set_facecolor('white')
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-self.band_thickness, self.height + self.band_thickness)
        self.ax.set_ylim(-self.band_thickness, self.width + self.band_thickness)

        # Band rectangle
        band_rect = patches.Rectangle(
            (-self.band_thickness, -self.band_thickness),
            self.height + 2 * self.band_thickness,
            self.width + 2 * self.band_thickness,
            linewidth=0,
            facecolor='black',
            zorder=0
        )
        self.ax.add_patch(band_rect)

        # Draw the table surface
        table_surface = patches.Rectangle(
            (0, 0), self.height, self.width,
            linewidth=0,
            facecolor='lightgray',
            zorder=1
        )
        self.ax.add_patch(table_surface)
        
        # Draw the bands
        outer_border = patches.Rectangle(
            (-self.band_thickness, -self.band_thickness),
            self.height + 2 * self.band_thickness,
            self.width + 2 * self.band_thickness,
            linewidth=2,
            edgecolor='black',
            facecolor='none',
            zorder=2
        )
        self.ax.add_patch(outer_border)

    # Define the carom table system
    def define_system(self):
        return {
            "standar": {
                "bottom": [str(i) for i in range(9)],
                "top": [str(i) for i in range(9)],
                "left": [str(i) for i in range(5)],
                "right": [str(i) for i in range(5)],
            },
            "system_50": {
                "bottom": [str(i *5) for i in range(9)],
                "top": [str(i * 5) for i in range(9)],
                "left": [str(i * 10) for i in range(5)],
                "right": [str(i * 10) for i in range(5)],
            },
            "system_100": {
                "bottom": [str(i * 7) for i in range(9)],
                "top": [str(i * 7) for i in range(9)],
                "left": [str(i * 14) for i in range(5)],
                "right": [str(i * 14) for i in range(5)],
            }
        }

    # Draw diamonds with numbers on the carom table
    def draw_diamonds_with_numbers(self):
        labels = self.systems.get(self.system, self.systems["standar"])
        radius = 4
        # Bottom side (horizontal from 0 to 8)
        for i, label in enumerate(labels['bottom']):    
            x = i * self.height / 8
            self.ax.plot(x, 0 - self.band_thickness / 2, 'wo', markersize=radius)
            self.ax.text(x, -5, label, color='darkgreen', ha='center', va='top', fontsize=8)
        
        # Top side
        for i, label in enumerate(labels['top']):
            x = i * self.height / 8
            self.ax.plot(x, self.width + self.band_thickness / 2, 'wo', markersize=radius)
            self.ax.text(x, self.width + 5, label, color='darkgreen', ha='center', va='bottom', fontsize=8)

        # Left side (vertical from 0 to 4)
        for j, label in enumerate(labels['left']):
            y = j * self.width / 4
            self.ax.plot(0 - self.band_thickness / 2, y, 'wo', markersize=radius)
            self.ax.text(-5, y, label, color='darkgreen', ha='right', va='center', fontsize=8)

        # Right side
        for j, label in enumerate(labels['right']):
            y = j * self.width / 4
            self.ax.plot(self.height + self.band_thickness / 2, y, 'wo', markersize=radius)
            self.ax.text(self.height + 5, y, label, color='darkgreen', ha='left', va='center', fontsize=8)

    def draw_balls(self, white_ball, red_ball, yellow_ball):
        radius = 5  
        
        # Ensure balls are within the table bounds
        def clamp_ball(pos):
            x, y = pos
            x = max(radius, min(self.height - radius, x))
            y = max(radius, min(self.width - radius, y))
            return (x, y)

        # Clamp the positions of the balls to ensure they stay within the table
        white_ball = clamp_ball(white_ball)
        red_ball = clamp_ball(red_ball)
        yellow_ball = clamp_ball(yellow_ball)  

        # Draw the white ball
        self.ax.add_patch(patches.Circle(white_ball, radius, color='white', ec='black', zorder=3))
        # Draw the red ball
        self.ax.add_patch(patches.Circle(red_ball, radius, color='red', ec='black', zorder=3))
        # Draw the yellow ball
        self.ax.add_patch(patches.Circle(yellow_ball, radius, color='yellow', ec='black', zorder=3))

    # Draw the carom table with balls and diamonds
    def show_table(self, white_ball, red_ball, yellow_ball):
        self.draw_diamonds_with_numbers()
        self.draw_balls(white_ball, red_ball, yellow_ball)
        plt.axis('off')
        plt.show()

# Example usage
if __name__ == "__main__":
    table = CarambolaTable(system="system_50")
    table.show_table(white_ball=(0, 0), red_ball=(100, 100), yellow_ball=(150, 152.4))
