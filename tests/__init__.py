import io
import unittest
import unittest.mock
import json
import portfolio_manager

class test_portfolio_manager(unittest.TestCase):
    def create_stock_data_and_portfolio_manager(self):
        stock_data_file_path = "stock_data.json"
        stock_data_file = open(stock_data_file_path)
        self.__stocks = json.load(stock_data_file)["funds"]
        stock_data = {}
        stock_data_file.close()

        for stock in self.__stocks:
            stock_data[stock["name"]] = stock["stocks"]

        portfolio_manager_variable = portfolio_manager.Portfolio_manager(stock_data)

        return stock_data, portfolio_manager_variable


    def test_add_portfolio(self):
        stock_data, portfolio_manager = self.create_stock_data_and_portfolio_manager()

        fund_to_add = ["ICICI_PRU_NIFTY_NEXT_50_INDEX"]
        portfolio = portfolio_manager.add_portfolio(fund_to_add)

        self.assertEqual(portfolio["ICICI_PRU_NIFTY_NEXT_50_INDEX"],
                         stock_data["ICICI_PRU_NIFTY_NEXT_50_INDEX"])


    def test_is_fund_name_valid(self):
        stock_data, portfolio_manager = self.create_stock_data_and_portfolio_manager()

        fund_name_which_exists = "PARAG_PARIKH_CONSERVATIVE_HYBRID"
        fund_name_which_does_not_exist = "NIPPON_INDIA_PHARMA_FUND"

        self.assertTrue(portfolio_manager.is_fund_name_valid(fund_name_which_exists))
        self.assertFalse(portfolio_manager.is_fund_name_valid(fund_name_which_does_not_exist))


    def test_add_stock(self):
        stock_data, portfolio_manager = self.create_stock_data_and_portfolio_manager()

        stock_to_add = ["new", "blue", "microchips"]
        fund_name = "PARAG_PARIKH_CONSERVATIVE_HYBRID"
        correct_updated_stock_list = stock_data[fund_name]
        correct_updated_stock_list.append(stock_to_add)

        portfolio_manager.add_stock(fund_name, stock_to_add)

        self.assertEqual(stock_data[fund_name], correct_updated_stock_list)


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_overlap(self, mock_stdoud):
        stock_data, portfolio_manager = self.create_stock_data_and_portfolio_manager()

        fund_to_add = ["ICICI_PRU_NIFTY_NEXT_50_INDEX", "UTI_NIFTY_INDEX"]
        fund_to_check = "PARAG_PARIKH_CONSERVATIVE_HYBRID"

        portfolio_manager.add_portfolio(fund_to_add)
        portfolio_manager.calculate_overlap(fund_to_check)

        self.assertEqual(mock_stdoud.getvalue(),
                         "PARAG_PARIKH_CONSERVATIVE_HYBRID ICICI_PRU_NIFTY_NEXT_50_INDEX 17.24%\n"
                         "PARAG_PARIKH_CONSERVATIVE_HYBRID UTI_NIFTY_INDEX 24.59%\n")


if __name__ == '__main__':
    unittest.main()