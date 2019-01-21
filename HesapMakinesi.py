#! /usr/bin/env python
# -*- coding: UTF-8 -*-
print("Onur'un Hesap Makinesi")
print("=======================")
#İşlem Tanımlama
print("1 İşlemi Toplama")
print("2 İşlemi Çıkarma")
print("3 İşlemi Çarpma")
print("4 İşlemi Bölme")
c1 = input("Lütfen İşlemi Seçin:")
a1 = input("Lütfen İlk Sayıyı Girin:")
b1 = input("Lütfen İkinci Sayıyı Girin:")
x1 = int(a1)
y1 = int(b1)
secim = c1
if secim == "1":
    print(x1, "+", y1, "=", (x1+y1))
elif secim == "2":
    print(x1, "-", y1, "=", (x1-y1))
elif secim == "3":
    print(x1, "x", y1, "=", (x1*y1))
elif secim == "4":
    print(x1, "/", y1, "=", (x1/y1))
else:
    print("Hatalı İşlem")
d1= input("Yeni İşlem İçin 5, İşleme Devam İçin 6:")
if d1 == "5":
    pass
elif d1 == "6":
    pass
else:
    print("Hatalı İşlem")
while d1 == "5":
    print("1 İşlemi Toplama")
    print("2 İşlemi Çıkarma")
    print("3 İşlemi Çarpma")
    print("4 İşlemi Bölme")
    c1 = input("Lütfen İşlemi Seçin:")
    a1 = input("Lütfen İlk Sayıyı Girin:")
    b1 = input("Lütfen İkinci Sayıyı Girin:")
    x1 = int(a1)
    y1 = int(b1)
    secim = c1
    if secim == "1":
        print(x1, "+", y1, "=", (x1 + y1))
    elif secim == "2":
        print(x1, "-", y1, "=", (x1 - y1))
    elif secim == "3":
        print(x1, "x", y1, "=", (x1 * y1))
    elif secim == "4":
        print(x1, "/", y1, "=", (x1 / y1))
    else:
        print("Hatalı İşlem")
    d1 = input("Yeni İşlem İçin 5, İşleme Devam İçin 6:")
    if d1 == "5":
        pass
    elif d1 == "6":
        pass
    else:
        print("Hatalı İşlem")
while d1 == "6":
    if secim == "1":
        x1 = (x1+y1)
    elif secim == "2":
        x1 = (x1-y1)
    elif secim == "3":
        x1 = (x1*y1)
    elif secim == "4":
        x1 = (x1/y1)
    else:
        print("Hata")
    print("1 İşlemi Toplama")
    print("2 İşlemi Çıkarma")
    print("3 İşlemi Çarpma")
    print("4 İşlemi Bölme")
    c1 = input("Lütfen İşlemi Seçin:")
    b1 = input("Lütfen İkinci Sayıyı Girin:")
    y1 = int(b1)
    secim = c1
    if secim == "1":
        print(x1, "+", y1, "=", (x1 + y1))
    elif secim == "2":
        print(x1, "-", y1, "=", (x1 - y1))
    elif secim == "3":
        print(x1, "x", y1, "=", (x1 * y1))
    elif secim == "4":
        print(x1, "/", y1, "=", (x1 / y1))
    else:
        print("Hatalı İşlem")
    d1 = input("Yeni İşlem İçin 5, İşleme Devam İçin 6:")
    if d1 == "5":
        pass
    elif d1 == "6":
        pass
    else:
        print("Hatalı İşlem")



