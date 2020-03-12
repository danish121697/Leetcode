def addToArrayForm(self, A, K):
        x = int(''.join([str(i) for i in A]))
        num = x+K
        return [int(i) for i in str(num)]
