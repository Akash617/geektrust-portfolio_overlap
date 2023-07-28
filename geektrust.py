from sys import argv
import json
import file_reader


def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    stock_data_file_path = "stock_data.json"

    # Open the files and send it to the file reader
    input_file = open(file_path, 'r')
    stock_data_file = open(stock_data_file_path)
    stock_data = json.load(stock_data_file)["funds"]

    file = file_reader.File_reader()
    file.read_file(input_file, stock_data)


if __name__ == "__main__":
    main()
