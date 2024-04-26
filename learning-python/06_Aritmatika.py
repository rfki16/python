# operasi aritmatika

a = 10
b = 3

# penjumlahan + 
hasil = a + b
print(a,'+',b, '=', hasil)

# pengurangan -
hasil = a - b
print(a,'-',b, '=', hasil)

# perkalian *
hasil = a * b
print(a,'*',b, '=', hasil)

# pembagian /
hasil = a / b
print(a,'/',b, '=', hasil)

# pangkat +*
hasil = a ** b
print(a,'**',b, '=', hasil)

# modulus %
hasil = a % b
print(a,'%',b, '=', hasil)

# floor division
hasil = a // b
print(a, '//' , b, '=', hasil)

# prioritas operasi
'''
    1. ()
    2. **
    3. perkalian dan teman-temannya
    4. penjumlahan dan pengurangan
'''

x = 2
y = 5
z = 6

hasil =  x ** y + z / x - y
print(x,'**',y,'+',z,'/',x,'-',y, '=' ,hasil)
