# --- Lojistik Kayıt Sistemi ---

# Değişkenleri Tanımlayalım (Girdi verileri)
konteyner_no = "GMNI-9922"
yuk_tipi = "Tekstil"
agirlik = 22.5 # Ton cinsinden
kapasite_siniri = 25.0

print(f"--- {konteyner_no} Nolu Konteyner Kontrolü ---")

# Basit bir Backend Karar Mekanizması (If-Else)
if agirlik <= kapasite_siniri:
    print(f"Durum: ONAYLANDI. {yuk_tipi} yükü gemiye yüklenebilir.")
    kalan_kapasite = kapasite_siniri - agirlik
    print(f"Not: Gemide bu hattan kalan boşluk: {kalan_kapasite} ton.")
else:
    print("Durum: REDDEDİLDİ! Kapasite aşımı var.")
    fark = agirlik - kapasite_siniri
    print(f"Uyarı: {fark} ton yük boşaltılmalıdır.")