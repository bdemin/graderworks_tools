def separate_files(files):
    images = []
    folders = []

    for f_name in files:
        f_split = f_name.split('.')
        f_ext = f_split[-1]

        if f_ext == 'jpg':
            images.append(f_name)
        elif f_split[-1] == f_name:
            folders[student_name.lower()] = f_name
            folders.append(f_name)
        else:
            print('Ignoring', f_name)
    return images, folders

