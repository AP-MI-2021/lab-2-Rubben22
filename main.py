def get_leap_years(start, end):
  exista = False
  for i in range (start, end + 1):
    if i % 4 == 0:
      print (i)
      exista = True
  if exista == False:
    print ("nu exista ani bisecti in intervalul indicat")
def test_get_leap_years():
  assert get_leap_years(2010,2018) == 2012, 2016
  assert get_leap_years(2000,2011) == 2004, 2008
  assert get_leap_years(2005, 2007) == ()

def is_palindrome(n):
  x = n
  nr = 0
  ok = False
  while x > 0:
    nr = nr * 10 + x % 10
    x = x // 10
  if n == nr:
    ok = True
  return ok
def test_is_palindrome():
  assert is_palindrome(4774) is True
  assert is_palindrome(121) is True
  assert is_palindrome(264) is False
  assert is_palindrome(22) is True

def get_perfect_squares(start,end):
  exista = False
  for i in range (start, end + 1):
    for j in range (i):
      if j * j == i:
        print (i," ")
        exista = True
  if exista == False:
    print("Nu exista patrate perfecte in interval")
def test_get_perfect_squares():
  assert get_perfect_squares(12,28) == 16, 25
def main():
  while True:
    print("1.Afiseaza anii bisecti dintre 2 ani dati: ")
    print("2.Afiseaza toate patratele perfecte dintr-un interval")
    print("3.Verifica daca un numar este palindrom")
    print("4.Iesi")
    optiune=int(input("Alege o optiune: "))
    if optiune == 1:
      unu = int(input("dati primul an: "))
      doi = int(input("dati al doilea an: "))
      get_leap_years(unu, doi)
    elif optiune == 2:
      print("Alege interval: ")
      stanga = int(input("limita stanga: "))
      dreapta = int(input("limita dreapta: "))
      get_perfect_squares(stanga, dreapta)
    elif optiune == 3:
      n=int(input("dati numarul: "))
      if is_palindrome(n) == True:
        print("este palindrom")
      else:
        print("nu este palindrom")
    elif optiune == 4:
      break
if __name__ == '__main__':
  main()