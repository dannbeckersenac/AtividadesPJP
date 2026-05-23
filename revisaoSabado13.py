import time

tanque = 125
tempo_escoamento = 5
tempo_total_escoamento = 0

while tanque > 0:
    print("Escoando 25 litros...")
    time.sleep(tempo_escoamento)
    tanque = tanque - 25
    tempo_total_escoamento = tempo_total_escoamento + tempo_escoamento
    print(f"Tanque atual: {tanque}")

print(f"Tempo total que levou para escoar os {tanque} litros foi de {tempo_total_escoamento} segundos")