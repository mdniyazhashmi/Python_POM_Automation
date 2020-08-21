<<<<<<< HEAD
pytest -v -s -m "sanity" --html=./reports/report_chrome.html testCases/ --browser chrome
=======
REM pytest -v -s -m "sanity" --html=./reports/report_chrome.html testCases/ --browser chrome
>>>>>>> 35d35cf76e593e7c23f8cbb759aaede55042d3f2
REM pytest -v -s -m "sanity" --html=./reports/report_firefox.html testCases/ --browser firefox

REM pytest -v -s -m "sanity and regression" --html=./reports/report_chrome.html testCases/ --browser chrome
REM pytest -v -s -m "sanity and regression" --html=./reports/report_firefox.html testCases/ --browser firefox

REM pytest -v -s -m "sanity or regression" --html=./reports/report_chrome.html testCases/ --browser chrome
REM pytest -v -s -m "sanity or regression" --html=./reports/report_firefox.html testCases/ --browser firefox

<<<<<<< HEAD
REM pytest -v -s -m "regression" --html=./reports/report_chrome.html testCases/ --browser chrome
REM pytest -v -s -m "regression" --html=./reports/report_firefox.html testCases/ --browser firefox
=======
pytest -v -s -m "regression" --html=./reports/report_chrome.html testCases/ --browser chrome
REM pytest -v -s -m "regression" --html=./reports/report_firefox.html testCases/ --browser firefox
>>>>>>> 35d35cf76e593e7c23f8cbb759aaede55042d3f2
