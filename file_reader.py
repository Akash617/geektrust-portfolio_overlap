import file_handler

class File_reader():
    def __init__(self):
        self.__stock_dict = {}


    def read_file(self, file, stock_data):
        self.__lines = file.readlines()
        self.parse_stock_data(stock_data)

        self.__file_handler = file_handler.File_handler()
        self.__file_handler.handle(self.__lines, self.__stock_dict)


    def parse_stock_data(self, stock_data):
        for data in stock_data:
            self.__stock_dict[data["name"]] = data["stocks"]
