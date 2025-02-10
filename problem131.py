class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def eh_palindromo(inicio: int, fim: int) -> bool:
            while inicio < fim:
                if s[inicio] != s[fim]:
                    return False
                inicio += 1
                fim -= 1
            return True

        def backtrack(inicio: int, caminho_atual: List[str], resultado: List[List[str]]):
            if inicio >= len(s):
                resultado.append(caminho_atual.copy())
                return

            for fim in range(inicio, len(s)):
                if eh_palindromo(inicio, fim):
                    caminho_atual.append(s[inicio:fim+1])
                    backtrack(fim + 1, caminho_atual, resultado)
                    caminho_atual.pop()

        resultado_final = []
        backtrack(0, [], resultado_final)
        return resultado_final  
