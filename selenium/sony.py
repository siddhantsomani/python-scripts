from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from pyvirtualdisplay import Display

# To make it execute in the background
# display = Display(visible=0, size=(800, 600))
# display.start()

f = open('sony.txt')
a = f.read()
print(a)
a = a.replace(' ','')
a = a.replace(',,',',')
a = a.replace('\n',',')
arr = a.split(',')
length = len(arr)
print(length)
i = 0
while (i<length):
	driver = webdriver.Firefox()
	driver.get("http://www.ericsson.com/thecompany/events/ericsson-innovation-awards/competition/#/submission/15873")
	driver.implicitly_wait(2)
	driver.find_element_by_link_text('Vote for this project').click()
	text = driver.find_element_by_id('voterEmailInputField')
	text.send_keys(arr[i])
	i = i+1
	print(str(length-i)+' left')
	text.send_keys(Keys.RETURN)
	driver.delete_all_cookies()
	driver.close()

# display.stop()
