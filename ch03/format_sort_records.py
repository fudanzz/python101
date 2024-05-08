PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

import operator

def format_sort_records(list_of_tuple):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted(list_of_tuple, key=operator.itemgetter(1, 0)):
        output.append(template.format(*person))
    return output

print('\n'.join(format_sort_records(PEOPLE)))