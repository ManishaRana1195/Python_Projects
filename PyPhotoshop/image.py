import png
import numpy as np


class Image:
    def __init__(self, x_pixels=0, y_pixels=0, num_channels=0, filename=""):
        self.input_path = "images/input/"
        self.output_path = "images/output/"
        if x_pixels and y_pixels and num_channels:
            self.x_pixels = x_pixels
            self.y_pixels = y_pixels
            self.num_channels = self.num_channels  # number of channels(R, G, B)
            self.image = np.zeros((x_pixels, y_pixels, num_channels))
        elif filename:
            self.image = self.read(filename)
            print(self.image.shape)
            self.x_pixels, self.y_pixels, self.num_channels = self.image.shape
        else:
            raise ValueError("You need to either specify a filename OR the dimensions of the image ")

    def read(self, filename, gamma=2.2):
        # convert image file into numpy array
        # image format - (width, height, stream of rows of pixels, info)
        image = png.Reader(self.input_path + filename).asFloat()
        # convert pixel row data into np array it is just stream/generator
        temp = np.array(list(image[2]))
        # convert 2D data into 3D having values for R,G,B colors
        temp.resize(image[1], image[0], 3)
        # Most images are not stored linearly. They are stored in a gamma-encoded format.
        # So gamma decoding  the values
        temp = temp ** gamma
        return temp

    def write(self, filename, gamma=2.2):
        temp = np.clip(self.image, 0, 1)
        y, x = temp.shape[0], temp.shape[1]
        temp = temp.reshape(y, x * 3)
        writer = png.Writer(x, y)
        with open(self.output_path+filename, "wb") as f: 
            writer.write(f, 255*(temp**(1/gamma)))
        self.image.reshape(y, x, 3) 

