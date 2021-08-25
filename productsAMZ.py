from selenium import webdriver    # Basic interface to simulate user interactions with any browser
from selenium.common.exceptions import NoSuchElementException    # Import a certain error from the corresponding module
import xlrd    # Module that allows us to work with XLSX files (version 1.2.0)
import xlsxwriter    # Module that allows us to write to XLSX files
import os    # Module that allows us to work with directories dynamically

products = []    # Working variables
availability = []
xpath = '//*[@id="availability"]/span'    # Xpath selector

dir = os.getcwd()    # Get the ASIN codes of the products defined in the specified file XLSX
filePath = dir+"\\productos.xlsx"                                    
sheet = xlrd.open_workbook(filePath)
hoja = sheet.sheet_by_name("Hoja1")
for i in range(0, hoja.nrows):
    products.append(hoja.cell_value(i,0))

options = webdriver.ChromeOptions()    # Define the necessary options to be able to use the Chrome browser
options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver_path = 'C:\\Users\\Jeshua\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(driver_path, options=options)

for p in products:    # Get and save the availability of each product
    driver.get("https://www.amazon.es/gp/product/"+p)
    try:
        ava = driver.find_element_by_xpath(xpath).text
        if "stock" in ava:
            availability.append(ava)
        elif "No disponible" in ava:
            availability.append(ava)
        else:
            availability.append("Disponible a través de otros vendedores de Amazon.")
    except NoSuchElementException:  
        availability.append("Amazon no vende o ha dejado de vender este producto.")

wb = xlsxwriter.Workbook('disponibilidad.xlsx')    # Write the data obtained in a new XLSX document
format = wb.add_format({'bg_color':'#FFD61C', 'border': 1, 'bold': True, 'italic': True, 'align': 'center'})
format2 = wb.add_format({'border': 1})
out = wb.add_worksheet()
out.set_column(0, 0, 15)
out.set_column(1, 1, 50)
out.write(0, 0, "ASIN", format)
out.write(0, 1, "DISPONIBILIDAD", format)
i=0
for asin in products:
    i+=1
    out.write(i, 0, asin, format2)
i=0
for product in availability:
    i+=1
    out.write(i, 1, product, format2)
wb.close()

print("HECHO!")