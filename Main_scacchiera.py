# Progetto iniziato il 16/05/23
# L'obbiettivo è quello di creare una scacchiera che selezionando un pezzo ti dica le mosse possibili e ti permetta di giocare un partita a scacchi

import scacchiera_e_pezzi as sp #modulo con funzioni per controllare mosse e creazione scacchiera
Fine_partita = False  # flag per la conclusione della partita
Turno = "b"

scacchiera = sp.inizializza_scacchiera()
sp.print_scacchiera(scacchiera)

while(not(Fine_partita)):
    if(sp.scacco_matto(scacchiera)):
        Fine_partita = True
    else:
        if(Turno == "b"):
            print("Turno bianco")
            re = sp.posizione_re("b",scacchiera)
            if (sp.sotto_scacco(re,scacchiera)):
                x = scacchiera[re.colonna][re.riga].mosse_possibili(scacchiera)
                i = 1
                for c_mossa in x:
                    sp.stampa_cordinate(x,i)
                    i = i+1
                y = input("dove vuoi muovere? (inserire il numero a sinistra della mossa)\n")
                while (not(sp.cordinata_mossa_presente(y,x))):
                     print("ERRORE: cordinata inserita errata")
                     y = input("dove vuoi muovere? (inserire il numero a sinistra della mossa)\n")
                sp.muovi_pezzo(x[y-1],scacchiera)
            else:
                y = 0
                while(y == 0):
                    x = input("che pezzo vuoi muovere?\n")
                    cordinate_vecchie = sp.da_input_a_cordinate(x)
                    while(not(sp.cordinata_posizione_presente(cordinate_vecchie,"b",scacchiera))):
                        print("ERRORE: cordinata inserita errata")
                        x = input("che pezzo vuoi muovere?\n")
                        cordinate_vecchie = sp.da_input_a_cordinate(x)
                    m = scacchiera[cordinate_vecchie.colonna][cordinate_vecchie.riga].pezzo.mosse_possibili(scacchiera)
                    i = 1
                    for c_mossa in  m:
                        sp.stampa_cordinate(c_mossa,i)
                        i = i+1
                    y = input("dove lo vuoi muovere? (inserire il numero a sinistra della mossa)\n")
                    while (not(sp.cordinata_mossa_presente(y,m))):
                        print("ERRORE: cordinata inserita errata")
                        y = input("dove vuoi muovere? (inserire il numero a sinistra della mossa)\n")
                    if(m[y-1].tipo_mossa == "Promozione"):
                        pezzo_in_cui_promuovere = sp.promozione()
                        sp.muovi_pezzo_promozione(m[y-1],scacchiera,pezzo_in_cui_promuovere)
                    else:
                        sp.muovi_pezzo(m[y-1],scacchiera)
        else:
            print("Turno nero")
            re = sp.posizione_re("n",scacchiera)
            if (sp.sotto_scacco(re,scacchiera)):
                x = re.mosse_possibili(scacchiera)
                i = 1
                for c_mossa in x:
                    sp.stampa_cordinate(x,i)
                    i = i+1
                y = input("dove vuoi muovere? (inserire il numero a sinistra della mossa)\n")
                while (not(sp.cordinata_mossa_presente(y,x))):
                     print("ERRORE: cordinata inserita errata")
                     y = input("dove vuoi muovere? (inserire il numero a sinistra della mossa)\n")
                sp.muovi_pezzo(x[y-1],scacchiera)
            else:
                y = 0
                while(y == 0):
                    x = input("che pezzo vuoi muovere?\n")
                    cordinate_vecchie = sp.da_input_a_cordinate(x)
                    while(not(sp.cordinata_posizione_presente(cordinate_vecchie,"n",scacchiera))):
                        print("ERRORE: cordinata inserita errata")
                        x = input("che pezzo vuoi muovere?\n")
                        cordinate_vecchie = sp.da_input_a_cordinate(x)
                    m = scacchiera[cordinate_vecchie.colonna][cordinate_vecchie.riga].pezzo.mosse_possibili(scacchiera)
                    i = 1
                    for c_mossa in  m:
                        sp.stampa_cordinate(c_mossa,i)
                        i = i+1
                    y = input("dove lo vuoi muovere? (inserire il numero a sinistra della mossa\n")
                    while (not(sp.cordinata_mossa_presente(y,m))):
                        print("ERRORE: cordinata inserita errata")
                        y = input("dove vuoi muovere? (inserire il numero a sinistra della mossa)\n")
                    if(m[y-1].tipo_mossa == "Promozione"):
                        pezzo_in_cui_promuovere = sp.promozione()
                        sp.muovi_pezzo_promozione(m[y-1],scacchiera,pezzo_in_cui_promuovere)
                    else:
                        sp.muovi_pezzo(m[y-1],scacchiera)
        sp.print_scacchiera(scacchiera)