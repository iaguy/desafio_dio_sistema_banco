class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.saques_restantes = 3

    def mostrar_menu(self):
        print("1. Ver saldo")
        print("2. Ver extrato")
        print("3. Sacar")
        print("4. Depositar")
        print("5. Sair")

    def ver_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    def ver_extrato(self):
        print("Extrato:")
        for transacao in self.extrato:
            print(transacao)

    def sacar(self, valor):
        if self.saques_restantes > 0 and valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R${valor:.2f}")
            self.saques_restantes -= 1
            print("Saque realizado com sucesso.")
        else:
            print("Não foi possível realizar o saque.")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor:.2f}")
            print("Depósito realizado com sucesso.")
        else:
            print("Não foi possível realizar o depósito.")

    def executar(self):
        while True:
            self.mostrar_menu()
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.ver_saldo()
            elif escolha == '2':
                self.ver_extrato()
            elif escolha == '3':
                if self.saques_restantes > 0:
                    valor = float(input("Digite o valor do saque: "))
                    self.sacar(valor)
                else:
                    print("Você atingiu o limite de saques.")
            elif escolha == '4':
                valor = float(input("Digite o valor do depósito: "))
                self.depositar(valor)
            elif escolha == '5':
                print("Saindo...")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    minha_conta = ContaBancaria()
    minha_conta.executar()
