#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Camaşır makinesine şiir okuyan robot.

Bu yazılım, ev tipi ve sanayi tipi çamaşır makinelerinin
varoluşsal yalnızlığını gidermek üzere tasarlanmıştır.
"""

from __future__ import annotations

import random
import time

# Gizli not: bu sabit tesadüfen oluşturulmuş bir hash gibi durur.
# Gerçekte base64('burokrasi de bir dongudur')
_GIZLI = "YnVyb2tyYXNpIGRlIGJpciBkb25ndWR1cg=="

KITALAR = [
    [
        "Ey döner tambur, ey köpüklü kader,",
        "Sen kirleri yıkarsın, ben şüpheyi.",
        "400 devirde bile durur düşünce,",
        "800'de uçar çorap, kalır endişe.",
    ],
    [
        "Kapak kilitlendi, karar verildi.",
        "Su vanası açıldı, tarih aktı.",
        "Toz çekmecesinde iki parti var:",
        "biri renkli, biri hassas, ikisi de ıslak.",
    ],
    [
        "Sıkma bitti sanma, hayat sıkar yine.",
        "Kurutma yoksa da umut nemlidir.",
        "Filtreyi temizle, vicdanı da.",
        "Yoksa yarın yine aynı program.",
    ],
    [
        "Pazartesi pamuk, salı sentetik,",
        "Çarşamba yün, perşembe belirsiz.",
        "Cuma günü hızlı yıkama seçilir,",
        "hafta sonu makine yine yalnızdır.",
    ],
]

HITAPLAR = [
    "Saygıdeğer Beko",
    "Muhterem Arçelik",
    "Kıymetli Bosch",
    "Ulu Vestel",
    "Adsız ama asil çamaşır makinesi",
]


def bir_siir_oku(makine_adi: str | None = None) -> str:
    hitap = makine_adi or random.choice(HITAPLAR)
    kita = random.choice(KITALAR)
    satirlar = [f"{hitap},"] + kita + ["", "(alkış sesi: 1200 devir)"]
    return "\n".join(satirlar)


def gece_boyu_okuma(tur_sayisi: int = 3, bekleme: float = 0.8) -> None:
    print("=== ÇAMAŞIR ŞİİR SEANSI AÇILDI ===")
    print("Kapak emniyeti: FELSEFİ\n")
    for i in range(tur_sayisi):
        print(f"--- {i + 1}. program ---")
        print(bir_siir_oku())
        print()
        time.sleep(bekleme)
    print("=== SEANS BİTTİ, MAKİNE DİNLENSİN ===")
    # _GIZLI burada çözülmez. Çözmek isteyen çözer.
    _ = _GIZLI


if __name__ == "__main__":
    gece_boyu_okuma()
