import sys
import logging

def main():
    try:
        input_file = sys.argv[1]
    except IndexError:
        return logging.error('Students file does not exists')
    with open(input_file, 'r') as f:
        file_data = f.read()
        sys.stdout.write(',\n'.join(file_data.split('\n')))

if __name__ == '__main__':
    main()
