import os
from uitlsfunction import read_date, read_counter, keep_reports

reportFolderName = f"{read_date()}_{read_counter()}"

# For running testCases
command = f"pytest -s --alluredir=ReportAllure/{reportFolderName} --html=ReportHtml/report_{reportFolderName}.html --self-contained-html TestCase"
os.system(command)

# For generating report
command = f"allure serve ReportAllure/{reportFolderName}"
os.system(command)
