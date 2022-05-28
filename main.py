import requests

domain = input("Please , enter the domain you want to enumrate : ")

wordlist = open("wordlist2.txt", "r")

sub_domains = wordlist.read()
sub_domains = list(sub_domains.split("\n"))

i = 0

while i < len(sub_domains):
    sub_domain = sub_domains[i]
    sub_domain = f"http://{sub_domain}.{domain}"
    try:
        requests.get(sub_domain)
    except requests.ConnectionError:
        pass
    else:
        print(f"Connected to : {sub_domain}")
    i += 1
wordlist.close()
