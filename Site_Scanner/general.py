import os

def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def write_file(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()