from solver import Solver

print("******************")
print("*    ORIGINAL    *")
print("******************")
solve = Solver()
print(f"- {solve.clients} clientes foram afetados pelo ocorrido.")
print(f"- {solve.ocurrencies} de ocorrĂȘncias.")
print(f"- {solve.amount} por falta de estoque.")
print(f"- {solve.wallet} por saldo insuficiente.\n")


print("*****************")
print("*    SHUFFLE    *")
print("*****************")
solve = Solver("shuffle")
print(f"- {solve.clients} clientes foram afetados pelo ocorrido.")
print(f"- {solve.ocurrencies} de ocorrĂȘncias.")
print(f"- {solve.amount} por falta de estoque.")
print(f"- {solve.wallet} por saldo insuficiente.\n")
