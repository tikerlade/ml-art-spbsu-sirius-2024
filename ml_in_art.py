import matplotlib.pyplot as plt

def imshow(img, title):
    """
    Plots image with title
    """
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')
    plt.show()
