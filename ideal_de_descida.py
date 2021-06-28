

#Cálculo de ideal de descida


while True:
   
   velocidade=float(input('\nVelocidade de cruzeiro em nós '))
   print(f'{velocidade} nós\n')
   
   altitude=float(input('Altitude de cruzeiro em ft '))
   print(f'{altitude} ft\n')
   
   altitude_descida=float(input('Altitude de descida em ft '))
   print(f'{altitude_descida} ft\n')
   
   razao=float(input('Razão de descida em ft/min '))
   print(f'{razao} ft/min\n')

   tempo=(altitude-altitude_descida)/(razao*60)

   distancia=velocidade*tempo

   print(f'Ideal de descida\n {distancia} MN\n')

   print('Deseja fazer novo cálculo? sim/nao\n')
   aux=input('')

   while aux!='sim' and aux!='não':
      print('\nResposta inválida\n')
      aux=input('\nDeseja fazer novo cálculo? sim/não\n')

   if aux=='não':
      break

   print('\n****************************************\n************\n******')
