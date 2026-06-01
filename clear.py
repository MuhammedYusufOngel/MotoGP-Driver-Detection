import os
import glob

resim_uzantilari = ["*.jpg", "*.jpeg", "*.png", "*.JPG", "*.JPEG", "*.PNG"]
silinen_sayac = 0

print("Etiketlenmemiş resimler taranıyor...")

for uzanti in resim_uzantilari:
    for resim_yolu in glob.glob(uzanti):
        dosya_adi, _ = os.path.splitext(resim_yolu)
        json_yolu = dosya_adi + ".json"
        
        if not os.path.exists(json_yolu):
            try:
                os.remove(resim_yolu)
                print(f"# Resim silindi: {resim_yolu}")
                silinen_sayac += 1
            except Exception as e:
                print(f"# {resim_yolu} silinirken hata oluştu: {e}")

print(f"\nİşlem tamamlandı! Toplam {silinen_sayac} adet etiketlenmemiş resim silindi.")