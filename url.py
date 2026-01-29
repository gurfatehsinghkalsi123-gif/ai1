import webbrowser
site  = input(f"which site you want to open(youtube, wikipedia)")
site = site.strip().lower()
url = f'https://www.{site}.com'
webbrowser.open(url)
