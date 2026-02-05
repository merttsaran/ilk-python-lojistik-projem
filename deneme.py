# Kullanıcıdan veri alalım
plaka = input("Lütfen araç plakasını giriniz: ")
yuk_miktari = float(input("Kaç ton yük var? "))

# Karar verelim
if yuk_miktari > 25:
    print(f"UYARI: {plaka} plakalı araçta kapasite aşımı var! Sefer başlatılamaz.")
else:
    print(f"ONAY: {plaka} plakalı araç {yuk_miktari} ton yük ile yola çıkmaya hazır.")
    