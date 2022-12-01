# -*- coding: utf-8 -*-
'''#
# Created on Fri Nov 11 2022
# Stock Analyzing Machine (SAM)
#
# @author: Nicholas Allen (D40094263)
# @puropse: Analyze stock information
# @date: 11/11/22
# 
# ╭ ╮ ╯ ╰ │ ─ ├ ┤ ┴ ┬ ┼
# '''

# Imports
from datetime import datetime
from stock_class import Stock, DailyData
from account_class import  Traditional, Robo
import matplotlib.pyplot as plt
import csv
import os
from os import get_terminal_size
'''  --- Menu styling ---
------------------------------

'''
# Get either width or length of terminal.
def get_term_size(w_or_l):
    term_size = get_terminal_size()
    if w_or_l == "w":
        if term_size.columns % 2 == 0:
            return term_size.columns - 4
        else:
            return term_size.columns - 5
    elif w_or_l == "l":
        return term_size.lines
# Print a unattached header with border   
def print_header(program_name="S.A.M. - Stock Analizing Machine", menu_name="-- Main Menu --"):
    # Start Menu Header
    print_H_bar("top")
    print_at_middle(program_name) 
    print_H_bar("middle")
    print_at_middle(menu_name)
    print_H_bar("bottom")
# Print a line between borders centered on the line
def print_at_middle(str_to_print):
    term_len = 90 # get_term_size("w")
    term_mid = term_len // 2
    str_len = len(str_to_print)
    str_mid = str_len // 2
    new_mid = (term_mid - str_mid) - 1
    if str_len % 2 != 0:
        offset_mid = new_mid - 1
        print("│" + (" " * new_mid) + str_to_print + (" " * offset_mid) + "│")
    else:
        print("│" + (" " * new_mid) + str_to_print + (" " * new_mid) + "│")
# Print a line between borders justified left on the line
def print_at_left(str_to_print):
    term_len = 90 # get_term_size("w")
    str_len = len(str_to_print)
    new_len = (term_len - str_len) - 3
    print("│ " + str_to_print + (" " * new_len) + "│")
# Pint a ticker box with borders to house stock symbols. No box is displayed if no symbols are added
def print_ticker(stock_list):
    if len(stock_list) > 0:
        print_H_bar("top")
        list_stocks = ""
        for stock in stock_list:
            list_stocks = list_stocks + stock.symbol + " "
        print_at_middle(list_stocks)
        print_H_bar("bottom")
# Print data into columns with borders
def print_col_data(str_to_print, num_of_columns, column_num):
    term_len = 90
    term_new_len = term_len // num_of_columns
    str_len = len(str(str_to_print))
    
    new_len = ((term_new_len - str_len) - 1) // 2
    # Check if the str is a even or odd number
    if str_len % 2 != 0: # if it is odd
        sec_half = new_len
    else:
        sec_half = new_len + 1
    # Check position of column
    if column_num == 1: # First column
        print("│" + (" " * new_len) + str(str_to_print) + (" " * sec_half) + "│", end="")
    elif (column_num < num_of_columns) and (column_num > 1): # Middle column
        print((" " * new_len) + str(str_to_print) + (" " * sec_half) + "│", end="")
    elif column_num == num_of_columns: # Last column
        print((" " * (new_len + 1)) + str(str_to_print) + (" " * sec_half) + "│")
# Print Headers for columns with borders
def print_col_header(str_to_print, num_of_columns, column_num):
    term_len = 90 # get_term_size("w")
    term_new_len = term_len // num_of_columns
    str_len = len(str_to_print)
    new_len = ((term_new_len - str_len) - 1) // 2
    if column_num == 1:
        print("│" + (" " * new_len) + str_to_print + (" " * new_len) + "│", end="")
    elif column_num == num_of_columns:
        print((" " * (new_len + 1)) + str_to_print + (" " * new_len) + "│")
    elif (column_num < num_of_columns) and (column_num > 1):
        print((" " * new_len) + str_to_print + (" " * new_len) + "│", end="")
# Print horazontal bar of specified length with column border attachments
def print_H_col_bar(location, num_of_columns):
    term_len = 90 # get_term_size("w")
    term_new_len = term_len // num_of_columns
    #str_len = len(str_to_print)
    term_len = term_new_len - 1
    column_number = 0
    while column_number <= num_of_columns:
        column_number += 1
        # First Column
        if column_number == 1:
            if location.lower() == "top":
                print("╭" + ("─" * term_len + "┬"), end="")
            elif location.lower() == "middle":
                print("├" + ("─" * term_len + "│"), end="")
            elif location.lower() == "bottom":
                print("├" + ("─" * term_len + "┼"), end="")
            elif location.lower() == "final":
                print("╰" + "─" * term_len + "┴", end="")
        # Middle Columns
        elif (column_number < num_of_columns) and (column_number > 1):
            if location.lower() == "top":
                print(("─" * term_len + "┬"), end="")
            elif location.lower() == "middle":
                print(("─" * term_len + "┼"), end="")
            elif location.lower() == "bottom":
                print(("─" * term_len + "┼"), end="")   
            elif location.lower() == "final":
                print(("─" * term_len + "┴"), end="")
        # Last Column
        elif column_number == num_of_columns:
            if location.lower() == "top":
                print(("─" * term_len + "─╮"))
            elif location.lower() == "middle":
                print(("─" * term_len + "─┤"))
            elif location.lower() == "bottom":
                print(("─" * term_len + "─┤"))
            elif location.lower() == "final":
                print("─" * term_len + "─╯")
# Print horazontal bar of specified length
def print_H_bar(location):
    term_len = 90 # get_term_size("w")
    if location.lower() == "top":
        print("╭" + "─" * (term_len - 2) + "╮")
    elif location.lower() == "middle":
        print("├" + "─" * (term_len - 2) + "┤")
    elif location.lower() == "bottom":
        print("╰" + "─" * (term_len - 2) + "╯\n")
# Clear Screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('Clear')

''' ---  MAIN PROGRAM  ---   
# -------------------------- 
'''     
# Add stock   
def add_stock(stock_list):
    clear_screen()
    option = ""
    loop_count = 0
    while option != "0":
        print_header("S.A.M. - Stock Analizing Machine", "-- Add Stock --")
        print_ticker(stock_list)
        while loop_count <= 2:
            if loop_count == 0:
                symbol = input("\nPlease input stock symbol: ").upper()
                loop_count += 1
            elif loop_count == 1:
                name = input("Please input company Name: ").capitalize()
                loop_count += 1
            elif loop_count == 2:
                shares = float(input("Please input the number of shares: "))
                loop_count += 1
        new_stock = Stock(symbol, name, shares)
        stock_list.append(new_stock)     
        print("\n** * ** Successfully Added Stock Information ** * **")
        again = input("\nWould you like to add another? (Y/n)")
        if (again.lower() == "y") or (again == ""):
            add_stock(stock_list)
        else:
            main_menu(stock_list)
# Remove stock and all daily data
def delete_stock(stock_list):
    clear_screen()
    print_header("S.A.M. - Stock Analizing Machine", "-- Delete Stock --")
    print_ticker(stock_list)
    symbol = input("Choose the stock symbol to remove (Example: MSFT, IBM): ").upper()
    found = False
    i = 0
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            stock_list.pop(i)
        i += 1
    if found == True:
        print("\n** * ** Successfully Removed Stock " + symbol + " ** * **")
    else:
        print("\n** * ** ERROR: Stock Symbol Not Found ** * **")
        print("\n** * **  Spelling must match EXACTLY  ** * **")
    _ = input("\nPress Enter to continue")
# List stocks being tracked
def list_stocks(stock_list):
    # Clear the screen
    clear_screen()
    # Print the Header
    print_header("S.A.M. - Stock Analizing Maching", "-- Stock List --")
    print_ticker(stock_list)
    # Start Main Menu
    print_H_col_bar("top", 3)
    print_col_data("Ticker Symbol", 3, 1)
    print_col_data("Company Name", 3, 2)
    print_col_data("Qnty. Shares", 3, 3)
    print_H_col_bar("bottom", 3)
    x = 0
    for stock in stock_list:
    
        my_stock = stock_list[x]
        print_col_data(my_stock.symbol, 3, 1)
        print_col_data(my_stock.name, 3, 2)
        print_col_data(my_stock.shares, 3, 3)
        x += 1
    print_H_col_bar("final", 3)
    _ = input("Please press Enter to continue.")
    if _:
        main_menu(stock_list)
# Add Daily Stock Data
def add_stock_data(stock_list):
    clear_screen()
    print_header("S.A.M. - Stock Analizing Machine","-- Add Daily Stock Data --")
    print_ticker(stock_list)
    symbol = input("Choose Stock to Add Daily Data to?: ").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        clear_screen()
        print_header("S.A.M. - Stock Analizing Machine","-- Add Daily Stock Data --")
        print_ticker(stock_list)
        print_H_bar("top")
        print_at_middle("Adding data for: " + symbol)
        print_H_bar("middle")
        print_at_left("Enter Data Separated by Commas - Do Not use Spaces")
        print_at_left("Enter a Blank Line to Quit")
        print_at_left("Enter Date,Price,Volume")
        print_H_bar("middle")
        print_at_middle("Example: 8/28/20,47.85,10550")
        print_H_bar("bottom")
        data = input("Enter Date,Price,Volume: ")
        while data != "":
            date, price, volume = data.split(",")
            daily_data = DailyData(date,float(price),float(volume))
          
            current_stock.add_data(daily_data)
            data = input("Enter Date,Price,Volume: ")
        print("Date Entry Complete")
    else:
        print("Symbol Not Found ***")
    _ = input("Press Enter to Continue ***")
# create investment
def investment_type(stock_list):
    clear_screen()
    print_header("S.A.M. - Stock Analizing Machine","-- Investment Account --")
    print_ticker(stock_list)
    balance = float(input("\nWhat is your initial balance: "))
    number = input("\nWhat is your account number: ")
    acct= input("\nDo you want a Traditional (t) or Robo (r) account: ")
    if acct.lower() == "r":
        years = float(input("\nHow many years until retirement: "))
        robo_acct = Robo(balance, number, years)
        print("\nYour investment return is ",robo_acct.investment_return())
        print("\n\n")
        _ = input("Press Enter to continue.")
    elif acct.lower() == "t":
        trad_acct = Traditional(balance, number)
        temp_list=[]
        print_header("S.A.M. - Stock Analizing Machine","-- Traditional Investment Account --")
        print("\nChoose stocks from the list below: ")
        while True:
            print_ticker(stock_list)
            symbol = input("\nWhich stock do you want to purchase, 0 to quit: ").upper()
            if symbol =="0":
                break
            shares = float(input("\nHow many shares do you want to buy?: "))
            found = False
            for stock in stock_list:
              if stock.symbol == symbol:
                  found = True
                  current_stock = stock
            if found == True:
                current_stock.shares += shares 
                temp_list.append(current_stock)
                print("\nBought ",shares,"of",symbol)
            else:
                print("\nSymbol Not Found ***")
        trad_acct.add_stock(temp_list)
        _ = input("Press Enter to continue.")
# Function to create stock chart
def display_stock_chart(stock_list,symbol):
    date = []
    price = []
    volume = []
    company = ""
    for stock in stock_list:
        if stock.symbol == symbol:
            company = stock.name
            for dailyData in stock.DataList:
                date.append(dailyData.date)
                price.append(dailyData.close)
                volume.append(dailyData.volume)
    plt.plot(date, price)
    plt.xlabel("date")
    plt.ylabel("Price")
    plt.title(company)
    plt.show()
# Display Chart
def display_chart(stock_list):
    symbol = ""
    print("Stock List: [", end ="")
    for stock in stock_list:
        print(stock.symbol + " ", end = "")
    print("]")
    symbol = input("Stock Symbol.").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        display_stock_chart(stock_list, symbol)
    else:
        print("ERROR: " + symbol + " was not found.")
    _ = input("Press Enter to continue.")
# Get price and volume history from Yahoo! Finance using CSV import.
def import_stock_csv(stock_list):
    clear_screen()
    print_header("S.A.M. - Stock Analizing Machine","-- Add Daily Stock Data --")
    print_ticker(stock_list)
    symbol = input("Please Choose Stock Symbol from the List Above: ").upper()
    fname = input("Please input file name:")
    for stock in stock_list:
        if stock.symbol == symbol:
            with open(fname, newline='') as stockdata:
                datareader = csv.reader(stockdata, delimiter=",")
                next(datareader)
                for row in datareader:
                    daily_data = DailyData(str(row[0]),float(row[4]),float(row[6]))
                    stock.add_data(daily_data)
    display_report(stock_list)
                
# Display Report
def display_report(stock_list):
    clear_screen()
    print_header("S.A.M. - Stock Analizing Machine","-- Add Daily Stock Data --")

    for stock in stock_list:
        count = 0
        price_total = 0
        volume_total = 0
        lowPrice = 999999.99
        highPrice = 0
        lowVolume = 999999999999
        highVolume = 0
        priceChange = 0
        print_H_bar("top")
        print_at_middle("Report for: " + stock.name)
        print_at_middle("Ticker Symbol: " + stock.symbol)
        print_at_middle("Shares: " + str(stock.shares))
        print_H_bar("middle")
        for daily_data in stock.DataList:
            count += 1
            if count == 1:
                startPrice = daily_data.close
            elif count == len(stock.DataList) - 1:
                endPrice = daily_data.close
                priceChange = endPrice - startPrice
            price_total = price_total + daily_data.close
            volume_total = volume_total + daily_data.volume
            if daily_data.close < lowPrice:
                lowPrice = daily_data.close
            if daily_data.close > highPrice:
                highPrice = daily_data.close
            if daily_data.volume < lowVolume:
                lowVolume = daily_data.volume
            if daily_data.volume > highVolume:
                highVolume = daily_data.volume
            
        
        if count > 0:
            low_price = "Low Price: ${:,.2f}".format(lowPrice)
            high_price = "High Price: ${:,.2f}".format(highPrice)
            average_price = "Average Price: ${:,.2f}".format(price_total / count )
            low_volume = "Low Volume: " + str(lowVolume)
            high_volume = "High Volume: " + str(highVolume)
            average_volume = "Average Volume: " + str(volume_total / count)
            change_price = "Change in Price: ${:,.2f}".format(priceChange)
            profit_loss = "Profit / Loss: ${:,.2f}".format(priceChange * stock.shares)
            print_at_left(str(low_price))
            print_at_left(str(high_price))
            print_at_left(str(average_price))
            print_at_left(str(low_volume))
            print_at_left(str(high_volume))
            print_at_left(str(average_volume))
            print_at_left(str(change_price))
            print_at_left(str(profit_loss))
        else:
            print_at_middle("NO DAILY HISTORY")
        print_H_bar("bottom")
    print_H_bar("top")
    print_at_middle("-- REPORT COMPLETE --")
    print_H_bar("bottom")
    _ = input("Press Enter to continue.")
# About screen
def about_SAM(stock_list):
    clear_screen()
    print_header("S.A.M. - Stock Analyzine Machine", "-- About --")
    print_ticker(stock_list)
    print_H_bar("top")
    print_at_middle("S.A.M. - Stock Analyzing Machine")
    print_at_middle("Version 0.4 (alpha4)")
    print_at_middle("")
    print_at_middle("Created for the CEIS150 course at DeVry University")
    print_at_middle("With Professor Lieberman")
    print_at_middle("")
    print_at_middle("Author: Nicholas Allen")
    print_at_middle("Version: 0.4")
    print_at_middle("")
    print_H_bar("bottom")
    _ = input("Press enter to continue.")
# Main Menu
def main_menu(stock_list):
    option = ""
    
    while True:
        # ╔╗╚╝═║╢─╟

        # Clear the screen
        clear_screen()
        print_header()
        print_ticker(stock_list)
        # Start Main Menu
        print_H_bar("top")
        print_at_left("- 1 - Add Stock")
        print_at_left("- 2 - Delete Stock")
        print_at_left("- 3 - List Stock")
        print_at_left("- 4 - Add Daily Stock Data")
        print_at_left("- 5 - Show Chart")
        print_at_left("- 6 - Investor Type")
        print_at_left("- 7 - Load Data")
        print_H_bar("middle")
        print_at_left("- 9 - About S.A.M.")
        print_at_left("- 0 - Exit")
        # End Main Menu
        # Start Menu Footer
        print_H_bar("Bottom")
        # End Menu Footer
        

        option = input("Enter Menu Option: ")
        
        

        if option =="0":
            print("Goodbye")
            exit()
        
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            delete_stock(stock_list)
        elif option == "3":
            list_stocks(stock_list)
        elif option == "4":
           add_stock_data(stock_list) 
        elif option == "5":
            display_chart(stock_list)
        elif option == "6":
            investment_type(stock_list)
        elif option == "7":
            import_stock_csv(stock_list)
        elif option == "9":
            about_SAM(stock_list)
        else:
            
            print("Goodbye")
# Begin program
def main():
    stock_list = []
    main_menu(stock_list)
# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()