""""
Example about function, in python.. here is triangle program for example
"""
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas ={alas} dan tinggi ={tinggi} memiliki luas {luas_segitiga}')

def hitung_luas(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

""""
the rule for def is
python read every line from begining, but then on "def"
he don't read it.. it just read hitung_luas function.. 
and then when he read the function on below.. the def is now running
"""

print(hitung_luas(20,6))
