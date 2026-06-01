import os
import json
from collections import Counter

#directory_path = r"./dataset_2026_mugello" 
directory_path = r"./dataset_final" 

etiket_sayaci = Counter()

for dosya in os.listdir(directory_path):
    if dosya.endswith('.json'):
        dosya_yolu = os.path.join(directory_path, dosya)
        with open(dosya_yolu, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for shape in data.get('shapes', []):
                etiket_sayaci[shape['label']] += 1

print("--- DRIVER LABEL COUNTS ---")
for surucu, adet in etiket_sayaci.items():
    print(f"{surucu}: {adet} adet kutu çizildi.")