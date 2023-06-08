import os

class EnumeraArquivos:
    def __init__(self):
        self.resultado = {}

    def enumerar(self, diretorio):
        for item in os.listdir(diretorio):
            path = os.path.join(diretorio, item)
            if os.path.isdir(path):
                self.enumerar(path)
            else:
                tamanho = os.path.getsize(path)
                if not tamanho in self.resultado:
                    self.resultado[tamanho] = []
                self.resultado[tamanho].append(path)
        return self.resultado

e = EnumeraArquivos()
resultado = e.enumerar(r'D:\tools\AutoIt')

for tamanho in sorted(resultado.keys())[-10:]:
    print ('[%d]: %s' % (tamanho, resultado[tamanho]))