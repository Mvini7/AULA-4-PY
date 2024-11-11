def horario (hora):

    if hora >= 4 and hora <= 12:
        print("Bom dia!")
    elif hora >= 13 and hora <= 17:
        print("Boa tarde!")
    elif hora >= 18 and hora <= 3:
        print("Boa noite!")

input_hora = int(input("Digite o horario que você está vendo isso (não pode ser horario quebrado! apenas 12, 13 e etc): "))

horario(input_hora)