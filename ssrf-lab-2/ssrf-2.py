import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exeptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def main():
    if len (sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])

    url = sys.argv[1]
    print("(+) Finding admin hostname...")
    admin_hostname = check_admin_hostname(url)
    # not complete

if __name__ == "__main__":
    main()
    