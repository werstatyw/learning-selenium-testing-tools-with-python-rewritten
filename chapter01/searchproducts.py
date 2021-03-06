from selenium import webdriver

# create a new Opera instance
driver = webdriver.Opera(executable_path = '../operadriver')
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get('http://demo-store.seleniumacademy.com/')

# get the search textbox
search_field = driver.find_element_by_name('q')
search_field.clear()

# enter search keeywords and submit
search_field.send_keys('tee')
search_field.submit()

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath('//h2[@class="productname"]/a')

# get the number of anchor elements found
print(f'Found {len(products)} products')

# iterate through each anchor element and print the text that is # name of the product
for product in products:
    print(product.text)

# close the browser window
driver.quit()