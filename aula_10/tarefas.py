last_id = 0


class Tarefa:
    def __init__(self, titulo, descricao=None, prioridade=0, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.concluida = concluida
        global last_id
        last_id += 1
        self.id = last_id

    def simples(self):
        return f"{self.id} - {self.titulo}"

    def detalhada(self):
        return f"ID: {self.id}\ntitulo: {self.titulo}\ndescricao: {self.descricao}\nPrioridade: {self.prioridade}\nconcluida: {self.concluida}"

    def contem(self, conteudo):
        return conteudo in self.titulo or conteudo in self.descricao

    def __lt__(self, other):
        return self.prioridade < other.prioridade


class Lista:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def remover_tarefa(self, id):
        # usando list comprehension
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa.id != id]
        # usando for-each tradicional
        # for tarefa in self.tarefas:
        #     if tarefa.id == id:
        #         self.tarefas.remove(tarefa)
        #         break
        

    def editar_tarefa(self, id, titulo=None, descricao=None, prioridade=None, concluida=None):
        for tarefa in self.tarefas:
            if tarefa.id == id:
                if titulo != None:
                    tarefa.titulo = titulo
                if descricao != None:
                    tarefa.descricao = descricao
                if prioridade != None:
                    tarefa.prioridade = prioridade
                if concluida != None:
                    tarefa.concluida = concluida
                break

    def obter_tarefas(self, filtro=None, apenas_nao_concluidas=False):
        self.tarefas = sorted(self.tarefas, reverse=True)

        tarefas=[]

        # usando list comprehension
        tarefas = [tarefa for tarefa in self.tarefas if not tarefa.concluida]
        # usando for-each tradicional
        # for tarefa in self.tarefas:
        #     if not tarefa.concluida:
        #         tarefas.append(tarefa)
        

        if not apenas_nao_concluidas:
            # usando list comprehension
            tarefas = tarefas + [tarefa for tarefa in self.tarefas if tarefa.concluida]
            # usando for-each tradicional
            # for tarefa in self.tarefas:
            #     if tarefa.concluida:
            #         tarefas.append(tarefa)
            

        if filtro:
            # usando list comprehension
            tarefas = [tarefa for tarefa in tarefas if tarefa.contem(filtro)]
            # usando for-each tradicional
            # for tarefa in tarefas:
            #     if not tarefa.contem(filtro):
            #         tarefas.remove(tarefa)

        return tarefas


if __name__ == "__main__":
    lista_tarefas = Lista()

    tarefa1 = Tarefa("Comprar mantimentos", "Leite, ovos, pão", 2)
    tarefa2 = Tarefa("Fazer exercícios", "Correr 5 km", 1)
    tarefa3 = Tarefa("Ler livro", "Capítulo 3", 3)

    lista_tarefas.adicionar_tarefa(tarefa1)
    lista_tarefas.adicionar_tarefa(tarefa2)
    lista_tarefas.adicionar_tarefa(tarefa3)

    print("Tarefas:")
    for tarefa in lista_tarefas.obter_tarefas():
        print(tarefa.simples())

    lista_tarefas.editar_tarefa(1, concluida=True)

    print("\nTarefas não concluidas:")
    for tarefa in lista_tarefas.obter_tarefas(apenas_nao_concluidas=True):
        print(tarefa.simples())

    print("\nTarefas Detalhadas:")
    for tarefa in lista_tarefas.obter_tarefas():
        print(tarefa.detalhada() + "\n")

    print("\nTarefas filtradas por 'os':")
    for tarefa in lista_tarefas.obter_tarefas(filtro="os"):
        print(tarefa.simples())
