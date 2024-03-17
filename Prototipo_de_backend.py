# Implementação do encapsulamento

class Usuario:
    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email
        self.__agendamentos = []

    def agendar_consulta(self, data, horario):
        novo_agendamento = Agendamento(data, horario)
        self.__agendamentos.append(novo_agendamento)
        return novo_agendamento

    def mostrar_agendamentos(self):
        for agendamento in self.__agendamentos:
            agendamento.mostrar_detalhes()

# Implementação da herança

class UsuarioPremium(Usuario):
    def __init__(self, nome, idade, email):
        super().__init__(nome, idade, email)
        self.__premium = True

# Implementação do polimorfismo

class Agendamento:
    def __init__(self, data, horario):
        self.__data = data
        self.__horario = horario

    def mostrar_detalhes(self):
        print(f"Data: {self.__data}")
        print(f"Horário: {self.__horario}")

class AgendamentoPremium(Agendamento):
    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print("Usuário Premium: Sim")

# Implementação do polimorfismo usando sobrescrição de métodos

class AplicativoPssPlus:
    def __init__(self):
        self.__usuarios = []

    def criar_usuario(self, nome, idade, email, premium=False):
        if premium:
            novo_usuario = UsuarioPremium(nome, idade, email)
        else:
            novo_usuario = Usuario(nome, idade, email)
        self.__usuarios.append(novo_usuario)
        return novo_usuario

    def mostrar_usuarios(self):
        for usuario in self.__usuarios:
            print(f"Nome: {usuario.__nome}")
            print(f"Email: {usuario.__email}")
            print(f"Idade: {usuario.__idade}")
            print(f"Premium: {'sim' if usuario.__premium else 'não'}")
            usuario.mostrar_agendamentos()

# Exemplo de uso do aplicativo PssPlus
app_pss_plus = AplicativoPssPlus()

# Criar dois usuários, um premium e um não premium
usuario1 = app_pss_plus.criar_usuario("João", 30, "joao@email.com", premium=True)
usuario2 = app_pss_plus.criar_usuario("Maria", 25, "maria@email.com")

# Agendar consultas para os usuários
usuario1.agendar_consulta("2023-10-15", "15:00")
usuario2.agendar_consulta("2023-10-10", "10:30")

# Mostrar informações dos usuários e seus agendamentos
app_pss_plus.mostrar_usuarios()
