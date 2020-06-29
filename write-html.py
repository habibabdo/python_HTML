import webbrowser

f = open('hello.html', 'w')

msg = """<html><head></head><body><p><h2>Hello Habib!</h2></p></body></html>"""

f.write(msg)
f.close()

webbrowser.open_new_tab('hello.html')