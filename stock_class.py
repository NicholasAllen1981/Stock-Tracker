"""
    Author: Nicholas Allen
    Date: 11.2.2022
    Purpose: CEIS150 - Track stock by symbol
"""
# Stock Class
#  Parent Class
##  Accepts symbol, name, and shares
###   stock = Stock(symbol, name, shares)
###     Creates Stock object
###   functions: stock.add_data(stock_data)
####    Adds stock object to list
class Stock():
    def __init__(self, symbol, name, shares):
        ## Check for empty symbol string
        if symbol:
            self.symbol = symbol
        else:
            print("\n***Error: Ticker symbol missing")
        ## Check for empty symbol string
        if name:
            self.name = name
        else:
            print("\n***Error: Company name missing")
        ## Check for negative shares
        if shares >= 0:
            self.shares = shares
        else:
            print("\n***Error: Negative amount of shares.\nSetting to 0")
            self.shares = 0
        self.DataList = [] # Daily stock data list
    # Stock function to add stock
    def add_data(self, stock_data):
        self.DataList.append(stock_data)
     
   
# DailyData class
#  Parent Class
##  Accepts date, close, and volume
###   dailyData = DailyData(date, close, volume)
###     Creates Stock object
class DailyData():
    def __init__(self, date, close, volume):
        import datetime
        today = datetime.date.today()
        if date:
            self.date = date
        else:
            print("\n***Error: Date missing, setting today's date")
            self.date = today
            
        if close >= 0.00:
            self.close = close
        else:
            print("\n***Error: Not a positive dollar amount.\nSetting the closing price to 0.01")
            self.close = 0.01
        if volume >= 0.00:
            self.volume = volume
        else:
            print("\n***Error: Not a positive volume.\nSetting the volume to 1.")
            self.volume = 1.00
            



# Unit Test - Do Not Change Code Below This Line *** *** *** *** *** *** *** *** ***
# main() is used for unit testing only. It will run when stock_class.py is run.
# Run this to test your class code. Once you have eliminated all errors, you are
# ready to continue with the next part of the project.

def main():
    import datetime
    error_count = 0
    error_list = []
    print("Unit Testing Starting---")
    # Test Add Stock
    print("Testing Add Stock...",end="")
    try:
        testStock = Stock("TEST","Test Company",100)
        print("Successful!")
    except:
        print("***Adding Stock Failed!")
        error_count = error_count+1
        error_list.append("Stock Constructor Error")
    # Test Change Symbol
    print("Test Change Symbol...",end="")
    try:
        testStock.symbol = "NEWTEST"
        if testStock.symbol == "NEWTEST":
            print("Successful!")
        else:
            print("***ERROR! Symbol change unsuccessful.")
            error_count = error_count+1
            error_list.append("Symbol Change Error")
    except:
        print("***ERROR! Symbol change failed.")
        error_count = error_count+1
        error_list.append("Symbol Change Failure")
    print("Test Change Name...",end="")
    try:
        testStock.name = "New Test Company"
        if testStock.name == "New Test Company":
            print("Successful!")
        else:
            print("***ERROR! Name change unsuccessful.")
            error_count = error_count+1
            error_list.append("Name Change Error")
    except:
        print("***ERROR! Name change failed.")
        error_count = error_count+1
        error_list.append("Name Change Failure")
        print("Test Change Name...",end="")
    try:
        testStock.shares = 2000
        if testStock.shares == 2000:
            print("Successful!")
        else:
            print("***ERROR! Shares change unsuccessful.")
            error_count = error_count+1
            error_list.append("Shares Change Error")
    except:
        print("***ERROR! Shares change failed.")
        error_count = error_count+1
        error_list.append("Shares Change Failure")
        

    # Test add daily data
    print("Creating daily stock data...",end="")
    daily_data_error = False
    try:
        dayData = DailyData("1/1/20",float(14.50),float(100000))
        testStock.add_data(dayData)
        today = datetime.date.today()
        if testStock.DataList[0].date != "1/1/20":
            if testStock.DataList[0].date != today:
                error_count = error_count + 1
                daily_data_error = True
                error_list.append("Add Daily Data - Problem with Date")
        if testStock.DataList[0].close != 14.50:
            error_count = error_count + 1
            daily_data_error = True
            error_list.append("Add Daily Data - Problem with Closing Price")
        if testStock.DataList[0].volume != 100000:
            error_count = error_count + 1
            daily_data_error = True
            error_list.append("Add Daily Data - Problem with Volume")  
    except:
        print("***ERROR! Add daily data failed.")
        error_count = error_count + 1
        error_list.append("Add daily data Failure!")
        daily_data_error = True
    if daily_data_error == True:
        print("***ERROR! Creating daily data failed.")
    else:
        print("Successful!")
    
    if (error_count) == 0:
        print("Congratulations - All Tests Passed")
    else:
        print("-=== Problem List - Please Fix ===-")
        for em in error_list:
            print(em)
    print("Goodbye")

# Program Starts Here
if __name__ == "__main__":
    # run unit testing only if run as a stand-alone script
    main()
