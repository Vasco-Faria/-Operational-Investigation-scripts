import pulp

prob = pulp.LpProblem("Minimize_Profit", pulp.LpMinimize)

# Variáveis de decisão
x1 = pulp.LpVariable("P1", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("P2", lowBound=0, cat='Integer')


# Função objetivo
prob += 30*x1 + 25*x2, "Total Profit"

# Restrições
prob += 1*x1 + 1*x2 >= 5  
prob += 2*x1 + 3*x2 >= 12          
prob += 6*x1 + 3*x2 >= 18         

# Restrições adicionais  
prob += x1 >=0
prob += x2 >=0         

# Resolvendo o problema
prob.solve()

print("Status:", pulp.LpStatus[prob.status])
print("Lucro mínimo:", pulp.value(prob.objective))
print("\n")
print("Quantidades ótimas a produzir:")
for v in prob.variables():
    print(v.name, "=", v.varValue)
