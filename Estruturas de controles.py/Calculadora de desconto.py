def calcular_desconto(valor):
    if valor >= 500:
        return valor * 0.20  # 20% de desconto
    elif valor >= 200:
        return valor * 0.10  # 10% de desconto
    else:
        return valor * 0.05  # 5% de desconto

while True:
    try:
        valor_produto = float(input("Digite o valor do produto: ").replace(",", "."))
        desconto = calcular_desconto(valor_produto)
        print(f"Desconto aplicado: R${desconto:.2f}")
        print(f"Valor final: R${valor_produto - desconto:.2f}")
        break
    except ValueError:
        print("Entrada inválida! Digite um número válido.")