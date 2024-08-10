def before_all(context):
    # Configurações antes de qualquer cenário
    print("Iniciando os testes...")

def after_all(context):
    # Limpeza após todos os cenários
    print("Todos os testes concluídos.")

def before_scenario(context, scenario):
    # Configurações antes de cada cenário
    print(f"Executando o cenário: {scenario.name}")

def after_scenario(context, scenario):
    # Limpeza após cada cenário
    print(f"Concluído o cenário: {scenario.name}")
