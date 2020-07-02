import os
import shutil

from get_root import root


def separate_files(files):
    # Separate between images and folders located inside files
    
    images = []
    folders = dict()

    for f_name in files:
        f_split = f_name.split('.')
        f_ext = f_split[-1]

        if f_ext == 'jpg':
            images.append(f_name)
        elif f_split[-1] == f_name:
            student_name = f_name.split('_')[0]
            folders[student_name.lower()] = f_name
        else:
            print('Ignoring', f_name)
    return images, folders

def image_handler(files):
    # Move all SolidWorks screenshots into corresponding student folders

    images, folders = separate_files(files)

    for image in images:
        student_name = image.split('_')[0]
        if student_name in folders:
            destination = folders[student_name]
            shutil.move(image, destination)
            print('Moving', image, 'to', destination)
        else:
            print(image, 'has no suitable folder')

def move_images():
    files = os.listdir(root)
    image_handler(files)

if __name__ == '__main__':
    move_images()
