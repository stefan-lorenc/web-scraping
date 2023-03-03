from selenium_base import driver_creation
from selenium.webdriver.common.by import By
import time

'''Example URL: https://www.similarweb.com/website/androidheadlines.com/#overview

Data to extract:
Domain (heading from the top)
Total Visits
Top Countries (first 3 country names with percentage)

Completed ~15 minutes
'''


def main(url):
    driver = driver_creation()
    driver.get(url)
    time.sleep(10)

    domain = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/header/h1/span/span[2]')
    total_visits = driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div/main/div/div/div[1]/section/div/div/div/div[5]/div/div[1]/p[2]')

    countries = driver.find_elements(By.CLASS_NAME, 'wa-geography__country-info')

    country_names, country_traffic = [], []


    for item in countries:
        country_name = item.find_element(By.CLASS_NAME, 'wa-geography__country-name')
        traffic = item.find_element(By.CLASS_NAME, 'wa-geography__country-traffic-value')

        country_names.append(country_name.text)
        country_traffic.append(traffic.text)

    print(domain.text, total_visits.text)

    for x, y in zip(country_names, country_traffic):
        print(x, y)


if __name__ == '__main__':
    main('https://www.similarweb.com/website/androidheadlines.com/#overview')
