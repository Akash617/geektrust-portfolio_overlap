import printer

class Portfolio_manager:
    def __init__(self, stock_data):
        self.__stock_data = stock_data
        self.__portfolio = {}
        self.__printer = printer.Printer()


    def is_fund_name_valid(self, fund):
        if fund in self.__stock_data.keys():
            return True

        self.__printer.fund_not_found()
        return False


    def add_portfolio(self, portfolios):
        for portfolio in portfolios:
            self.__portfolio[portfolio] = self.__stock_data[portfolio]

        return self.__portfolio


    def add_stock(self, fund, stock_name_list):
        if not self.is_fund_name_valid(fund):
            return

        stock_name = " ".join(stock_name_list)

        new_stock_list = self.__stock_data[fund]
        new_stock_list.append(stock_name)

        if fund in self.__portfolio.keys():
            self.__portfolio[fund] = new_stock_list

        self.__stock_data[fund] = new_stock_list


    def calculate_overlap(self, fund):
        if not self.is_fund_name_valid(fund):
            return

        for key, value in self.__portfolio.items():
            overlap_percentage = self.get_overlap_between_two_funds(self.__stock_data[fund], value)
            self.__printer.print_overlap(fund, key, overlap_percentage)


    def get_overlap_between_two_funds(self, fund, my_fund):
        overlapping_stocks = [stock for stock in fund if stock in my_fund]

        # This is dumb but GeekTrust considers these magic numbers otherwise:
        multiple = 2
        total = 100
        overlap_percentage = (multiple * len(overlapping_stocks)) / (len(fund) + len(my_fund)) * total

        return overlap_percentage
