#imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from stocks import Stonks
import os

options = Options()
options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
PATH = "project_site/chromedriver.exe"
driver = webdriver.Chrome(options=options)

def stock_collector(ticker):
    """
    Takes a a number of tickers split by a comma inputted
    by the user and collects information on the stocks.
    Use stocks = stock_collector(tickers)
    """
    #going directly to the stats page for maximum efficiency
    driver.get('https://ca.finance.yahoo.com/quote/{}/key-statistics?p={}'.format(ticker,ticker))

    #collecting information about the stock
    name = driver.find_element_by_xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1').get_attribute('innerHTML')
    price = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/div/div/div/div[3]/div[1]/div/span[1]").get_attribute('innerHTML')
    PE_ratio = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div[1]/div/div/div/div/table/tbody/tr[4]/td[2]").get_attribute('innerHTML') 
    beta = driver.find_element_by_css_selector("#Col1-0-KeyStatistics-Proxy > section > div.Mstart\(a\).Mend\(a\) > div.Fl\(end\).W\(50\%\).smartphone_W\(100\%\) > div > div:nth-child(1) > div > div > table > tbody > tr.Bxz\(bb\).H\(36px\).BdY.Bdc\(\$seperatorColor\) > td.Fw\(500\).Ta\(end\).Pstart\(10px\).Miw\(60px\)").get_attribute('innerHTML')
    yearly_change = driver.find_element_by_css_selector("#Col1-0-KeyStatistics-Proxy > section > div.Mstart\(a\).Mend\(a\) > div.Fl\(end\).W\(50\%\).smartphone_W\(100\%\) > div > div:nth-child(1) > div > div > table > tbody > tr:nth-child(2) > td.Fw\(500\).Ta\(end\).Pstart\(10px\).Miw\(60px\)").get_attribute('innerHTML')
    held_by_institutions = driver.find_element_by_css_selector("#Col1-0-KeyStatistics-Proxy > section > div.Mstart\(a\).Mend\(a\) > div.Fl\(end\).W\(50\%\).smartphone_W\(100\%\) > div > div:nth-child(2) > div > div > table > tbody > tr:nth-child(7) > td.Fw\(500\).Ta\(end\).Pstart\(10px\).Miw\(60px\)").get_attribute('innerHTML')
    shares_short = driver.find_element_by_xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[2]/div[2]/div/div[2]/div/div/table/tbody/tr[9]/td[2]').get_attribute('innerHTML')
    dividend = driver.find_element_by_css_selector('#Col1-0-KeyStatistics-Proxy > section > div.Mstart\(a\).Mend\(a\) > div.Fl\(end\).W\(50\%\).smartphone_W\(100\%\) > div > div:nth-child(3) > div > div > table > tbody > tr:nth-child(3) > td.Fw\(500\).Ta\(end\).Pstart\(10px\).Miw\(60px\)').get_attribute('innerHTML')
    if dividend[0] == '<':
        dividend = 'N/A'
    if beta[0] == '<':
        beta = 'N/A'
    #initializing the stock object with all data
    item = Stonks(name,ticker,price,PE_ratio,beta,yearly_change,held_by_institutions,shares_short,dividend)
        
    return item
