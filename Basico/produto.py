p1, N1, price1 = input().split(' ')
p2, N2, price2 = input().split(' ')

#como eu usei split e ele e usado pra strings, logo converte em string porem que quero numero int e float logo eu tenho que converter
p1 = int(p1)
N1 = int(N1)
N2 = int(N2)
price1 = float(price1)
price2 = float(price2)

total1 = price1 * N1
total2 = price2 * N2

total = total1 + total2

print(f"VALOR A PAGAR = R$ {total:.2f}")