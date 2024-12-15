class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.sinistra = None
        self.destra = None

class AlberoBinario:
    def __init__(self):
        self.radice = None

    def aggiungi(self, valore):
        if self.radice is None:
            self.radice = Nodo(valore)
        else:
            self._aggiungi(self.radice, valore)

    def _aggiungi(self, nodo, valore):
        if valore <= nodo.valore:
            if nodo.sinistra is None:
                nodo.sinistra = Nodo(valore)
            else:
                self._aggiungi(nodo.sinistra, valore)
        else:
            if nodo.destra is None:
                nodo.destra = Nodo(valore)
            else:
                self._aggiungi(nodo.destra, valore)

    def stampa_in_ordine(self):
        self._stampa_in_ordine(self.radice)

    def _stampa_in_ordine(self, nodo):
        if nodo is not None:
            self._stampa_in_ordine(nodo.sinistra)
            print(nodo.valore, end=' ')
            self._stampa_in_ordine(nodo.destra)

# Funzione principale
def main():
    albero = AlberoBinario()
    print("Inserisci numeri nell'albero binario. Digita '666s' per terminare.")
    while True:
        try:
            numero = int(input("Inserisci un numero: "))
            if numero == 666:
                break
            albero.aggiungi(numero)
        except ValueError:
            print("Per favore inserisci un numero valido.")
    
    print("\nNumeri in ordine crescente:")
    albero.stampa_in_ordine()

if __name__ == "__main__":
    main()
