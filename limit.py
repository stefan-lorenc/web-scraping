from selenium_base import driver_creation
from selenium.webdriver.common.by import By
import time
import re

'''
Scrape the results of this calculator:

per each industry, revenue, limit
extract min, max, avg

https://www.limit.com/price-feed?industry_class=Information&revenue=1000000&limit=1000000

There will be more tasks immediately when completed.

Completed ~20 minutes
'''


def main(url):
    driver = driver_creation(is_headless=True)
    driver.get(url)
    time.sleep(5)

    min_max = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/section/section[2]/div[1]/div[1]/p[2]').text
    average = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/section/section[2]/div[1]/div[1]/div/p').text

    min_max = re.findall(r'[$][0-9].[0-9][a-zA-z]', min_max)

    print('Minimum', min_max[0], 'Maximum', min_max[1], 'Average', average)


if __name__ == '__main__':
    industries = ['Information', 'Public+Administration', 'Retail', 'Technical+Services', 'Healthcare', 'Manufacturing',
                  'Construction', 'Real+Estate', 'Other']
    revenues = ['1000000', '2000000', '3000000', '4000000', '5000000', '10000000', '15000000', '20000000', '25000000',
                '30000000', '40000000', '50000000', '60000000', '70000000', '80000000', '90000000', '100000000']

    limits = ['1000000', '2000000', '3000000']

    for industry in industries:
        for revenue in revenues:
            for limit in limits:
                main(f'https://www.limit.com/price-feed?industry_class={industry}&revenue={revenue}&limit={limit}')
