import glob
import json
import os

def parse_json_file(dirname):
    json_files = glob.glob(os.path.join(dirname, '*.json'))
    math = []
    literature = []
    science = []

    for json_file in json_files:
        with open(json_file) as file:
            for data in json.load(file):
                math.append(data['math'])
                literature.append(data['literature'])
                science.append(data['science'])
        print(f'{json_file}/n')
        print(f'Math: min {min(math)} , max {max(math)} , avg {sum(math)/len(math)}')
        print(f'Literature: min {min(literature)} , max {max(literature)} , avg {sum(literature)/len(literature)}')
        print(f'Science: min {min(science)} , max {max(science)} , avg {sum(science)/len(science)}')

        
if __name__ == '__main__':
    parse_json_file('./data/json')