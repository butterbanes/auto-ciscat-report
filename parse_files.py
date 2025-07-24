import os


def get_curr_files(current_dir=os.getcwd()):
    return os.listdir(current_dir)

get_curr_files()
