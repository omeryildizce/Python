omerHesap={
    "ad": "Ömer Yıldız",
    "hesapNo": "1234560",
    "bakiye" : 3000,
    "ekHesap":  2000
}

aliHesap={
    "ad": "Ali Yıldız",
    "hesapNo": "1234561",
    "bakiye" : 2000,
    "ekHesap": 1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if hesap["bakiye"] >=miktar:
        hesap["bakiye"] -= miktar
    else:
        toplam = hesap["bakiye"]+hesap["ekHesap"]
        if toplam>=miktar:
            ekHasapKullanimi = input("Ek Hesap Kullanmak İstermisiniz.(e/h)")
            if ekHasapKullanimi == "e":
                miktar -= hesap["bakiye"]
                hesap["bakiye"] = 0                
                hesap["ekHesap"] -= miktar
                print(hesap["ekHesap"])
        else:
            print("Yetersiz Bakiye.")        

    print(hesap["bakiye"])


paraCek(omerHesap,4000)
 


