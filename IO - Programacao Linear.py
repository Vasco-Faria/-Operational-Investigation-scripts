import pulp


prob = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Variáveis de decisão
x1 = pulp.LpVariable("P1", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("P2", lowBound=0, cat='Integer')
x3 = pulp.LpVariable("P3", lowBound=0, cat='Integer')

# Função objetivo
prob += 33*x1 + 12*x2 + 19*x3, "Total Profit"

# Restrições
prob += 9*x1 + 3*x2 + 5*x3 <= 500  
prob += 5*x1 + 4*x2 <= 350          
prob += 3*x1 + 2*x3 <= 150          

# Restrições adicionais
prob += x2 >= 20        
prob += x1 >=0
prob += x2 >=0
prob += x3 >=0           

# Resolvendo o problema
prob.solve()


print("Status:", pulp.LpStatus[prob.status])
print("Lucro máximo:", pulp.value(prob.objective ))
print("\n")
print("Quantidades ótimas a produzir:")
for v in prob.variables():
    print(v.name, "=", v.varValue)