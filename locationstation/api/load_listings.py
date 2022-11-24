data = []

def load_data(filename):
    with open(filename, 'r') as reader:
        line = reader.readline()
        while line!='':
            data = tuple(line)
            print(data[3], end='')
            line = reader.readline()
            data = tuple(line)

if __name__=='__main__':
    load_data('listings.csv')
