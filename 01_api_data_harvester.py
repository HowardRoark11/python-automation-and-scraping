try:


    import requests
    url="https://jsonplaceholder.typicode.com/users"
    answer_=requests.get(url)
    users=answer_.json()
except:
    print("[-] İnternet bağlantısı yok veya siteye ulaşılamıyor!")
with open("users.txt","w",encoding="utf-8") as dosya:
    for user in users:
        dosya.write(f"İsim: {user['name']} - E-Posta: {user['email']} - Şirket:{user['company']['name']} \n")
print("[+] İşlem tamamlandı! Lütfen sol taraftaki users.txt dosyasını kontrol et.")
