#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from contextlib import closing
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

page_url = "https://scholar.google.com/citations?user=r9m5qwkAAAAJ&hl=en&oi=ao#d=gs_md_cita-d&u=%2Fcitations%3Fview_op%3Dview_citation%26hl%3Den%26user%3Dr9m5qwkAAAAJ%26citation_for_view%3Dr9m5qwkAAAAJ%3Au5HHmVD_uO8C%26tzom%3D300"
target_id = 'aep-abstract-sec-id8'
target_class = 'gsh_csp'

with closing(Firefox()) as browser:
	browser.get(page_url)
	element_present = EC.presence_of_element_located((By.CLASS_NAME, target_class))
	try:
		WebDriverWait(browser, timeout=10).until(element_present)
	except TimeoutException:
		print("TIMEOUT")

	page_source = browser.page_source

abstract = BeautifulSoup(page_source, "html.parser").find_all('div', class_=target_class)
print(abstract)
