import matplotlib.pyplot as plt

class Plot:

    x = list(())
    y = list(())

    def point(self, x, y):
        self.x.append(x)
        self.y.append(y)
        
    
    def show(self):
        plt.plot(self.x, self.y)
        plt.show()
