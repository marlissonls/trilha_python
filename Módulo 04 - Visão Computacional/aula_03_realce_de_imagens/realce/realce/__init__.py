import enhance

__all__ = ['enhance']

if __name__ == '__main__':
    image_base_path: str = './img/elaineruido.png'
    select_gaussian_filter: list = [3, 5, 7, 9, 11]
    new_enhanced_img_path: str = enhance.new_image_enhancement(image_base_path, select_gaussian_filter[0])
    another_enhanced_img_path: str = enhance.new_image_enhancement(new_enhanced_img_path, select_gaussian_filter[0])