import warnings
warnings.filterwarnings("ignore")
null = ()
class node:
    def __init__(self,key,data=None,father=null,left=null,right=null):
        self.key = key
        self.data = data # Memorizza i dati (detti dati satellite) associati alla chiave
        self.father = father
        self.left = left
        self.right = right
        
    def insert(self,node):
        '''Inserisce un nuovo nodo nell'albero. La posizione di inserimento
           dipende dalla chiave ed è tale per cui l'albero rimane 
           ordinato per la ricerca.
           Il nodo ha già inseriti i campi key e data.
           La funzione implementa il classico inserimento ricorsivo.
        '''
        if node.key<self.key:
            if self.left is not null:
                self.left.insert(node)
            else:
                node.father = self
                self.left = node
        elif self.right is not null:
            self.right.insert(node)
        else:
            node.father = self
            self.right = node
            
    def __iter__(self):
        '''Inizializza alcune variabili utilizzate per
           la visita dell'albero. E' necessario invoovare prima __iter__
           altrimenti in metodo __next__ (pur definito) non funzionerebbe.
        '''
        self.cursor = self
        self.finish = False
        self.leftexplore = True
        return self
    
    def __next__(self):
        '''Visita (iterativa) in ordine dell'albero.
        '''
        while not self.finish:
            if self.leftexplore:
                while self.cursor.left is not null:
                    self.cursor = self.cursor.left
                self.leftexplore = False
                return self.cursor
            if self.cursor.right is not null:
                self.cursor = self.cursor.right
                self.leftexplore = True
            else: 
                while self.cursor.father is not null and self.cursor == self.cursor.father.right:
                    self.cursor = self.cursor.father 
                if self.cursor.father is null:
                    self.finish = True
                else:
                    self.cursor = self.cursor.father
                    self.leftexplore = False
                    return self.cursor
        raise StopIteration
