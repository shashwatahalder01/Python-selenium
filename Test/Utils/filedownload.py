from selenium import webdriver
import requests

FILE_SAVER_MIN_JS_URL = "https://raw.githubusercontent.com/eligrey/FileSaver.js/master/dist/FileSaver.min.js"

file_saver_min_js = requests.get(FILE_SAVER_MIN_JS_URL).content

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)

# Execute FileSaver.js in page's context
driver.execute_script(file_saver_min_js)

# Now you can use saveAs() function
download_script = f'''
    return fetch('https://cdn.sstatic.net/Sites/stackoverflow/company/img/logos/so/so-logo.svg?v=a010291124bf',
        {{
            "credentials": "same-origin",
            "headers": {{"accept":"image/webp,image/apng,image/*,*/*;q=0.8","accept-language":"en-US,en;q=0.9"}},
            "referrerPolicy": "no-referrer-when-downgrade",
            "body": null,
            "method": "GET",
            "mode": "cors"
        }}
    ).then(resp => {{
        return resp.blob();
    }}).then(blob => {{
        saveAs(blob, 'stackoverflow_logo.svg');
    }});
    '''

driver.execute_script(download_script)
# Done! Your browser has saved an SVG image!



#  using chrome options

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
# options.add_experimental_option("prefs", {
#   "download.default_directory": r"C:\Users\xxx\downloads\Test",
#   "download.prompt_for_download": False,
#   "download.directory_upgrade": True,
#   "safebrowsing.enabled": True
# })