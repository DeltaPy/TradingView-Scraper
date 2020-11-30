from colorama import Fore, Style, Back
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import colorama
import time

colorama.init()
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')

print("Example: 'USD/EUR' or 'BTC/ETH'")

inUrl = input("Insert exchanges by separating them with '/': ")
url = "https://www.tradingview.com/symbols/" + inUrl.replace('/','').upper() + "/technicals/"
print("Less than 2 seconds is" +Fore.RED + " NOT "+ Style.RESET_ALL + "recommended!")
updateRate = int(input("Refresh every how many seconds: "))

try:
    driver = webdriver.Chrome(options=chrome_options)
    print(f"{Fore.CYAN}Connecting to: " + url)
    driver.get(url)
    print(Fore.GREEN + "Running!\nPress CTRL + C to STOP" + Style.RESET_ALL)
except: 
    print(f"{Fore.RED}Error!")



def scrape():
    try:
        timeBtn = driver.find_element_by_xpath("//*[@id='technicals-root']/div/div/div[1]/div/div/div[1]/div/div/div[1]")
        timeBtn.click()
        time.sleep(1)
        summary = driver.find_element_by_xpath("//*[@id='technicals-root']/div/div/div[2]/div[2]/span[2]")
        oscillators = driver.find_element_by_xpath("//*[@id='technicals-root']/div/div/div[2]/div[1]/span")
        movAvg = driver.find_element_by_xpath("//*[@id='technicals-root']/div/div/div[2]/div[3]/span")
        return [summary.text, oscillators.text, movAvg.text]
        
    except: 
        try:
            inUrlSwapped = list(inUrl)
            inUrlSwappedB = list(inUrl)
            inUrlSwapped[4], inUrlSwapped[5], inUrlSwapped[6] = inUrlSwappedB[0], inUrlSwappedB[1], inUrlSwappedB[2]
            inUrlSwapped[0], inUrlSwapped[1], inUrlSwapped[2] = inUrlSwappedB[4], inUrlSwappedB[5], inUrlSwappedB[6]
            urlSwap = inUrlSwapped[0] + inUrlSwapped[1] + inUrlSwapped[2] +inUrlSwapped[3] +inUrlSwapped[4] +inUrlSwapped[5] +inUrlSwapped[6]
            print(f"{Fore.RED}" + inUrl.upper() + " not found trying " + urlSwap.upper())
            url = "https://www.tradingview.com/symbols/" + urlSwap.replace('/','').upper() + "/technicals/"
            driver.get(url)
            timeBtn = driver.find_element_by_xpath("//*[@id='technicals-root']/div/div/div[1]/div/div/div[1]/div/div/div[1]")
            timeBtn.click()
            time.sleep(1)
            summary = driver.find_element_by_xpath("//*[@id='technicals-root']/div/div/div[2]/div[2]/span[2]")
            oscillators = driver.find_element_by_xpath("//*[@id='technicals-root']/div/div/div[2]/div[1]/span")
            movAvg = driver.find_element_by_xpath("//*[@id='technicals-root']/div/div/div[2]/div[3]/span")
            return [summary.text, oscillators.text, movAvg.text]
        except:
            print(f"{Fore.RED}Exchange doesnt exist or tool is outdated!")
            driver.quit()
            exit()




while True:
    result = scrape()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"\n{Style.BRIGHT}{Fore.WHITE}["+current_time+f"{Style.RESET_ALL}] [", end ='')

    # __SUMMARY__

    if result[0] == "STRONG SELL":
        text = f"{Style.BRIGHT}{Fore.WHITE}Summary{Style.RESET_ALL}:{Style.BRIGHT}{Fore.RED} " + result[0] + f"{Style.RESET_ALL}] ["
        print(text, end = '')
    elif result[0] == "SELL":
        text = f"{Style.BRIGHT}{Fore.WHITE}Summary{Style.RESET_ALL}:{Style.DIM}{Fore.RED} " + result[0] + f"{Style.RESET_ALL}] ["
        print(text, end = '')
    elif result[0] == "STRONG BUY":
        text = f"{Style.BRIGHT}{Fore.WHITE}Summary{Style.RESET_ALL}:{Style.BRIGHT}{Fore.GREEN} " + result[0] + f"{Style.RESET_ALL}] ["
        print(text, end = '')
    elif result[0] == "BUY":
        text = f"{Style.BRIGHT}{Fore.WHITE}Summary{Style.RESET_ALL}:{Style.DIM}{Fore.GREEN} " + result[0] + f"{Style.RESET_ALL}] ["
        print(text, end = '')
    else:
        print(f"{Style.BRIGHT}{Fore.WHITE}Summary{Style.RESET_ALL}: " + result[0] + "] [", end ='')

    # __OSCILLATORS__

    if result[1] == "SELL":
        text = f"{Style.BRIGHT}{Fore.WHITE}Oscillators{Style.RESET_ALL}:{Style.DIM}{Fore.RED} " + result[1] + f"{Style.RESET_ALL}] ["
        print(text, end = '')
    elif result[1] == "STRONG SELL":
        text = f"{Style.BRIGHT}{Fore.WHITE}Oscillators{Style.RESET_ALL}:{Style.BRIGHT}{Fore.RED} " + result[1] + f"{Style.RESET_ALL}] ["
        print(text, end = '')
    elif result[1] == "BUY":
        text = f"{Style.BRIGHT}{Fore.WHITE}Oscillators{Style.RESET_ALL}:{Style.DIM}{Fore.GREEN} " + result[1] + f"{Style.RESET_ALL}] ["
        print(text, end = '')
    elif result[1] == "STRONG BUY":
        text = f"{Style.BRIGHT}{Fore.WHITE}Oscillators{Style.RESET_ALL}:{Style.BRIGHT}{Fore.GREEN} " + result[1] + f"{Style.RESET_ALL}] ["
        print(text, end = '')
    else:
        print(f"{Style.BRIGHT}{Fore.WHITE}Oscillators{Style.RESET_ALL}: " + result[1] + "] [", end ='')

    # __MOVING AVERAGE__

    if result[2] == "SELL":
        text = f"{Style.BRIGHT}{Fore.WHITE}Moving Average{Style.RESET_ALL}:{Style.DIM}{Fore.RED} " + result[2] + f"{Style.RESET_ALL}]"
        print(text)
    elif result[2] == "STRONG SELL":
        text = f"{Style.BRIGHT}{Fore.WHITE}Moving Average{Style.RESET_ALL}:{Style.BRIGHT}{Fore.RED} " + result[2] + f"{Style.RESET_ALL}]"
        print(text)
    elif result[2] == "BUY":
        text = f"{Style.BRIGHT}{Fore.WHITE}Moving Average{Style.RESET_ALL}:{Style.DIM}{Fore.GREEN} " + result[2] + f"{Style.RESET_ALL}]"
        print(text)
    elif result[2] == "STRONG BUY":
        text = f"{Style.BRIGHT}{Fore.WHITE}Moving Average{Style.RESET_ALL}:{Style.BRIGHT}{Fore.GREEN} " + result[2] + f"{Style.RESET_ALL}]"
        print(text)
    else:
        print(f"{Style.BRIGHT}{Fore.WHITE}Moving Average{Style.RESET_ALL}: " + result[2] + "]", end ='')

    time.sleep(updateRate-1)
    driver.refresh()

driver.quit()