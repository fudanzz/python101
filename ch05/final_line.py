def final_line(file_name):
    file = open(file_name)
    lines = file.readlines()
    return lines[-1]

def get_final_line(filename):
    final_line = ''
    for line in open(filename):
        final_line = line
    return final_line

if __name__ == '__main__':
    print(final_line('../ch04/menu.py'))
    print(final_line('../ch04/rainfall.py'))
    print(get_final_line('../ch04/menu.py'))
    print(get_final_line('../ch04/rainfall.py'))