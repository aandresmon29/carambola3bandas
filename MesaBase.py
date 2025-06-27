import matplotlib.pyplot as plt
import matplotlib.patches as patches

##Carom Table Parameters
#This code defines a class for creating a carom table with specified dimensions and appearance.
class CarambolaTable():
    def __init__(self, height=302.8, width=152.4, band_thickness=5):
        self.height = height
        self.width = width 
        self.band_thickness = band_thickness
        self.fig, self.ax = plt.subplots()
        self.setup_table()

    #Table setup method
    #This method sets up the table with the specified dimensions and appearance.
    def setup_table(self):
        #Set the figure size and aspect ratio
        self.fig.patch.set_facecolor('white')
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-self.band_thickness, self.height + self.band_thickness)
        self.ax.set_ylim(-self.band_thickness, self.width + self.band_thickness)

        #Band rectangle
        band_rect = patches.Rectangle(
            (-self.band_thickness, -self.band_thickness),
            self.height + 2 * self.band_thickness,
            self.width + 2 * self.band_thickness,
            linewidth=0,
            facecolor='black',
            zorder=0
        )
        self.ax.add_patch(band_rect)

        #Draw the table surface
        table_surface = patches.Rectangle(
            (0, 0), self.height, self.width,
            linewidth=0,
            facecolor='lightgray',
            zorder=1
        )
        self.ax.add_patch(table_surface)
        
        #Draw the bands
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

    #Draw diamonds with numbers on the carom table
    def draw_diamonds_with_numbers(self):
        #Bottom side (horizontal from 0 to 8)
        for i in range(9):
            x = i * self.height / 8
            self.ax.plot(x, 0 - self.band_thickness / 2, 'wo', markersize=4)
            self.ax.text(x, -5, f"{i}", color='darkgreen', ha='center', va='top', fontsize=8)

        # Left side (vertical from 0 to 4)
        for j in range(5):
            y = j * self.width / 4
            self.ax.plot(0 - self.band_thickness / 2, y, 'wo', markersize=4)
            self.ax.text(-5, y, f"{j}", color='darkgreen', ha='right', va='center', fontsize=8)

        # Top side
        for i in range(9):
            x = i * self.height / 8
            self.ax.plot(x, self.width + self.band_thickness / 2, 'wo', markersize=4)
            self.ax.text(x, self.width + 5, f"{i}", color='darkgreen', ha='center', va='bottom', fontsize=8)

        # Right side
        for j in range(5):
            y = j * self.width / 4
            self.ax.plot(self.height + self.band_thickness / 2, y, 'wo', markersize=4)
            self.ax.text(self.height + 5, y, f"{j}", color='darkgreen', ha='left', va='center', fontsize=8)

    def draw_balls(self, white_ball, red_ball, yellow_ball):
        # Draw the white ball
        self.ax.add_patch(patches.Circle(white_ball, 5, color='white', ec='black', zorder=3))
        # Draw the red ball
        self.ax.add_patch(patches.Circle(red_ball, 5, color='red', ec='black', zorder=3))
        # Draw the yellow ball
        self.ax.add_patch(patches.Circle(yellow_ball, 5, color='yellow', ec='black', zorder=3))

    #Draw the carom table with balls and diamonds
    def show_table(self, white_ball=(50, 50), red_ball=(100, 100), yellow_ball=(150, 150)):
        self.draw_diamonds_with_numbers()
        self.draw_balls(white_ball, red_ball, yellow_ball)
        plt.axis('off')
        plt.show()

# Example usage
if __name__ == "__main__":
    table = CarambolaTable()
    table.show_table(white_ball=(50, 50), red_ball=(100, 100), yellow_ball=(150, 150))
