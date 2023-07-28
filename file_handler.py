class File_handler:
    def __init__(self):
        pass

    def handle(self, lines, stock_data):
        # Iterate over lines in the file
        for self.__line in lines:
            # Format lines, remove the newline and split into a list
            self.__line = self.__line.replace("\n", "").split(" ")
