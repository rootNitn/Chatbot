import urllib.request

def check_internet():
    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
        return True
    except:
        return False
