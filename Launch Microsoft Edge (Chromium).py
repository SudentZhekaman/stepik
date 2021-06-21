from msedge.selenium_tools import Edge, EdgeOptions

# Launch Microsoft Edge (Chromium)
options = EdgeOptions()
options.use_chromium = True
driver = Edge(options = options)
driver.get('https://stepik.org/lesson/25969/step/8')

