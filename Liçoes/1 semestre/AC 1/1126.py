dia_compra = str(input())
dia_espera = int(input())
semana = ["domingo", "segunda", "terca", "quarta", "quinta", "sexta", "sabado"]
semana1 ={"domingo": 0, "segunda": 1, "terca": 2, "quarta": 3, "quinta": 4, "sexta": 5, "sabado": 6}
if dia_compra in semana and dia_espera == 0 and dia_espera >= 0 and dia_espera <= 6:
  print("chega hoje!")
elif dia_compra in semana and dia_espera >= 0 and dia_espera <= 6:
  print("sera entregue {}".format(semana[(semana1[dia_compra] + dia_espera) - 7]))
