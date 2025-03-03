
carro = {"marca": "Toyota", "modelo": "Corolla", "ano": 2022}


print(carro["modelo"])  


carro["cor"] = "preto"
print(carro) 


del carro["ano"]
print(carro) 

for chave, valor in carro.items():
    print(f"{chave}: {valor}")
