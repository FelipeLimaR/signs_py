

                                                      ###MENU ENTRADA \/


                                                          #DIA \/
dia = int(input("Digite o dia em que você nasceu: "))
while dia >31:
  dia = int(input("Número inválido! Digite outra data: "))
                                                          #DIA /\

  
                                                          #MÊS \/
mes = int(input("Digite o mês em que você nasceu: "))
while mes >12:
  mes = int(input("O ano tem apenas 12 meses! Digite outro número: "))  
                                                          #MÊS /\

ano = int(input("Digite o ano em que você nasceu: "))

                                                          #HORA \/
hora_nascimento = int(input("Digite a hora em que você nasceu: "))
while hora_nascimento >24:
  hora_nascimento = int(input("Hora inválida! Digite uma hora valida: "))
                                                          #HORA /\

                                                          #MINUTOS \/
minutos_nascimento = int(input("Digite os minutos: "))
while minutos_nascimento >59:
  minutos_nascimento = int(input("Minutos invalidos! Digite um número válido: "))
                                                          #MINUTOS /\


                                                      ###MENU ENTRADA/\


                                                    ###MENU VALORES \/
hora    = hora_nascimento
minutos = minutos_nascimento


x         = str("Seu signo é:")
y         = str("Seu ascendente é:")
lua       = str("Sua lua é em:")
venus1    = str("Sua Venus é em:")
marte1    = str("Seu Marte é em:")
jupiter1  = str("Seu Júpiter é em:")
saturno1  = str("Seu Saturno é em:")
urano1    = str("Seu Urano é em:")
netuno1   = str("Seu Netuno é em:")
plutao1   = str("Seu Plutão é em:")


s1  = str("Áries")
s2  = str("Touro")
s3  = str("Gêmeos")
s4  = str("Câncer")
s5  = str("Leão")
s6  = str("Virgem")
s7  = str("Libra")
s8  = str("Escorpião")
s9  = str("Sagitário")
s10 = str("Capricórnio")
s11 = str("Aquário")
s12 = str("Peixes")

                                                          ###MENU VALORES /\




                                                              #CAPRCÓRNIO   \/

          ###JANEIRO  \/
  
if mes == 1 and dia <=20:
  signo = s10


     ###VENUS \/
  ### Ás 13:36 do dia 13 de Janeiroo Vênus entra em Capricórnio ### 
  if ano == 1990 and dia < 13:
    venus2 = s9
  if ano == 1990 and dia == 13 and hora <= 13 and minutos < 36:
    venus2 = s9
  if ano == 1990 and dia == 13 and hora == 13 and minutos >=36:
    venus2 = s10
  if ano == 1990 and dia == 13 and hora > 13:
    venus2 = s10
  if ano == 1990 and dia > 13:
    venus2 = s10
    ###VENUS /\

    ###ASCENDENTE \/    
  ascendente = (hora_nascimento - 6) // 2
    
  if hora_nascimento == 0:
    ascendente = s7   
  if hora_nascimento == 1:
    ascendente = s7
  if hora_nascimento == 2:
    ascendente = s8   
  if hora_nascimento == 3:
    ascendente = s8
  if hora_nascimento == 4:
    ascendente = s9
  if hora_nascimento == 5:
    ascendente = s9

  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:    
    ascendente = signo
    
  if ascendente == 1:
    ascendente = s11
  if ascendente == 2:
    ascendente = s12
  if ascendente == 3:
    ascendente = s1
  if ascendente == 4:
    ascendente = s2  
  if ascendente == 5:
    ascendente = s3   
  if ascendente == 6:
    ascendente = s4
  if ascendente == 7:
    ascendente = s5
  if ascendente == 8:
    ascendente = s6
  if ascendente == 9:
    ascendente = s7
  if ascendente == 10:
    ascendente = s8
  if ascendente == 11:
    ascendente = s9
  if ascendente == 12:
    ascendente = s10
    ###ASCENDENTE/\

 

    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2)

                                                                #CAPRICÓRNIO  /\
                                                                #AQUÁRIO      \/
  
          #JANEIRO  \/
  
if mes == 1 and dia >=21:
  signo = s11

  
    ###VENUS \/
  if ano == 1990 and mes == 1:
    venus2 = s10
    ###VENUS /\


    ###ASCENDENTE \/
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s8    
  if hora_nascimento == 1:
    ascendente = s8
  if hora_nascimento == 2:
    ascendente = s9
  if hora_nascimento == 3:
    ascendente = s9
  if hora_nascimento == 4:
    ascendente = s10
  if hora_nascimento == 5:
    ascendente = s10

  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo

  if ascendente == 1:
    ascendente = s12
  if ascendente == 2:
    ascendente = s1
  if ascendente == 3:
    ascendente = s2 
  if ascendente == 4:
    ascendente = s3   
  if ascendente == 5:
    ascendente = s4
  if ascendente == 6:
    ascendente = s5
  if ascendente == 7:
    ascendente = s6
  if ascendente == 8:
    ascendente = s7
  if ascendente == 9:
    ascendente = s8
  if ascendente == 10:
    ascendente = s9
  if ascendente == 11:
    ascendente = s10
  if ascendente == 12:
    ascendente = s11
    ###ASCENDENTE /\


  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!")

          #FEVEREIRO  \/
  
if mes == 2 and dia <=18:
  signo = s11


    ###VENUS \/
  if ano == 1990 and mes == 2:
    venus2 = s10
    ###VENUS /\
    
  
    ###ASCENDENTE \/
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s8
  if hora_nascimento == 1:
    ascendente = s8
  if hora_nascimento == 2:
    ascendente = s9
  if hora_nascimento == 3:
    ascendente = s9
  if hora_nascimento == 4:
    ascendente = s10
  if hora_nascimento == 5:
    ascendente = s10
    
  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo

  if ascendente == 1:
    ascendente = s12
  if ascendente == 2:
    ascendente = s1
  if ascendente == 3:
    ascendente = s2
  if ascendente == 4:
    ascendente = s3
  if ascendente == 5:
    ascendente = s4
  if ascendente == 6:
    ascendente = s5
  if ascendente == 7:
    ascendente = s6
  if ascendente == 8:
    ascendente = s7
  if ascendente == 9:
    ascendente = s8
  if ascendente == 10:
    ascendente = s9
  if ascendente == 11:
    ascendente = s10
  if ascendente == 12:
    ascendente = s11
    ###ASCENDENTE /\
    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!")
  
                                                              #AQUÁRIO      /\
                                                              #PEIXES       \/

if mes == 2 and dia >29:
  dia = int(input("Fevereiro tem apenas 29 dias. Digite outra data: "))
  
  while dia > 29:
    dia = int(input("Fevereiro tem apenas 29 dias. Digite outra data: "))

          #FEVEREIRO  \/    
    
if mes == 2 and dia >=19:
  signo = s12


      ###VENUS \/
  if ano == 1990 and mes == 2:
    venus2 = s10
      ###VENUS /\

    ###ASCENDENTE \/
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s9
  if hora_nascimento == 1:
    ascendente = s9
  if hora_nascimento == 2:
    ascendente = s10
  if hora_nascimento == 3:
    ascendente = s10
  if hora_nascimento == 4:
    ascendente = s11
  if hora_nascimento == 5:
    ascendente = s11
    
  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo

  if ascendente == 1:
    ascendente = s1
  if ascendente == 2:
    ascendente = s2
  if ascendente == 3:
    ascendente = s3
  if ascendente == 4:
    ascendente = s4
  if ascendente == 5:
    ascendente = s5
  if ascendente == 6:
    ascendente = s6
  if ascendente == 7:
    ascendente = s7
  if ascendente == 8:
    ascendente = s8
  if ascendente == 9:
    ascendente = s9
  if ascendente == 10:
    ascendente = s10
  if ascendente == 11:
    ascendente = s11
  if ascendente == 12:
    ascendente = s12
    ###ASCENDENTE /\
    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!")


          #MARÇO  \/  
if mes == 3 and dia <=20:
  signo = s12
  

     ###VENUS \/
    ### Ás 17:52 do dia 03 de março Vênus entra em Aquário ### 
  if ano == 1990 and dia < 3:
    venus2 = s10
  if ano == 1990 and dia == 3 and hora <= 17 and minutos < 52:
    venus2 = s10
  if ano == 1990 and dia == 3 and hora == 17 and minutos >= 52:
    venus2 = s11
  if ano == 1990 and dia == 3 and hora > 17:
    venus2 = s11
  if ano == 1990 and dia > 3:
    venus2 = s11
    ###VENUS /\
    

    ###ASCENDENTE \/
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s9
  if hora_nascimento == 1:
    ascendente = s9
  if hora_nascimento == 2:
    ascendente = s10
  if hora_nascimento == 3:
    ascendente = s10
  if hora_nascimento == 4:
    ascendente = s11
  if hora_nascimento == 5:
    ascendente = s11

  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo

  if ascendente == 1:
    ascendente = s1
  if ascendente == 2:
    ascendente = s2
  if ascendente == 3:
    ascendente = s3
  if ascendente == 4:
    ascendente = s4
  if ascendente == 5:
    ascendente = s5
  if ascendente == 6:
    ascendente = s6
  if ascendente == 7:
    ascendente = s7
  if ascendente == 8:
    ascendente = s8
  if ascendente == 9:
    ascendente = s9
  if ascendente == 10:
    ascendente = s10
  if ascendente == 11:
    ascendente = s11
  if ascendente == 12:
    ascendente = s12
    ###ASCENDENTE /\
    
    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!")

  
                                                              #PEIXES       /\
                                                              #ÁRIES        \/

  
          #MARÇO  \/
  
if mes == 3 and dia >=21:
  signo = s1

    ###VENUS \/
  if ano == 1990 and mes == 3:
    venus2 = s11
    ###VENUS /\

  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s10
  if hora_nascimento == 1:
    ascendente = s10
  if hora_nascimento == 2:
    ascendente = s11
  if hora_nascimento == 3:
    ascendente = s11
  if hora_nascimento == 4:
    ascendente = s12
  if hora_nascimento == 5:
    ascendente = s12
    
  if hora_nascimento == 6:
    ascendente = signo
  if hora_nascimento == 7:
    ascendente = signo

  if ascendente == 1:
    ascendente = s2
  if ascendente == 2:
    ascendente = s3
  if ascendente == 3:
    ascendente = s4
  if ascendente == 4:
    ascendente = s5
  if ascendente == 5:
    ascendente = s6
  if ascendente == 6:
    ascendente = s7
  if ascendente == 7:
    ascendente = s8
  if ascendente == 8:
    ascendente = s9
  if ascendente == 9:
    ascendente = s10
  if ascendente == 10:
    ascendente = s11
  if ascendente == 11:
     ascendente = s12
  if ascendente == 12:
    ascendente = s12

  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!")

          #ABRIL \/

if mes == 4 and dia <=20:
  signo = s1

       ###VENUS \/
    ### Ás 03:52 do dia 04 de Maio Vênus entra em Áries### 
  if ano == 1990 and dia < 4:
    venus2 = s12
  if ano == 1990 and dia == 4 and hora <= 3 and minutos < 52:
    venus2 = s12
  if ano == 1990 and dia == 4 and hora == 3 and minutos >= 52:
    venus2 = s1
  if ano == 1990 and dia == 4 and hora > 3:
    venus2 = s1
  if ano == 1990 and dia > 4:
    venus2 = s1
    ###VENUS /\


    ###ASCENDENTE \/
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s10
  if hora_nascimento == 1:
    ascendente = s10
  if hora_nascimento == 2:
    ascendente = s11
  if hora_nascimento == 3:
    ascendente = s11
  if hora_nascimento == 4:
    ascendente = s12
  if hora_nascimento == 5:
    ascendente = s12
    
  if hora_nascimento == 6:
    ascendente = signo   
  if hora_nascimento == 7:
    ascendente = signo

  if ascendente == 1:
    ascendente = s2
  if ascendente == 2:
    ascendente = s3
  if ascendente == 3:
    ascendente = s4    
  if ascendente == 4:
    ascendente = s5
  if ascendente == 5:
    ascendente = s6
  if ascendente == 6:
    ascendente = s7
  if ascendente == 7:
    ascendente = s8
  if ascendente == 8:
    ascendente = s9
  if ascendente == 9:
    ascendente = s10
  if ascendente == 10:
    ascendente = s11
  if ascendente == 11:
     ascendente = s12
  if ascendente == 12:
    ascendente = s1
    ###ASCENDENTE /\

    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!")

  
                                                              #ÁRIES  /\
                                                              #TOURO  \/

  
if mes == 4 and dia >30:
  dia = int(input("Abril tem apenas 30 dias. Digite outra data: "))
  while dia >30:
    dia = int(input("Abril tem apenas 30 dias. Digite outra data: "))

          #ABRIL  \/

if mes == 4 and dia >=21:
  signo = s2

       ###VENUS \/
    ### Ás 10:13 do dia 30 de Maio Vênus entra em Touro### 
  if ano == 1990 and dia < 30:
    venus2 = s1
  if ano == 1990 and dia == 30 and hora <= 10 and minutos < 13:
    venus2 = s1
  if ano == 1990 and dia == 30 and hora == 10 and minutos >= 13:
    venus2 = s2
  if ano == 1990 and dia == 30 and hora > 10:
    venus2 = s2
  if ano == 1990 and dia > 30:
    venus2 = s2
    ###VENUS /\

    
    ###ASCENDENTE /\
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s11
  if hora_nascimento == 1:
    ascendente = s11
  if hora_nascimento == 2:
    ascendente = s12
  if hora_nascimento == 3:
    ascendente = s12
  if hora_nascimento == 4:
    ascendente = s1
  if hora_nascimento == 5:
    ascendente = s1
    
  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo
    
  if ascendente == 1:
    ascendente = s3
  if ascendente == 2:
    ascendente = s4    
  if ascendente == 3:
    ascendente = s5
  if ascendente == 4:
    ascendente = s6
  if ascendente == 5:
    ascendente = s7
  if ascendente == 6:
    ascendente = s8
  if ascendente == 7:
    ascendente = s9   
  if ascendente == 8:
    ascendente = s10
  if ascendente == 9:
    ascendente = s11
  if ascendente == 10:
     ascendente = s12
  if ascendente == 11:
    ascendente = s1
  if ascendente == 12:
    ascendente = s2
    ###ASCENDENTE /\

    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!")
  
          #MAIO   \/

if mes == 5 and dia <=20:
  signo = s2

     ###VENUS \/
  if ano == 1990 and mes == 5:
    venus2 = s2
    ###VENUS /\


    ###ASCENDENTE \/
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s11
  if hora_nascimento == 1:
    ascendente = s11
  if hora_nascimento == 2:
    ascendente = s12
  if hora_nascimento == 3:
    ascendente = s12
  if hora_nascimento == 4:
    ascendente = s1
  if hora_nascimento == 5:
    ascendente = s1
    
  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo
    
  if ascendente == 1:
    ascendente = s3
  if ascendente == 2:
    ascendente = s4
  if ascendente == 3:
    ascendente = s5
  if ascendente == 4:
    ascendente = s6
  if ascendente == 5:
    ascendente = s7
  if ascendente == 6:
    ascendente = s8
  if ascendente == 7:
    ascendente = s9
  if ascendente == 8:
    ascendente = s10
  if ascendente == 9:
    ascendente = s11
  if ascendente == 10:
     ascendente = s12
  if ascendente == 11:
    ascendente = s1
  if ascendente == 12:
    ascendente = s2
    ###ASCENDENTE /\

    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!")


                                                              #TOURO  /\
                                                              #GÊMEOS \/

if mes == 5 and dia >30:
  dia = int(input("Maio tem apenas 30 dias. Digite outra data: "))
  while dia >30:
    dia = int(input("Maio tem apenas 30 dias. Digite outra data: "))

          #MAIO   \/
  
if mes == 5 and dia >=21:
  signo = s3


    ###ASCENDENTE \/
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s12
  if hora_nascimento == 1:
    ascendente = s12
  if hora_nascimento == 2:
    ascendente = s1
  if hora_nascimento == 3:
    ascendente = s1
  if hora_nascimento == 4:
    ascendente = s2
  if hora_nascimento == 5:
    ascendente = s2
    
  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo
    
  if ascendente == 1:
    ascendente = s4  
  if ascendente == 2:
    ascendente = s5
  if ascendente == 3:
    ascendente = s6
  if ascendente == 4:
    ascendente = s7
  if ascendente == 5:
    ascendente = s8
  if ascendente == 6:
    ascendente = s9
  if ascendente == 7:
    ascendente = s10
  if ascendente == 8:
    ascendente = s11
  if ascendente == 9:
     ascendente = s12
  if ascendente == 10:
    ascendente = s1
  if ascendente == 11:
    ascendente = s2
  if ascendente == 12:
    ascendente = s3
    ###ASCENDENTE /\

    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!")

          #JUNHO  \/

if mes == 6 and dia <=20:
  signo = s3

     ###VENUS \/
  if ano == 1990 and mes == 6:
    venus2 = s2
    ###VENUS /\

  
    ###ASCENDENTE \/
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s12
  if hora_nascimento == 1:
    ascendente = s12
  if hora_nascimento == 2:
    ascendente = s1
  if hora_nascimento == 3:
    ascendente = s1
  if hora_nascimento == 4:
    ascendente = s2
  if hora_nascimento == 5:
    ascendente = s2
    
  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo
  
  if ascendente == 1:
    ascendente = s4    
  if ascendente == 2:
    ascendente = s5
  if ascendente == 3:
    ascendente = s6
  if ascendente == 4:
    ascendente = s7
  if ascendente == 5:
    ascendente = s8
  if ascendente == 6:
    ascendente = s9
  if ascendente == 7:
    ascendente = s10
  if ascendente == 8:
    ascendente = s11
  if ascendente == 9:
     ascendente = s12
  if ascendente == 10:
    ascendente = s1
  if ascendente == 11:
    ascendente = s2
  if ascendente == 12:
    ascendente = s3
    ###ASCENDENTE /\

    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!")

                                                              #GÊMEOS /\
                                                              #CÂNCER \/

          #JUNHO  \/
  
if mes == 6 and dia >=21:
  signo = s4

           ###VENUS \/
    ### Ás 00:14 do dia 25 de Junho Vênus entra em Gêmeos### 
  if ano == 1990 and dia < 25:
    venus2 = s2
  if ano == 1990 and dia == 25 and hora <= 00 and minutos < 14:
    venus2 = s2
  if ano == 1990 and dia == 25 and hora == 00 and minutos >= 14:
    venus2 = s3
  if ano == 1990 and dia == 25 and hora > 00:
     venus2 = s3
  if ano == 1990 and dia > 25:
     venus2 = s3
    ###VENUS /\


    ###ASCENDENTE \/
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s1
  if hora_nascimento == 1:
    ascendente = s1
  if hora_nascimento == 2:
    ascendente = s2
  if hora_nascimento == 3:
    ascendente = s2
  if hora_nascimento == 4:
    ascendente = s3
  if hora_nascimento == 5:
    ascendente = s3
    
  if hora_nascimento == 6:
    ascendente = signo
  if hora_nascimento == 7:
    ascendente = signo
    
  if ascendente == 1:
    ascendente = s5
  if ascendente == 2:
    ascendente = s6
  if ascendente == 3:
    ascendente = s7
  if ascendente == 4:
    ascendente = s8
  if ascendente == 5:
    ascendente = s9
  if ascendente == 6:
    ascendente = s10
  if ascendente == 7:
    ascendente = s11
  if ascendente == 8:
     ascendente = s12
  if ascendente == 9:
    ascendente = s1
  if ascendente == 10:
    ascendente = s2
  if ascendente == 11:
    ascendente = s3
  if ascendente == 12:
    ascendente = s4
    ###ASCENDENTE /\

    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!")

          #JULHO  \/

if mes == 7 and dia <=22:
  signo = s4

       ###VENUS \/
    ### Ás 03:41 do dia 20 de Julho Vênus entra em Câncer### 
  if ano == 1990 and dia < 20:
    venus2 = s3
  if ano == 1990 and dia == 20 and hora <= 3 and minutos < 41:
    venus2 = s3
  if ano == 1990 and dia == 20 and hora == 3 and minutos >= 41:
    venus2 = s4
  if ano == 1990 and dia == 20 and hora > 3:
     venus2 = s4
  if ano == 1990 and dia > 20:
     venus2 = s4
    ###VENUS /\



    ###ASCENDENTE \/
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s1
  if hora_nascimento == 1:
    ascendente = s1
  if hora_nascimento == 2:
    ascendente = s2
  if hora_nascimento == 3:
    ascendente = s2
  if hora_nascimento == 4:
    ascendente = s3
  if hora_nascimento == 5:
    ascendente = s3
    
  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo
    
  if ascendente == 1:
    ascendente = s5
  if ascendente == 2:
    ascendente = s6
  if ascendente == 3:
    ascendente = s7
  if ascendente == 4:
    ascendente = s8
  if ascendente == 5:
    ascendente = s9
  if ascendente == 6:
    ascendente = s10
  if ascendente == 7:
    ascendente = s11
  if ascendente == 8:
     ascendente = s12
  if ascendente == 9:
    ascendente = s1
  if ascendente == 10:
    ascendente = s2
  if ascendente == 11:
    ascendente = s3
  if ascendente == 12:
    ascendente = s4
    ###ASCENDENTE /\

    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!")

                                                              #CÂNCER   /\
                                                              #LEÃO     \/

if mes == 7 and dia >30:
  dia = int(input("Julho tem apenas 30 dias. Digite outra data: "))
  while dia >30:
    dia = int(input("Julho tem apenas 30 dias. Digite outra data: "))

          #JULHO \/
  
if mes == 7 and dia >=23:
  signo = s5

    ###VENUS \/
  if ano == 1990 and mes == 7:
    venus2 = s4
    ###VENUS /\
  

    ###ASCENDENTE \/
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s2
  if hora_nascimento == 1:
    ascendente = s2
  if hora_nascimento == 2:
    ascendente = s3
  if hora_nascimento == 3:
    ascendente = s3
  if hora_nascimento == 4:
    ascendente = s4
  if hora_nascimento == 5:
    ascendente = s4
    
  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo
    
  if ascendente == 1:
    ascendente = s6
  if ascendente == 2:
    ascendente = s7
  if ascendente == 3:
    ascendente = s8
  if ascendente == 4:
    ascendente = s9
  if ascendente == 5:
    ascendente = s10
  if ascendente == 6:
    ascendente = s11
  if ascendente == 7:
     ascendente = s12
  if ascendente == 8:
    ascendente = s1
  if ascendente == 9:
    ascendente = s2
  if ascendente == 10:
    ascendente = s3
  if ascendente == 11:
    ascendente = s4
  if ascendente == 12:
    ascendente = s5
    ###ASCENDENTE /\

    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!")

          #AGOSTO \/
  
if mes == 8 and dia <23:
  signo = s5

      ###VENUS \/
    ### Ás 22:05 do dia 13 de Agosto Vênus entra em Leão### 
  if ano == 1990 and dia < 13:
    venus2 = s4
  if ano == 1990 and dia == 13 and hora <= 22 and minutos < 5:
    venus2 = s4
  if ano == 1990 and dia == 13 and hora == 22 and minutos >= 5:
    venus2 = s5
  if ano == 1990 and dia == 13 and hora > 22:
     venus2 = s5
  if ano == 1990 and dia > 13:
     venus2 = s5
      ###VENUS /\
     

    ###ASCENDENTE \/
  ascendente = (hora_nascimento - 6) // 2
  
  if hora_nascimento == 0:
    ascendente = s2
  if hora_nascimento == 1:
    ascendente = s2
  if hora_nascimento == 2:
    ascendente = s3
  if hora_nascimento == 3:
    ascendente = s3
  if hora_nascimento == 4:
    ascendente = s4
  if hora_nascimento == 5:
    ascendente = s4
    
  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo
    
  if ascendente == 1:
    ascendente = s6
  if ascendente == 2:
    ascendente = s7
  if ascendente == 3:
    ascendente = s8
  if ascendente == 4:
    ascendente = s9
  if ascendente == 5:
    ascendente = s10
  if ascendente == 6:
    ascendente = s11
  if ascendente == 7:
     ascendente = s12
  if ascendente == 8:
    ascendente = s1
  if ascendente == 9:
    ascendente = s2
  if ascendente == 10:
    ascendente = s3
  if ascendente == 11:
    ascendente = s4
  if ascendente == 12:
    ascendente = s5
    ###ASCENDENTE /\

    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!")

                                                              #LEÃO     /\
                                                              #VIRGEM   \/

          #AGOSTO \/

if mes == 8 and dia >=23:
  signo = s6

      ###VENUS \/
  if ano == 1990 and mes == 8:
    venus2 = s5
      ###VENUS /\


    ###ASCENDENTE \/
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s3
  if hora_nascimento == 1:
    ascendente = s3
  if hora_nascimento == 2:
    ascendente = s4
  if hora_nascimento == 3:
    ascendente = s4
  if hora_nascimento == 4:
    ascendente = s5
  if hora_nascimento == 5:
    ascendente = s5
    
  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo

  if ascendente == 1:
    ascendente = s7
  if ascendente == 2:
    ascendente = s8
  if ascendente == 3:
    ascendente = s9
  if ascendente == 4:
    ascendente = s10
  if ascendente == 5:
    ascendente = s11
  if ascendente == 6:
     ascendente = s12
  if ascendente == 7:
    ascendente = s1
  if ascendente == 8:
    ascendente = s2
  if ascendente == 9:
    ascendente = s3
  if ascendente == 10:
    ascendente = s4
  if ascendente == 11:
    ascendente = s5
  if ascendente == 12:
    ascendente = s6
    ###ASCENDENTE /\

    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!")

          #SETEMBRO \/
### INCOMPLETO
  ##\/
  ##\/
  ##\/
if mes == 9 and dia <=22:
  signo = s6

  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s3
  if hora_nascimento == 1:
    ascendente = s3
  if hora_nascimento == 2:
    ascendente = s4
  if hora_nascimento == 3:
    ascendente = s4
  if hora_nascimento == 4:
    ascendente = s5
  if hora_nascimento == 5:
    ascendente = s5
    
  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo

  if ascendente == 1:
    ascendente = s7
  if ascendente == 2:
    ascendente = s8
  if ascendente == 3:
    ascendente = s9
  if ascendente == 4:
    ascendente = s10
  if ascendente == 5:
    ascendente = s11
  if ascendente == 6:
     ascendente = s12
  if ascendente == 7:
    ascendente = s1
  if ascendente == 8:
    ascendente = s2
  if ascendente == 9:
    ascendente = s3
  if ascendente == 10:
    ascendente = s4
  if ascendente == 11:
    ascendente = s5
  if ascendente == 12:
    ascendente = s6

  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!", marte1, marte2 + "!")

                                                              #VIRGEM   /\
                                                              #LIBRA    \/
  
if mes == 9 and dia >30:
  dia = int(input("Setembro tem apenas 30 dias. Digite outra data: "))
  while dia >30:
    dia = int(input("Setembro tem apenas 30 dias. Digite outra data: "))

          #SETEMBRO \/
 
if mes == 9 and dia >=23:
  signo = s7

  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s4
  if hora_nascimento == 1:
    ascendente = s4
  if hora_nascimento == 2:
    ascendente = s5
  if hora_nascimento == 3:
    ascendente = s5
  if hora_nascimento == 4:
    ascendente = s6
  if hora_nascimento == 5:
    ascendente = s6

  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo

  if ascendente == 1:
    ascendente = s8
  if ascendente == 2:
    ascendente = s9
  if ascendente == 3:
    ascendente = s10
  if ascendente == 4:
    ascendente = s11
  if ascendente == 5:
     ascendente = s12
  if ascendente == 6:
    ascendente = s1
  if ascendente == 7:
    ascendente = s2
  if ascendente == 8:
    ascendente = s3
  if ascendente == 9:
    ascendente = s4
  if ascendente == 10:
    ascendente = s5
  if ascendente == 11:
    ascendente = s6
  if ascendente == 12:
    ascendente = s7

  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!", marte1, marte2 + "!")

          #OUTUBRO \/

if mes == 10 and dia <=22:
  signo = s7
  
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s4
  if hora_nascimento == 1:
    ascendente = s4
  if hora_nascimento == 2:
    ascendente = s5
  if hora_nascimento == 3:
    ascendente = s5
  if hora_nascimento == 4:
    ascendente = s6
  if hora_nascimento == 5:
    ascendente = s6

  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo

  if ascendente == 1:
    ascendente = s8
  if ascendente == 2:
    ascendente = s9
  if ascendente == 3:
    ascendente = s10
  if ascendente == 4:
    ascendente = s11
  if ascendente == 5:
     ascendente = s12
  if ascendente == 6:
    ascendente = s1
  if ascendente == 7:
    ascendente = s2
  if ascendente == 8:
    ascendente = s3
  if ascendente == 9:
    ascendente = s4
  if ascendente == 10:
    ascendente = s5
  if ascendente == 11:
    ascendente = s6
  if ascendente == 12:
    ascendente = s7


  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!", marte1, marte2 + "!")

                                                              #LIBRA      /\
                                                              #ESCORPIÃO  \/
          #OUTUBRO \/

if mes == 10 and dia >=23:
  signo = s8
  
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s5
  if hora_nascimento == 1:
    ascendente = s5
  if hora_nascimento == 2:
    ascendente = s6
  if hora_nascimento == 3:
    ascendente = s6
  if hora_nascimento == 4:
    ascendente = s7
  if hora_nascimento == 5:
    ascendente = s7

  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo

  if ascendente == 1:
    ascendente = s9
  if ascendente == 2:
    ascendente = s10
  if ascendente == 3:
    ascendente = s11
  if ascendente == 4:
     ascendente = s12
  if ascendente == 5:
    ascendente = s1
  if ascendente == 6:
    ascendente = s2
  if ascendente == 7:
    ascendente = s3
  if ascendente == 8:
    ascendente = s4
  if ascendente == 9:
    ascendente = s5
  if ascendente == 10:
    ascendente = s6
  if ascendente == 11:
    ascendente = s7
  if ascendente == 12:
    ascendente = s8

  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!", marte1, marte2 + "!")

          #NOVEMBRO \/

if mes == 11 and dia <=21:
  signo = s8
  
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s5
  if hora_nascimento == 1:
    ascendente = s5
  if hora_nascimento == 2:
    ascendente = s6
  if hora_nascimento == 3:
    ascendente = s6
  if hora_nascimento == 4:
    ascendente = s7
  if hora_nascimento == 5:
    ascendente = s7

  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo

  if ascendente == 1:
    ascendente = s9
  if ascendente == 2:
    ascendente = s10
  if ascendente == 3:
    ascendente = s11
  if ascendente == 4:
     ascendente = s12
  if ascendente == 5:
    ascendente = s1
  if ascendente == 6:
    ascendente = s2
  if ascendente == 7:
    ascendente = s3
  if ascendente == 8:
    ascendente = s4
  if ascendente == 9:
    ascendente = s5
  if ascendente == 10:
    ascendente = s6
  if ascendente == 11:
    ascendente = s7
  if ascendente == 12:
    ascendente = s8

  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!", marte1, marte2 + "!")

                                                              #ESCORPIÃO  /\
                                                              #SAGITÁRIO  \/
if mes == 11 and dia >30:
  dia = int(input("Novembro tem apenas 30 dias. Digite outra data: "))
  while dia >30:
    dia = int(input("Novembro tem apenas 30 dias. Digite outra data: "))

          #NOVEMBRO \/ 
if mes == 11 and dia >=22:
  signo = s9

  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s6
  if hora_nascimento == 1:
    ascendente = s6
  if hora_nascimento == 2:
    ascendente = s7
  if hora_nascimento == 3:
    ascendente = s7
  if hora_nascimento == 4:
    ascendente = s8
  if hora_nascimento == 5:
    ascendente = s8

  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo

  if ascendente == 1:
    ascendente = s10
  if ascendente == 2:
    ascendente = s11
  if ascendente == 3:
     ascendente = s12
  if ascendente == 4:
    ascendente = s1
  if ascendente == 5:
    ascendente = s2
  if ascendente == 6:
    ascendente = s3  
  if ascendente == 7:
    ascendente = s4    
  if ascendente == 8:
    ascendente = s5 
  if ascendente == 9:
    ascendente = s6
  if ascendente == 10:
    ascendente = s7
  if ascendente == 11:
    ascendente = s8
  if ascendente == 12:
    ascendente = s9
    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!", marte1, marte2 + "!")
  
          #DEZEMBRO \/    
if mes == 12 and dia <=21:
  signo = s9

  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s6
  if hora_nascimento == 1:
    ascendente = s6
  if hora_nascimento == 2:
    ascendente = s7
  if hora_nascimento == 3:
    ascendente = s7
  if hora_nascimento == 4:
    ascendente = s8
  if hora_nascimento == 5:
    ascendente = s8

  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo

  if ascendente == 1:
    ascendente = s10
  if ascendente == 2:
    ascendente = s11
  if ascendente == 3:
     ascendente = s12
  if ascendente == 4:
    ascendente = s1
  if ascendente == 5:
    ascendente = s2
  if ascendente == 6:
    ascendente = s3  
  if ascendente == 7:
    ascendente = s4    
  if ascendente == 8:
    ascendente = s5 
  if ascendente == 9:
    ascendente = s6
  if ascendente == 10:
    ascendente = s7
  if ascendente == 11:
    ascendente = s8
  if ascendente == 12:
    ascendente = s9
    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!", marte1, marte2 + "!")
                                                              #SAGITÁRIO    /\
                                                              #CAPRICÓRNIO  \/
          #DEZEMBRO \/

if mes == 12 and dia >=22:
  signo = s10
  
  ascendente = (hora_nascimento - 6) // 2

  if hora_nascimento == 0:
    ascendente = s7
  if hora_nascimento == 1:
    ascendente = s7
  if hora_nascimento == 2:
    ascendente = s8
  if hora_nascimento == 3:
    ascendente = s8
  if hora_nascimento == 4:
    ascendente = s9
  if hora_nascimento == 5:
    ascendente = s9

  if hora_nascimento == 6:
    ascendente = signo          #Signo às 06 Horas
  if hora_nascimento == 7:
    ascendente = signo
    
  if ascendente == 1:
    ascendente = s11
  if ascendente == 2:
    ascendente = s12
  if ascendente == 3:
    ascendente = s1
  if ascendente == 4:
    ascendente = s2
  if ascendente == 5:
    ascendente = s3
  if ascendente == 6:
    ascendente = s4
  if ascendente == 7:
    ascendente = s5
  if ascendente == 8:
    ascendente = s6
  if ascendente == 9:
    ascendente = s7
  if ascendente == 10:
    ascendente = s8
  if ascendente == 11:
    ascendente = s9
  if ascendente == 12:
    ascendente = s10
    
  print(x, signo + "!", y, ascendente + "!", venus1, venus2 + "!", marte1, marte2 + "!")
                                                              #CAPRICÓRNIO  /\
