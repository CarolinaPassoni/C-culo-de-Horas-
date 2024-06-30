from datetime import datetime, timedelta
import pandas as pd

# Definição de colaboradores e seus horários
colaboradores = [
    {
        "nome": "Jose",
        "matricula": 1600,
        "horarios": ["05:15", "12:00", "13:00", "17:00"]
    },
    {
        "nome": "Paulo",
        "matricula": 1705,
        "horarios": ["05:00", "11:00", "12:00", "19:30"]
    },
    {
        "nome": "Lucas",
        "matricula": 1706,
        "horarios": ["06:00", "12:00", "13:00", "18:00"]
    },
    {
        "nome": "Cabral",
        "matricula": 17060,
        "horarios": ["05:30", "11:00", "12:00", "17:00"]
    },
    {
        "nome": "Carolina",
        "matricula": 1092,
        "horarios": ["07:00", "12:00", "13:00", "18:00"]  # Horários de trabalho de segunda a domingo 
    }
]

# Função para calcular as horas trabalhadas
def calcular_horas_trabalhadas(horarios):
    total_horas = timedelta()
    for i in range(0, len(horarios) - 1, 2):
        entrada = datetime.strptime(horarios[i], "%H:%M")
        saida = datetime.strptime(horarios[i + 1], "%H:%M")
        total_horas += (saida - entrada)
    return total_horas

# Função para calcular horas extras
def calcular_horas_extras(horas_trabalhadas, jornada=8):
    jornada_horas = timedelta(hours=jornada)
    if horas_trabalhadas > jornada_horas:
        return horas_trabalhadas - jornada_horas
    else:
        return timedelta()

# Calculando e mostrando as horas extras para cada colaborador
data = []
for colaborador in colaboradores:
    horas_trabalhadas = calcular_horas_trabalhadas(colaborador["horarios"])
    horas_extras = calcular_horas_extras(horas_trabalhadas)
    data.append({
        'Nome': colaborador["nome"],
        'Matrícula': colaborador["matricula"],
        'Horas Trabalhadas': str(horas_trabalhadas),
        'Horas Extras': str(horas_extras)
    })
    print(f'Colaborador: {colaborador["nome"]} - Matrícula: {colaborador["matricula"]}')
    print(f'Horas Trabalhadas: {horas_trabalhadas}')
    print(f'Horas Extras: {horas_extras}')
    print('-' * 30)

# Criando o DataFrame
df = pd.DataFrame(data)

# Salvando o DataFrame em um arquivo Excel
file_path = "horas_colaboradores_atualizado.xlsx"
df.to_excel(file_path, index=False)

print(f'Arquivo Excel salvo em: {file_path}')
