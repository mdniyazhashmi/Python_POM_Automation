taskkill /F /IM chromedriver.exe
REM pytest -v -s -m "sanity" --html=./reports/report_chrome.html testCases/ --browser chrome
REM pytest -v -s -m "sanity" --html=./reports/report_firefox.html testCases/ --browser firefox

REM pytest -v -s -m "sanity and regression" --html=./reports/report_chrome.html testCases/ --browser chrome
REM pytest -v -s -m "sanity and regression" --html=./reports/report_firefox.html testCases/ --browser firefox

REM pytest -v -s -m "sanity or regression" --html=./reports/report_chrome.html testCases/ --browser chrome
REM pytest -v -s -m "sanity or regression" --html=./reports/report_firefox.html testCases/ --browser firefox

pytest -v -s -m "regression" --html=./reports/report_chrome.html testCases/ --browser chrome
pytest -v -s -m "regression" --html=./reports/report_firefox.html testCases/ --browser firefox