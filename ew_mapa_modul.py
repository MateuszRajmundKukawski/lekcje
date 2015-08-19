__author__ = 'mati'


plik = 'plik'
def zwrocSlownik(plik):
    with open(plik) as f:
        wiersze = [row.rstrip() for row in f]
    '''
    rstrip() ucina biale znaki po prawej stronie w stringu. znal nowej lini jest bialym znakiem
    w rstrip mozna podac cokolwiek, np. 'kot' wtedy usunie wszystkie koty po na koncu tekstu
    TU robimy to poto, aby kolejne elementy w liscie 'wiersze' byly pozbawione /n bo tego nie potrzebujemy
    '''

    dzialki = [row.split(',')[0] for row in wiersze]
    '''
    mamy gole wiersza, ale chcemy liste dzialek wiec:
    filtrujemy liste:
    kazdy element (tu zmienna 'row') tniemy (dzielimy) za pomoca ',' -> .split(',')
    pobieremy pierwszy element [0] -> numer dzialki
    '''

    set_dzialki = set(dzialki)
    '''
    robimy set -> zbior wartosci unikalnych
    '''


    print wiersze
    print dzialki
    print set_dzialki

    slownik = {}
    '''
    deklaruja zmienna slownik, ktora bedzie slownikiem :)
    pozniej bedziemy sie do niej odwolywali, inaczej sypnie bledem
    '''

    '''
    teraz magia, tu fajnie widac po co jest filtrowanie list
    '''


    for dz in set_dzialki:
        '''
        petla leci po numerach dzialek
        '''
        #print dz
        kot = [element for element in wiersze if element.split(',')[0] == dz]
        '''
        i tu najwazniejszy element
        filtrujemy liste 'wiersze' w taki sposob aby nowa lista 'kot'
        zawierala tylko te wiersze, dla ktorych numer dzialki == numer dzialki z seta -- to po czym iterujemy
        element 'splitujemy' przecinkiem i pobieramy pierwszy element nowopowstalej listy
        a nastepnie porownujemy go z numerem dzialki po ktorym iterujemy

        [<zwroc> element <dla> element <z/w> in wiersze <jesli> if <element.podzieliny_za_pomoca_przcinka[obiekt_pierwszy> element.split(',')[0]
        <rowna sie> == <numer dzialki z seta> == dz

        '''
        print dz, kot
        '''
        a tu aktualizujemy slownik
        klucz to numer dzialki
        dane to kot (fajna nazwa, bo ktorka :)) - czyli nasza lista powstala w wyniku filtowania
        '''
        slownik[dz]=kot





    '''
    a z tym slownikiem mozesz juz robic wszystko
    '''
    return slownik

if __name__ == '__main__':
    nasz_plik = 'plik'
    print zwrocSlownik(nasz_plik)

