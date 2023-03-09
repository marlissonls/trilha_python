import matplotlib.pyplot as plt
import cv2
import numpy as np

__all__ = ['read_image', 'write_image', 'enhance_image', 'plot_image_configs', 'plot_display', 'new_image_enhancement']

def read_image(image_path_name: str) -> np.ndarray:
    """ 
    Returns a matrix of an image.
    
        image_path_name: a string of the form './img/imgName.imgExtension' indicating the path of an image.
    """
    return cv2.imread(image_path_name)

def write_image(img: np.ndarray, image_path_name: str) -> str:
    """ 
    Writes a matrix of an image to an image file and returns the name of the image file written.

        img: a matrix of an image of type ndarray.\n
        image_path_name: a string of the form './img/imgName.imgExtension' indicating the path of an image.
    """
    new_img_path: str = set_new_image_path(image_path_name)
    cv2.imwrite(new_img_path, img)
    return new_img_path

def set_new_image_path(image_path_name: str) -> str:
    """
    Generates and returns an image path of type string of the form './img/imgName.imgExtension'.

        image_path_name: a string of the form './img/imgName.imgExtension' indicating the path of an image.
    """
    img_path_splited: list = image_path_name.split('/')
    img_name_splited: list = img_path_splited[2].split('.')
    path: str = img_path_splited[1]
    name: str = img_name_splited[0]
    extension: str = img_name_splited[1]
    return f'./{path}/enhanced_{name}.{extension}'

def enhance_image(image: np.ndarray, gaussian_filter: int) -> np.ndarray:
    """
    Returns an enhanced matrix of an image.

        image: a base image matrix.\n
        gaussian_filter: a number in the list: [3, 5, 7, 9, 11].
    """
    return np.vstack([np.hstack([cv2.medianBlur(image, gaussian_filter)])])

def plot_image_configs(image: np.ndarray, title: str) -> None:
    """
    Sets the plotting of a matrix of an image.

        image: matrix of an image.\n
        title: string that sets the title of the plot.
    """
    plt.figure(figsize=(4,4))
    plt.title(title)
    plt.imshow(image)

def plot_display() -> None:
    """
    Display the plot of images.
    """
    plt.show()

def new_image_enhancement(path: str, gaussian_filter: int) -> str:
    """
    Generates a new enhanced image file from a base image file and returns the path of the new image file.

        path: a string of the form './img/imgName.imgExtension' indicating the path of an image.\n
        gaussian_filter: a number in the list: [3, 5, 7, 9, 11].
    """
    img_path: str = path
    img_matrix: np.ndarray = read_image(img_path)
    enhanced_img_matrix: np.ndarray = enhance_image(img_matrix, gaussian_filter)
    enhanced_img_path: str = write_image(enhanced_img_matrix, img_path)

    plot_image_configs(img_matrix, img_path)
    plot_image_configs(enhanced_img_matrix, enhanced_img_path)
    plot_display()
    return enhanced_img_path

# see the __init__.py file with this entry point ./__init__.py
""" if __name__ == '__main__':
    image_base_path: str = './img/elaineruido.png'
    select_gaussian_filter: list = [3, 5, 7, 9, 11]
    new_enhanced_img_path: str = new_image_enhancement(image_base_path, select_gaussian_filter[0])
    another_enhanced_img_path: str = new_image_enhancement(new_enhanced_img_path, select_gaussian_filter[0]) """