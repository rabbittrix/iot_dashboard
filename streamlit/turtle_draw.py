import matplotlib.pyplot as plt

def draw_device_icon(device_type, color):
    plt.figure()
    plt.title(device_type)
    plt.gca().add_patch(plt.Circle((0.5, 0.5), 0.4, color=color))
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.axis('off')
    plt.show()