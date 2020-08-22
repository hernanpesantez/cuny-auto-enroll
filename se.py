

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# =============be awere that this script will try to register for all your classes that are alredy in your shoping cart========
#==============you may have to remove the classes  you don't want, and also be nice to other students ==============



from selenium import webdriver


# ChromeDriverManager will insall selenium for you if not present in your system
# webdriver_manager must be install in you system
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.support.ui import Select



# we have to sleep for a bit cunyfisrt server is slow
import time



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



usernameString = "your-cuny-emai"
passwordString = "your-cuny-password"

#launch url
url = "https://ssologin.cuny.edu/cuny.html?resource_url=https%3A%2F%2Fhome.cunyfirst.cuny.edu" \
      "%252Fpsp%252Fcnyepprd%252FEMPLOYEE%252FEMPL%252Fh%252F%3Ftab%253DDEFAULT"


# create a new Chrome session 
browser =  webdriver.Chrome(ChromeDriverManager().install())



browser.implicitly_wait(30)
browser.get(url)



# fill in username
username = browser.find_element_by_id("CUNYfirstUsernameH")
username.send_keys(usernameString)
# fill in password
password = browser.find_element_by_id("CUNYfirstPassword")
password.send_keys(passwordString)

# submit password and username
logIn = browser.find_element_by_id('submit')
logIn.click()







browser.find_element_by_css_selector("a[href*='https://home.cunyfirst.cuny.edu']").click()


username = browser.find_element_by_id("CUNYfirstUsernameH")
username.send_keys(usernameString)

password = browser.find_element_by_id("CUNYfirstPassword")
password.send_keys(passwordString)


logIn = browser.find_element_by_id('submit')
logIn.click()

# click on student center
browser.find_element_by_xpath('//*[@id="crefli_HC_SSS_STUDENT_CENTER"]').click()


# this took me some time to figere it out, you need to be aware of iframes
iframe_one = browser.find_element_by_xpath('//*[@id="ptifrmtgtframe"]')

#so here se switch to that iframe and start manipulating it 
browser.switch_to.frame(iframe_one)

browser.find_element_by_xpath('//*[@id="win0div$ICField245"]/table').click()




browser.find_element_by_xpath('//*[@id="win0divDERIVED_SSTSNAV_SSTS_NAV_TABS"]/div/table/tbody/tr[2]/td[8]/a').click()

browser.find_element_by_xpath('//*[@id="trSSR_DUMMY_RECV1$0_row2"]/td[1]').click()

browser.find_element_by_xpath('//*[@id="DERIVED_SSS_SCT_SSR_PB_GO"]').click()

browser.find_element_by_xpath('//*[@id="DERIVED_REGFRM1_LINK_ADD_ENRL$82$"]').click()

browser.find_element_by_xpath('//*[@id="DERIVED_REGFRM1_SSR_PB_SUBMIT"]').click()



# this wille

while True:

	try:
		browser.find_element_by_xpath('//*[@id="win0divDERIVED_SSTSNAV_SSTS_NAV_TABS"]/div/table/tbody/tr[2]/td[8]/a').click()


		browser.find_element_by_xpath('//*[@id="DERIVED_REGFRM1_LINK_ADD_ENRL$82$"]').click()

		browser.find_element_by_xpath('//*[@id="DERIVED_REGFRM1_SSR_PB_SUBMIT"]').click()
		time.sleep(10)
	except:
		print('Someting went wrong: trying again')
