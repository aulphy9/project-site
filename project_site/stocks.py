#class to gather and store information about specifc stocks
class Stonks:
    def __init__(self,name,ticker,price,PE_ratio,beta,yearly_change,held_by_institutions,shares_short,dividend):
        """
        Initilizes a stock object with critical information about defined stock
        Use: stock = Stonks()
        Use in conjunctionwith web scrap ing tool
        """
        if beta != 'N/A':
            self.beta = float(beta)
        else:
            self.beta = beta
        self.name = str(name)
        self.ticker = str(ticker)
        self.price = price
        self.PE_ratio = float(PE_ratio)
        self.yearly_change = str(yearly_change)
        self.held_by_institutions = str(held_by_institutions)
        self.shares_short = float(shares_short)
        self.dividend = dividend

    def __str__(self):
        """
        Prints off basic info about instance of a stock
        Use: str(stock)
        """
        output = ("Name: {}\nPrice: ${}\nTicker: {}".format(self.name,self.price,self.ticker))
        return output
    
    def volatility(self):
        """
        Uses the 5 year beta ratio to determine how risky/volatile
        said stock is compared to the relevant market.
        Use: risk = stock.volatility()
        """
        status = None
        if self.beta != "N/A":
            print("This function uses the beta value of a stock to determine volatility of the stock.")
            status = None
            if self.beta == 1.0:
                status = 'Systematic risk: volatility correlates with current market, price fluctuates normally.'
            elif self.beta < 1.0:
                status = 'No  risk: volatility is less than what correlates with the current market, price fluctuates less.'
            elif self.beta > 1.0:
                status = 'Moderate risk: price is more volatile compared to others in the market, price fluctuates more.'
            else:
                if self.beta < 1.0:
                    status = '''Special case: price activity is the opposite of what happens in the market, I.E market prices go up,
                    stock goes down'''
        return status

    def price_to_earnings(self):
        """
        Explains how to use this type of ratio and what it indicates about a stock.
        Use: stock.price_to_earnings()
        """
        print("The price to earnings ratio relates a the stocks price to its earnings per share")
        print("If you want to calculate this yourself you do price per share/ earnings per share")
        print("In laymens terms, this is a quick check to see if a stock price is overvalued or undervalued")
        print(""""In this function we will be using the forward price to earnings, which means we use the predicted earnings
        per share over the next 12 months.""")
        ratio = None
        if self.PE_ratio > 25.00 and self.PE_ratio < 30.00:
            ratio = 'Slightly overvalued'
        elif self.PE_ratio < 25.00 and self.PE_ratio > 20.00:
            ratio = 'Slightly undervalued'
        elif self.PE_ratio > 30.00:
            ratio = "Don't buy"
        else:
            ratio = 'Buy'
        return ratio

    def has_dividend(self):
        """
        Determines whether or not a stock has a dividend.
        Use: stock.has_dividend()
        """
        if self.dividend != 'N/A':
            return True
        else:
            return False

    def short_squeeze_status(self):
        """
        In light of recent stock market events, this will be included so 
        you don't buy a stock Wall Street investment banking firms are
        betting against.
        Use: stock.short_squeeze_status()
        """
        if self.shares_short >= 40.00:
            status = 'DO NOT BUY THIS STOCK'
        else:
            status = 'In the clear'
        return status 
    
    
    def classification(self):
        """
        Uses the functions above and certain aspects of a stock
        to determine what category a stock fits under and what type of portfolio to add it
        to.
        Use: stock.classification()
        """
        #checking if stock is 'blue chip'
        if self.has_dividend == True and self.beta <= 1.0:
            status = 'Blue Chip'
            explanation = """This is what we call a blue chip stock, it
            is a stock you buy and hold over a long period of time becuase the
            price does not fluctuate very much. It also pays dividends at a set dates
            throught the fiscal year, adding value to your portfolio. If you want low risk and
            consisitent returns, this is the stock for you."""
        
        #checking if stock has high growth potential
        elif self.PE_ratio < 25.00 and self.PE_ratio > 20.00 and self.beta > 1.0:
            status = 'High Growth Potential'
            explanation = """With the price to equity ratio showing this stock being slightly
            undervalued in combination with moderate to high valatility shows potential for
            higher returns in a short period of time. You would buy this stock for a short while
            and sell it IF it goes up. This is a risker route to take, if you are okay with that,
            buy this stock."""

        #checking if the stock is real bad
        elif (self.shares_short >= 40.00 and self.PE_ratio > 25.00 and self.PE_ratio < 30.00):
            status = "STAY AWAY"
            explanation = """This stock is almost guranteed to go down in value with a lot of
            people betting on it decreasing in value and its price to earnings ratio showing
            it to be overvalued in price. Do NOT buy this stock."""
        
        #stock is pretty average, do with this what you will
        else:
            status = "Average"
            explanation = """This stock is pretty cut and dry, not in danger of a short squeeze, not super high
            growth potential or risk and lacks a dividend, if you are looking for something to diversify your
            portfolio, buy this."""
        return status, explanation
        
        
    
    
    
