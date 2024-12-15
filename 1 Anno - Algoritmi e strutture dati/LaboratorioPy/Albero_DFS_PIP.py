class Node:
    """
    Classe che rappresenta un nodo dell'albero.
    Ogni nodo ha un valore, un figlio sinistro e un figlio destro.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """
    Classe che rappresenta un albero binario e fornisce metodi per aggiungere nodi e
    eseguire traversate DFS (Pre-Order, In-Order, Post-Order).
    """
    def __init__(self):
        self.root = None

    def insert(self, value, direction):
        """
        Inserisce un valore nell'albero binario seguendo la direzione indicata.

        :param value: Il valore del nodo da inserire
        :param direction: Una stringa che specifica il percorso ("L" per sinistra, "R" per destra)
        """
        if self.root is None:
            # Se l'albero è vuoto, il primo nodo diventa la radice
            self.root = Node(value)
            print(f"Radice inserita: {value}")
        else:
            # Altrimenti, segui la direzione per trovare la posizione corretta
            current = self.root
            for i, d in enumerate(direction[:-1]):
                if d == 'L':
                    if current.left is None:
                        current.left = Node(None)  # Nodo temporaneo
                    current = current.left
                elif d == 'R':
                    if current.right is None:
                        current.right = Node(None)  # Nodo temporaneo
                    current = current.right
                else:
                    raise ValueError("Direzione non valida. Usa 'L' per sinistra o 'R' per destra.")

            # Inserisce il nodo nella posizione finale
            if direction[-1] == 'L':
                current.left = Node(value)
            elif direction[-1] == 'R':
                current.right = Node(value)
            else:
                raise ValueError("Direzione non valida. Usa 'L' per sinistra o 'R' per destra.")
            print(f"Nodo inserito: {value} in direzione {direction}")

    def dfs_pre_order(self, node):
        """
        Stampa i nodi in ordine Pre-Order (radice, sinistra, destra).
        """
        if node is not None:
            print(node.value, end=' ')
            self.dfs_pre_order(node.left)
            self.dfs_pre_order(node.right)

    def dfs_in_order(self, node):
        """
        Stampa i nodi in ordine In-Order (sinistra, radice, destra).
        """
        if node is not None:
            self.dfs_in_order(node.left)
            print(node.value, end=' ')
            self.dfs_in_order(node.right)

    def dfs_post_order(self, node):
        """
        Stampa i nodi in ordine Post-Order (sinistra, destra, radice).
        """
        if node is not None:
            self.dfs_post_order(node.left)
            self.dfs_post_order(node.right)
            print(node.value, end=' ')

# Funzione principale
if __name__ == "__main__":
    print("Gestione Albero Binario")
    tree = BinaryTree()

    while True:
        try:
            valore = input("Inserisci un valore (0000 per terminare): ")
            if valore == "0000":
                break
            direzione = input("Specifica la direzione (es. L per sinistra, R per destra, LL per sinistra-sinistra): ")
            tree.insert(valore, direzione)
        except Exception as e:
            print(f"Errore: {e}")

    while True:
        print("\nScegli il tipo di stampa:")
        print("1. DFS Pre-Order")
        print("2. DFS In-Order")
        print("3. DFS Post-Order")
        print("4. Esci")
        scelta = input("Inserisci la tua scelta: ")

        if scelta == "1":
            print("Stampa Pre-Order:")
            tree.dfs_pre_order(tree.root)
            print()
        elif scelta == "2":
            print("Stampa In-Order:")
            tree.dfs_in_order(tree.root)
            print()
        elif scelta == "3":
            print("Stampa Post-Order:")
            tree.dfs_post_order(tree.root)
            print()
        elif scelta == "4":
            print("Programma terminato.")
            break
        else:
            print("Scelta non valida. Riprova.")
