# 1-m
def sonlar(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return "Hammasi musbat"
    else:
        return "Manfiy mavjud"

print(sonlar(3, 5, 7))
print(sonlar(3, -2, 5))

# 2-m
def son_tur(son):
    if 1 <= son <= 9:
        return "Bir xonali"
    elif 10 <= son <= 99:
        return "Ikki xonali"
    else:
        return "Boshqa"


print(son_tur(5))
print(son_tur(45))
print(son_tur(123))

# 3-m
def son(a, b):
    if (a % 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0):
        return "Turli turdagi"
    else:
        return "Bir xil turdagi"

print(son(4, 7))
print(son(6, 8))

# 4-m
def matn(matn):
    if len(matn) % 2 == 0 and len(matn) > 6:
        return "Mos keladi"
    else:
        return "Mos emas"

d = "hello"
res = matn(d)
print(res)

f = ("salomhello")
res = matn(f)
print(res)

# 5-m
def tekshir(yosh, talaba):
    if yosh < 18 and talaba == False:
        return "voyaga yetmagan"
    elif yosh >= 18 and talaba == True:
        return "Talaba"
    else:
        return "Oddiy fuqaro"

maatn = 20
res = tekshir(maatn)
print(res)

# 6-m
def son_qabul_ql(son):
    if son % 3 or 5 == 0:
        return "Mos son"
    else:
        return "Mos emas"

s = 23
res = son_qabul_ql(s)
print(res)

# 7-m
def login1(login):
    if len(login) < 5:
        return "Noto‘g‘ri login"
    else:
        return "Kuchsiz parol"
de = 233
res = login1(98)
print(res)

# 9
def son_tekshir(n):
    if n > 0 and n % 2 == 0:
        natija = "Musbat juft"
    elif n > 0 and n % 2 != 0:
        natija = "Musbat toq"
    else:
        natija = "Manfiy yoki nol"

    return natija
res1 = son_tekshir(8)
print(res1)
res2 = son_tekshir(7)
print(res2)
res3 = son_tekshir(-2)
print(res3)

# 10- m
def uzunlik_tekshir(matn1, matn2):
    if len(matn1) == len(matn2):
        natija = "Uzunligi teng"
    else:
        natija = "Uzunligi teng emas"
    return natija
res = uzunlik_tekshir("salom", "dunyo")
print(res)
res = uzunlik_tekshir("python", "code")
print(res)

# 11-m
def tekwr(mant):
    if tekwr(0).isupper() and tekwr(-1) == '.':
        return "To'g'ri gap"
    else:
        return "Xato format"

res = tekwr("Salom")
print(res)

res = tekwr('salom')
print(res)

# 12-m
def belgi(email):
    if "@" and "_" in email:
        return "Email togri"
    else:
        return "Email noto'g'ri"

res = belgi("shohsanamplatova@gmail.com")
print(res)
res2 = belgi("@shohsanampolatova_gmail.com")
print(res2)

# 13-m
def ism(ismm):
    if len(ismm) < 3:
        return "Juda qisqa"
    elif 3 <= len(ismm) <= 10:
        return "Normal"
    else:
        return "Juda uzun"

res = ism("hi")
print(res)

res1 = ism("salom")
print(res1)

res2 = ism("Assalomu alaykum")
print(res2)

# 14-m
def son(sonn):
    if sonn > 100 % 2 == 0:
        return "Katta"
    else:
        return "Shartga mos emas"

res = son( 120)
print(res)

# 15-m
def matn_tekwr(matn):
    for belgi in matn:
        if not (belgi.isalpha() or belgi == " "):
            return "Ortiqcha belgilar bor"
        return "Toza matn"

res = matn_tekwr("jdh hyeg")
print(res)

# 16-m
def sonlar(toq , juft):
    if toq % 2 == 0 and juft % 2 == 0:
        return "Ikkalasi juft"
    elif toq % 3 == 0 and juft % 3 == 0:
        return "Ikkalasi toq"
    else:
        return "Aralash"

res = sonlar(12 , 2)
print(res)

res2 = sonlar(27, 9)
print(res2)

res3 = sonlar(2 , 5)
print(res3)

# 17-m
def raqam(raqamii):
    if len(raqamii) == 9:
        return "To'g'ri raqam"
    else:
        return "Noto'g'ri raqam"

res = raqam("998993190915")
print(res)

res1 = raqam("993190915")
print(res1)

# 18-m
def matn(matnnnnn):
    if len(matnnnnn) > 5 :
        return "Katta palindrom"
    else:
        return "Oddiy yoki palidrom emas"

res = matn("Salloomm")
print(res)

res2 = matn("hi")
print(res2)

# 19-m
def son(soni):
    if soni > 0 and soni < 50:
        return "kichik musbat"
    elif soni > 50:
        return "katta musbat"
    else:
        return "manfiy nol"

res = son(38)
print(res)

res2 = son(65)
print(res2)

res3 = son(0)
print(res3)

# 20-m
def qabul(nom, parol):
    if len(nom) == 6 and len(parol) == 6:
        return "Qabul qilindi"
    else:
        return "Ma'lumotlar juda qisqa"

res = qabul("shohsanam", "login1")
print(res)

# 21-m
def qabul(a, b, c):
    if max(a, b, c):
        return f"eng katta {max(a, b, c)}"

res = qabul(9, 7, 5)
print(res)

# 22-m
def oy(fasl):
    if fasl == 3 or fasl == 4 or fasl == 5:
        return "Bahor"
    elif fasl == 6 or fasl == 7 or fasl == 8:
        return "Yoz"
    elif fasl == 9 or fasl == 10 or fasl == 11:
        return "Kuz"
    elif fasl == 12 or fasl == 1 or fasl == 2:
        return "Qish"

res = oy(2)
print(res)

res = oy(9)
print(res)

# 23-m
def son(soni):
    if soni % 2 == 0 and soni % 3 == 0:
        return " 6 ga karrali"
    elif soni % 2 == 0 or soni % 3 == 0:
        return "Qisman mos"
    else:
        return "Mos emas"

res = son(79)
print(res)
res = son(14)
print(res)

# 24-m

# 25-m

# 26-m
def qabul(parol):
    if len(parol) < 6:
        return "Juda zaif"
    elif len(parol) > 6 < 10:
        return "O'rtacha"
    elif len(parol) > 10:
        return "Kuchli"

res = qabul(7)
print(res)

# 27-m

