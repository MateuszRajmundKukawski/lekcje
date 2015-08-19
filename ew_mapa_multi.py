import ew_mapa_modul as ew
import  glob
__author__ = 'mati'

lista_plikow = glob.glob('*.txt')
print lista_plikow
print 'zaczynamy!'
print '*'*3
for pliczek in lista_plikow:

    print "dla pliku:", pliczek
    ew.zwrocSlownik(pliczek)
    print '*\n'*3
