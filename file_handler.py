import portfolio_manager

class File_handler:
    def __init__(self):
        self.__portfolio = {}
        pass

    def handle(self, lines, stock_data):
        self.__portfolio_manager = portfolio_manager.Portfolio_manager(stock_data)

        # Iterate over lines in the file
        for self.__line in lines:
            # Format lines, remove the newline and split into a list
            self.__line = self.__line.replace("\n", "").split(" ")

            if self.__line[0] == "CURRENT_PORTFOLIO":
                self.__portfolio_manager.add_portfolio(self.__line[1:])

            if self.__line[0] == "CALCULATE_OVERLAP":
                self.__portfolio_manager.calculate_overlap(self.__line[1])

            if self.__line[0] == "ADD_STOCK":
                self.__portfolio_manager.add_stock(self.__line[1], self.__line[2:])
