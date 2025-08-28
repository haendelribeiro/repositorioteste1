# Programa para analise de dados de altura e genero
# Disciplina: Tecnologias para Front-End com Logica Imperativa
# TED 1 - Atividade Individual

# o programa deve solicitar a altura e o genero (Masculino ou Feminino) de 15 pessoas.
# as alturas devem ser armazenadas em uma lista ou variavel apropriada.
# o genero deve ser armazenado de forma que voce possa contar quantas pessoas sao do genero Feminino.
# calcular e exibir a maior e a menor altura entre as 15 pessoas.
def main():
    print("=" * 60)
    print("ANALISE DE DADOS DE ALTURA E GENERO")
    print("=" * 60)
    print()

    # 15 pessoas (nome, altura, genero)
    pessoas = [
        {"nome": "Alice", "altura": 1.65, "genero": "Feminino"},
        {"nome": "Bruno", "altura": 1.80, "genero": "Masculino"},
        {"nome": "Carla", "altura": 1.70, "genero": "Feminino"},
        {"nome": "Daniel", "altura": 1.75, "genero": "Masculino"},
        {"nome": "Eduarda", "altura": 1.60, "genero": "Feminino"},
        {"nome": "Felipe", "altura": 1.85, "genero": "Masculino"},
        {"nome": "Gabriela", "altura": 1.68, "genero": "Feminino"},
        {"nome": "Henrique", "altura": 1.90, "genero": "Masculino"},
        {"nome": "Isabela", "altura": 1.62, "genero": "Feminino"},
        {"nome": "João", "altura": 1.78, "genero": "Masculino"},
        {"nome": "Karina", "altura": 1.72, "genero": "Feminino"},
        {"nome": "Lucas", "altura": 1.82, "genero": "Masculino"},
        {"nome": "Mariana", "altura": 1.66, "genero": "Feminino"},
        {"nome": "Nicolas", "altura": 1.88, "genero": "Masculino"},
        {"nome": "Olivia", "altura": 1.64, "genero": "Feminino"}
    ]

    # exibir dados coletados
    print("DADOS COLETADOS:")
    print("-" * 40)
    for i, pessoa in enumerate(pessoas, 1):
        print(f"{i:2d}. {pessoa['nome']:10} - {pessoa['altura']:.2f}m - {pessoa['genero']}")
    print()

    # alturas e gêneros
    alturas = [pessoa['altura'] for pessoa in pessoas]
    generos = [pessoa['genero'] for pessoa in pessoas]

    # calculos
    maior_altura = max(alturas)
    menor_altura = min(alturas)

    # cncontrar pessoas de maior e menor altura
    pessoa_maior_altura = [p for p in pessoas if p['altura'] == maior_altura][0]
    pessoa_menor_altura = [p for p in pessoas if p['altura'] == menor_altura][0]

    # alcular média de altura dos homens
    alturas_masculino  = [p['altura'] for p in pessoas if p['genero'] == 'Masculino']
    media_masculino = sum(alturas_masculino) / len(alturas_masculino) if alturas_masculino else 0

    # mulheres
    numero_feminino = sum(1 for p in pessoas if p['genero'] == 'Feminino')

    # resultados
    print("RESULTADOS DA ANÁLISE:")
    print("=" * 40)
    print(f"→ Maior altura: {maior_altura:.2f}m ({pessoa_maior_altura['nome']})")
    print(f"→ Menor altura: {menor_altura:.2f}m ({pessoa_menor_altura['nome']})")
    print(f"→ Média de altura masculina: {media_masculino:.2f}m")
    print(f"→ Número de pessoas do gênero feminino: {numero_feminino}")
    print()

    # Estatísticas adicionais
    print("ESTATÍSTICAS ADICIONAIS:")
    print("-" * 30)
    print(f"Total de pessoas analisadas: {len(pessoas)}")
    print(f"Homens: {len(alturas_masculino)}")
    print(f"Mulheres: {numero_feminino}")
    print(f"Altura média geral: {sum(alturas)/len(alturas):.2f}m")
    print()

    # faixa de altura
    print("DISTRIBUIÇÃO POR FAIXA DE ALTURA:")
    print("-" * 35)
    baixa = [p for p in pessoas if p['altura'] < 1.70]
    media = [p for p in pessoas if 1.70 <= p['altura'] < 1.80]
    alta = [p for p in pessoas if p['altura'] >= 1.80]

    print(f"Baixa (<1.70m): {len(baixa)} pessoas")
    print(f"Média (1.70-1.79m): {len(media)} pessoas")
    print(f"Alta (≥1.80m): {len(alta)} pessoas")

if __name__ == "__main__":
    main()

