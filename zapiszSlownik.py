import ew_mapa_modul as ew
import  glob
__author__ = 'mati'

lista_plikow = glob.glob('*.txt')
print lista_plikow
print 'zaczynamy!'
print '*'*3
for pliczek in lista_plikow:

    print "dla pliku:", pliczek
    nazwa_noweg_pliku = pliczek[:-4]+'wynik.txt'
    """
    to jest ciekway myk, bo napisy mozemy ciac/indekoswac podobnie jak listy
    """
    roboczy_slownik = ew.zwrocSlownik(pliczek)
    """
    a tu uzywamy metody zwrocSlownik z modulu ew_mapa_modul - zeby bylo latwiej
    wczytalismy go jako ew
    przy okazji wazna sprawa
    pocztasz duzo o przestrzeni nazw itp.
    generalnie, trzeba uwazac jak sie nazywa zmienne, bo jesli np:
    nazwiesz zmiena lub metode print to juz zwykly print nie zadziala
    dlatego lepiej unikac nazw w stylu
    file, list itp
    """

    with open(nazwa_noweg_pliku, 'w') as npl:
        for klucz, wartosc in roboczy_slownik.items():
            print klucz, wartosc
            '''
            teraz czas to zapiac
            zapiszmy w wersji najprostszej
            piersza kolumna: nr dzialki
            druga kolumna: strony (polaczone przecinkiem)
            '''
            '''
            po chwili namylu -> tu tez filtrujmey liste
            '''
            wartosc = ','.join([','.join(strona.split(',')[1:]) for strona in wartosc])

            print wartosc
            wiersz_do_zapisu = ';'.join([klucz, wartosc])+'\n'
            print 'wiersz_do_zapisu', wiersz_do_zapisu
            npl.write(wiersz_do_zapisu)

