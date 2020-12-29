##
# 
# Пошук слова в матриці символів
# Виконано за допомогою алгоритму схожого на рекурсивний варіант пошуку вшир
#  
#
##

from math import sqrt
import typing as t

class Matrix():
    def __init__(self, matrix: list):
        """
        symbols - наші літери
        _matrixDim - n розмірність матриці (nxn)
        """
        
        self.symbols = matrix
        self._matrixDim = int(sqrt(len(matrix)))
    
    @property
    def symbols(self):
        return self._symbols

    @symbols.setter
    def symbols(self, value: list):
        side = sqrt(len(value))
        if side % 1 != 0:
            raise ValueError("Matrix has not a perfect square side")
        self._symbols = value

    def isAtTopEdge(self, index: int) -> bool:
        if index in range(0, self._matrixDim): 
            return True
       
    def isAtDownEdge(self, index: int) -> bool:
        symbols_length = len(self.symbols)
        if index in range(symbols_length - self._matrixDim - 1, symbols_length):
            return True
        else:
            return False

    def isAtRightEdge(self, index: int) -> bool:
        if (index + 1) % self._matrixDim == 0:
            return True
        else:
            return False
    
    def isAtLeftEdge(self, index: int) -> bool:
        if index % self._matrixDim == 0:
            return True
        else:
            return False

class MatrBFS():
    def __init__(self, matrix: Matrix, word: str):
        self._matrix = matrix 
        self._word = word
        self._start = -1
        self._wrongStart = []
        self._current = 0

    def moveLeft(self) -> int:
        return self._current - 1
    
    def moveRight(self) -> int:
        return self._current + 1

    def moveUp(self) -> int:
        return self._current - self._matrix._matrixDim 
    
    def moveDown(self) -> int:
        return self._current + self._matrix._matrixDim
    

    # Додає варіант продовження знаходження слова в чергу
    def _appedQueue(self, queue: list, symbol: str, step: int):
        if self._matrix.symbols[step] == symbol:
            queue.append(step)

    # Знаходження початкового символу в матриці
    def _findStart(self):
        for i in range(len(self._matrix.symbols)):
            if i in self._wrongStart:
                continue
            if self._matrix.symbols[i] == self._word[0]:
                self._start = i
        if self._start == -1:
            raise ValueError(f"Matrix doesn't have starting symbol of the word {self._word} - {self._word[0]} \nor matrix doesn't contain the word {self._word}")
        else:
            self._current = self._start
        return self._start         
        
    # перетворення валідного індексу клітинки в шлях
    def _convertIndexToTable(self, index: int) -> str:
        return "[" + str(index // self._matrix._matrixDim) + "," + str(index % self._matrix._matrixDim) + "]" + "->"

    # пошук слова серед матриці, рухаємося по матриці залежно від клітинки в якій ми знаходимося
    # Рекурсивно викликаємо, відповідно для декількох варіантів виходу для клітинки чи одного
    def _findWord(self, path: str, temp_word, queue, word, word_index) -> t.Tuple[str, str, bool]:
        """
        path - шлях для слова 
        temp_word - слово за яким ми перевіряємо правильність рівність із шуканим словом 
        queue - черга варіатів продовження шляху для слова 
        word - шукане слово 
        word_index - індекс символу в шуканому слові на цьому рекурсивному виклику 
        """

        if len(queue) == 0:

            if word == temp_word:
                return path, temp_word, True
            else:
                return path, temp_word, False

        if len(queue) == 1:
            
            self._current = queue.pop(0)
            path += self._convertIndexToTable(self._current)
            temp_word += self._matrix.symbols[self._current]
            word_index += 1

            if word_index > len(word) - 1:
                return path, temp_word, True

            if self._matrix.isAtTopEdge(self._current):

                        if self._current == 0:
                
                            step = self.moveDown()
                            self._appedQueue(queue, word[word_index], step)
        
                            step = self.moveRight()
                            self._appedQueue(queue, word[word_index], step)

                        elif self._current == self._matrix._matrixDim - 1:

                            step = self.moveDown()
                            self._appedQueue(queue, word[word_index], step)

                            step = self.moveLeft()
                            self._appedQueue(queue, word[word_index], step)

                        else:
                            
                            step = self.moveDown()
                            self._appedQueue(queue, word[word_index], step)

                            step = self.moveLeft()
                            self._appedQueue(queue, word[word_index], step)

                            step = self.moveRight()
                            self._appedQueue(queue, word[word_index], step)

            elif self._matrix.isAtDownEdge(self._current):

                        if self._current == len(self._matrix.symbols) - 1:

                            step = self.moveUp()
                            self._appedQueue(queue, word[word_index], step)

                            step = self.moveLeft()
                            self._appedQueue(queue, word[word_index], step)

                        elif self._current == len(self._matrix.symbols) - self._matrix._matrixDim:

                            step = self.moveUp() 
                            self._appedQueue(queue, word[word_index], step)

                            step = self.moveRight()
                            self._appedQueue(queue, word[word_index], step)

                        else:
                            
                            step = self.moveUp() 
                            self._appedQueue(queue, word[word_index], step)

                            step = self.moveRight()
                            self._appedQueue(queue, word[word_index], step)

                            step = self.moveLeft()
                            self._appedQueue(queue, word[word_index], step)

            elif self._matrix.isAtRightEdge(self._current):

                            step = self.moveUp()
                            self._appedQueue(queue, word[word_index], step)

                            step = self.moveLeft()
                            self._appedQueue(queue, word[word_index], step)

                            step = self.moveDown()
                            self._appedQueue(queue, word[word_index], step)

            elif self._matrix.isAtLeftEdge(self._current):

                            step = self.moveUp()
                            self._appedQueue(queue, word[word_index], step)

                            step = self.moveRight()
                            self._appedQueue(queue, word[word_index], step)

                            step = self.moveDown()
                            self._appedQueue(queue, word[word_index], step)

            else:

                            step = self.moveUp()
                            self._appedQueue(queue, word[word_index], step)

                            step = self.moveRight()
                            self._appedQueue(queue, word[word_index], step)

                            step = self.moveDown()
                            self._appedQueue(queue, word[word_index], step)

                            step = self.moveLeft()
                            self._appedQueue(queue, word[word_index], step)

            return self._findWord(path, temp_word, queue, word, word_index)

        else:
            for start in queue:
                return self._findWord(path, temp_word, [start], word, word_index)

    # алгоритм схожий на пошук вшир: знаходимо початок слова в матриці і шукаємо, 
    # поки не отримаємо шукане слов або викинеться помилка, 
    # return: шукане слово, та шлях у вигляді [a, b] -> [c, d] -> ....
    def _BFS(self):
        flag = False
        find_word = ""
        while find_word != self._word:
            self._start = self._findStart()
            queue = [self._start]
            path = ""
            word_index = 0
            path, find_word, flag = self._findWord(path, find_word, queue, self._word, word_index)
            self._wrongStart.append(self._start) 
            self._start = -1 
            

        return path, find_word, flag
    
    def getPathWord(self):
        path, find_word, flag = self._BFS()
        if flag == False:
            path += "Wrong path or matrix doesn't contain word"
        print(path + "\n" + find_word)
        

if __name__ == "__main__":
    try:
        litterals = "QLGNAEKIRLRNGEAE" 
        word_matrix = list(litterals)
        word = "GEAE"
        matrix = Matrix(word_matrix)
        BFS_INTERFACE = MatrBFS(matrix, word)
        BFS_INTERFACE.getPathWord()
    except ValueError as e:
        massage = e
        print(massage)
        

    
