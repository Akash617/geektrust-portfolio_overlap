class Printer:
    def __init__(self):
        pass


    def print_overlap(self, fund, my_fund, overlap_percentage):
        print("{0} {1} {2:.2f}%".format(fund, my_fund, overlap_percentage))


    def fund_not_found(self):
        print("FUND_NOT_FOUND")
