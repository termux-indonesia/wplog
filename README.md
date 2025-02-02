# wplog
Bruteforce CMS Wordpress

# Preview
```


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

usage: wplog.py [-h] -url URL [-u USER] [-p WORDLIST]

WordPress Login Brute Force

options:
  -h, --help            show this help message and exit
  -url URL              Target URL (contoh: http://example.com)
  -u USER, --user USER  Username untuk brute force
  -p WORDLIST, --wordlist WORDLIST
                        Path ke file wordlist
```

# Command
User Enumeration:
```
python wplog.py -url http://example.com
```
Mode Bruteforce
```
python wplog.py -url http://example.com -u admin -p wordlist.txt
```

# Please Visit my blog
<a href="https://mainsec.blogspot.com/" alt="mainsec" target="_blank">touch me</a>
