# Stock-Tracker


S.A.M. - Stock Analyzer Machine is the result of a class project for CEIS150 - Object Oriented Programming

Project Info:

    Author: Nicholas Allen
    Date:   Oct - Dec 2022
    Reason: To track the values of stock investments
        For:    DeVry University
        With:   Professor Lieberman
        During: November Session
        Class:  CEIS150
        GitHub: https://github.com/NicholasAllen1981/Stock-Tracker


Week 1 (Module 1)

    Setting Up IDE and getting ready

Week 2 (Module 2)

    Created stock_class.py
        Stock(symbol as string, name as string, shares as float)
            Stock.add_data(stock_data)
                stock_data takes form of date,price,shares with NO spaces
                date is formatted as mm/dd/yy
                price is formated as floats
                shares is formated as float
Week 3 (Module 3)
    
    Using sample menu code stock_menu_v3.py
        Connected sample menu code in stock_menu_v3.py to classes in stock_class.py.
        Created menu styling system
        Added code to add stock
        Added code to delete stock
        Added code to list stock
        Added code to add daily stock data
        Fixed Option 0 Exit to correctly exit the program
        Added menu option 9 About S.A.M.
            Added code to create a About screen
Week 4 (Module 4)
    
    Created account_class.py
        Retirement_Account(balance as float, number as float)
            Traditional(balance as float, number as float)
                Traditional.add_stock(stock_data)
                    stock_data as date,price,shares seperated with , with NO spaces
                    date as mm/dd/yy,price as float,shares as float
            Robo(balance as float, number as float, years as float)
                Returns the value of the return on investment based on the balance and  number of years
Week 5 (Module 5)
    
    Using stock_menu_v3.py
        Added code to display_chart(stock_list)
        Added code to display_stock_chart(stock_list)
            Created chart using matplotlib and data added with add daily data option
Week 6 (Module 6)
    


            

