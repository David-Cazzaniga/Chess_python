#Definizione classi e funzioni dei singoli pezzi

log_scacchiera = []

class Pezzo:
    def __init__(self, colonna, riga, squadra):
        self.colonna=colonna
        self.riga=riga
        self.squadra=squadra

class Torre(Pezzo):
    def __init__(self, colonna, riga, squadra, prima_mossa_fatta):
        super().__init__(colonna, riga, squadra)
        self.prima_mossa_fatta = prima_mossa_fatta
    def stampa_lettera(self):
        return "T"
    def mosse_possibili(self,scacchiera):
        if (pinned(self,scacchiera)):
            return None
        else:
            mosse = []
            x = controlla_sinistra(self,scacchiera)
            if(x):
                mosse.extend(x)
            x = controlla_destra(self,scacchiera)
            if(x):
                mosse.extend(x)
            x = controlla_alto(self,scacchiera)
            if(x):
                mosse.extend(x)
            x = controlla_basso(self,scacchiera)
            if(x):
                mosse.extend(x)
            x = controlla_arrocco(self,scacchiera)
            return mosse

class Cavallo(Pezzo):
    def stampa_lettera(self):
        return "C"
    def mosse_possibili(self,scacchiera):
        if (pinned(self,scacchiera)):
            return None
        else:
            mosse = []
            x = controlla_cavallo(self,scacchiera)
            if(x):    
                mosse.extend(x)
            return mosse

class Alfiere(Pezzo):
    def stampa_lettera(self):
        return "A"
    def mosse_possibili(self,scacchiera):
        if (pinned(self,scacchiera)):
            return None
        else:
            mosse = []
            x = controlla_altosinistra(self,scacchiera)
            if(x):    
                mosse.extend(x)
            x = controlla_bassosinistra(self,scacchiera)
            if(x):    
                mosse.extend(x)
            x = controlla_bassodestra(self,scacchiera)
            if(x):    
                mosse.extend(x)
            x = controlla_altodestra(self,scacchiera)
            if(x):    
                mosse.extend(x)
            return mosse

class Regina(Pezzo):
    def stampa_lettera(self):
        return "D"
    def mosse_possibili(self,scacchiera):
        if (pinned(self,scacchiera)):
            return None
        else:
            mosse = []
            x = controlla_sinistra(self,scacchiera)
            if(x):
                mosse.extend(x)
            x = controlla_destra(self,scacchiera)
            if(x):
                mosse.extend(x)
            x = controlla_alto(self,scacchiera)
            if(x):
                mosse.extend(x)
            x = controlla_basso(self,scacchiera)
            if(x):
                mosse.extend(x)
            x = controlla_altosinistra(self,scacchiera)
            if(x):
                mosse.extend(x)
            x = controlla_bassosinistra(self,scacchiera)
            if(x):
                mosse.extend(x)
            x = controlla_bassodestra(self,scacchiera)
            if(x):
                mosse.extend(x)
            x = controlla_altodestra(self,scacchiera)
            if(x):
                mosse.extend(x)
            return mosse

class Re(Pezzo):
    def __init__(self, colonna, riga, squadra, scacco, prima_mossa_fatta):
        super().__init__(colonna, riga, squadra)
        self.scacco = scacco
        self.prima_mossa_fatta = prima_mossa_fatta
    def stampa_lettera(self):
        return "R"
    def mosse_possibili(self,scacchiera):
        mosse = []
        cordinate_pezzi_che_stanno_dando_scacco = sotto_scacco(self,scacchiera)
        if(cordinate_pezzi_che_stanno_dando_scacco):
            x = controlla_difesa_scacco(self,cordinate_pezzi_che_stanno_dando_scacco, scacchiera)
            if(x):    
                mosse.extend(x)
        else:
            x = controlla_re(self,scacchiera)
            if(x):    
                mosse.extend(x)
        return mosse

class Pedone(Pezzo):
    def __init__(self, colonna, riga, squadra, prima_mossa_fatta, avanzamento_due_caselle_turno_precedente):
        super().__init__(colonna, riga, squadra)
        self.prima_mossa_fatta = prima_mossa_fatta
        self.avanzamento_due_caselle_turno_precedente = avanzamento_due_caselle_turno_precedente
    def stampa_lettera(self):
        return "P"
    def mosse_possibili(self,scacchiera):
        if (pinned(self,scacchiera)):
            return None
        else:
            mosse = []
            x = controlla_pedone(self,scacchiera)
            if(x):    
                mosse.extend(x)
            x = controlla_enpassant(self,scacchiera,log_scacchiera)
            if(x):    
                mosse.extend(x)
            return mosse

def sotto_scacco(re,scacchiera):
    if(type(re) == Re):
        mosse = []
        cordinate_pezzi_che_stanno_dando_scacco = []
        x = controlla_alto(re,scacchiera)
        if(x):        
            mosse.extend(x)
        x = controlla_destra(re,scacchiera)
        if(x):      
            mosse.extend(x)
        x = controlla_basso(re,scacchiera)
        if(x):       
            mosse.extend(x)
        x = controlla_sinistra(re,scacchiera)
        if(x):    
            mosse.extend(x)
        x = controlla_altosinistra(re,scacchiera)
        if(x):
            mosse.extend(x)
        x = controlla_altodestra(re,scacchiera)
        if(x):  
            mosse.extend(x)
        x = controlla_bassodestra(re,scacchiera)
        if(x): 
            mosse.extend(x)
        x = controlla_bassosinistra(re,scacchiera)
        if(x):        
            mosse.extend(x)
        x = controlla_cavallo(re,scacchiera)
        if(x):     
            mosse.extend(x)
        cordinate_pezzi_avversari = []
        for mossa in mosse:
            if(scacchiera[mossa.colonna][mossa.riga].pezzo != None):
                cordinate_pezzi_avversari.append(mossa)
        for pezzo in cordinate_pezzi_avversari:
            mosse_pezzo = scacchiera[pezzo.colonna][pezzo.riga].pezzo.mosse_possibili(scacchiera)
            for mossa in mosse_pezzo:
                if(scacchiera[mossa.colonna][mossa.riga].pezzo != None):
                    if(type(scacchiera[mossa.colonna][mossa.riga].pezzo) == Re):
                        cordinate_pezzi_che_stanno_dando_scacco.append(mossa)
        return cordinate_pezzi_che_stanno_dando_scacco
    else:
        print("ERRORE CONTROLLO SOTTO SCACCO: Non è un Re")

def posizione_re(s,scacchiera):
    for i in range(8):
        for j in range(8):
            if(type(scacchiera[i][j].pezzo) == Re and scacchiera[i][j].pezzo.squadra == s):
                return scacchiera[i][j].pezzo

def posizione_re_avversario(s,scacchiera):
    if (s == "b"):
        s = "n"
    else:
        s = "b"
    for i in range(8):
        for j in range(8):
            if(type(scacchiera[i][j].pezzo) == Re and scacchiera[i][j].pezzo.squadra == s):
                return scacchiera[i][j].pezzo

def pinned(pezzo,scacchiera):
    i = pezzo.colonna
    j = pezzo.riga
    s = pezzo.squadra
    x = posizione_re(s,scacchiera)
    pezzi_scacco_base = sotto_scacco(x,scacchiera)
    scacchiera_modificata = scacchiera.copy()
    scacchiera_modificata[i][j].pezzo = None
    scacchiera_modificata[i][j].occupata = False
    pezzi_scacco_modificata = sotto_scacco(x,scacchiera_modificata)
    if(pezzi_scacco_base and pezzi_scacco_modificata):
        if (set(pezzi_scacco_base) == set(pezzi_scacco_modificata)):
            return False
        else:
            return True
    
def controlla_sinistra(pezzo,scacchiera):
    i = pezzo.colonna
    j = pezzo.riga
    s = pezzo.squadra
    mosse = []
    if(i-1 > -1):
        if(scacchiera[i-1][j].occupata == False):
            x = Cordinata(i-1,j,None,i,j)
            if(x):
                mosse.append(x)
            i = i-1
        elif(scacchiera[i-1][j].occupata == True and scacchiera[i-1][j].pezzo.squadra != s):
            x = Cordinata(i-1,j,"mangiata",i,j)
            if(x):
                mosse.append(x)
            i = i-1
        else:
            return mosse
    else:
        return mosse

def controlla_destra(pezzo,scacchiera):
    i = pezzo.colonna
    j = pezzo.riga
    s = pezzo.squadra
    mosse = []
    if(i+1 < 8):
        if(scacchiera[i+1][j].occupata == False):
            x = Cordinata(i+1,j,None,i,j)
            if(x):
                mosse.append(x)
            i = i+1
        elif(scacchiera[i+1][j].occupata == True and scacchiera[i+1][j].pezzo.squadra != s):
            x = Cordinata(i+1,j,"mangiata",i,j)
            if(x):
                mosse.append(x)
            i = i+1
        else:
            return mosse
    else:
        return mosse

def controlla_alto(pezzo,scacchiera):
    i = pezzo.colonna
    j = pezzo.riga
    s = pezzo.squadra
    mosse = []
    if(j+1 < 8):
        if(scacchiera[i][j+1].occupata == False):
            x = Cordinata(i,j+1,None,i,j)
            if(x):
                mosse.append(x)
            j = j+1
        elif(scacchiera[i][j+1].occupata == True and scacchiera[i][j+1].pezzo.squadra != s):
            x = Cordinata(i,j+1,"mangiata",i,j)
            if(x):
                mosse.append(x)
            j = j+1
        else:
            return mosse
    else:
        return mosse

def controlla_basso(pezzo,scacchiera):
    i = pezzo.colonna
    j = pezzo.riga
    s = pezzo.squadra
    mosse = []
    if(j-1 > -1):
        if(scacchiera[i][j-1].occupata == False):
            x = Cordinata(i,j-1,None,i,j)
            if(x):
                mosse.append(x)
            j = j-1
        elif(scacchiera[i][j-1].occupata == True and scacchiera[i][j-1].pezzo.squadra != s):
            x = Cordinata(i,j-1,"mangiata",i,j)
            if(x):
                mosse.append(x)
            j = j-1
        else:
            return mosse
    else:
        return mosse

def controlla_altodestra(pezzo,scacchiera):
    i = pezzo.colonna
    j = pezzo.riga
    s = pezzo.squadra
    mosse = []
    if(j+1 < 8 and i+1 < 8):
        if(scacchiera[i+1][j+1].occupata == False):
            x = Cordinata(i+1,j+1,None,i,j)
            if(x):
                mosse.append(x)
            i = i+1
            j = j+1
        elif(scacchiera[i+1][j+1].occupata == True and scacchiera[i+1][j+1].pezzo.squadra != s):
            x = Cordinata(i+1,j+1,"mangiata",i,j)
            if(x):
                mosse.append(x)
            i = i+1
            j = j+1
        else:
            return mosse
    else:
        return mosse

def controlla_bassodestra(pezzo,scacchiera):
    i = pezzo.colonna
    j = pezzo.riga
    s = pezzo.squadra
    mosse = []
    if(j-1 > -1 and i+1 < 8):
        if(scacchiera[i+1][j-1].occupata == False):
            x = Cordinata(i+1,j-1,None,i,j)
            if(x):
                mosse.append(x)
            i = i+1
            j = j-1
        elif(scacchiera[i+1][j-1].occupata == True and scacchiera[i+1][j-1].pezzo.squadra != s):
            x = Cordinata(i+1,j-1,"mangiata",i,j)
            if(x):
                mosse.append(x)
            i = i+1
            j = j-1
        else:
            return mosse
    else:
        return mosse

def controlla_bassosinistra(pezzo,scacchiera):
    i = pezzo.colonna
    j = pezzo.riga
    s = pezzo.squadra
    mosse = []
    if(j-1 > -1 and i-1 > -1):
        if(scacchiera[i-1][j-1].occupata == False):
            x = Cordinata(i-1,j-1,None,i,j)
            if(x):
                mosse.append(x)
            i = i-1
            j = j-1
        elif(scacchiera[i-1][j-1].occupata == True and scacchiera[i-1][j-1].pezzo.squadra != s):
            x = Cordinata(i-1,j-1,"mangiata",i,j)
            if(x):
                mosse.append(x)
            i = i-1
            j = j-1
        else:
            return mosse
    else:
        return mosse

def controlla_altosinistra(pezzo,scacchiera):
    i = pezzo.colonna
    j = pezzo.riga
    s = pezzo.squadra
    mosse = []
    if(j+1 < 8 and i-1 > -1):
        if(scacchiera[i-1][j+1].occupata == False):
            x = Cordinata(i-1,j+1,None,i,j)
            if(x):
                mosse.append(x)
            i = i-1
            j = j+1
        elif(scacchiera[i-1][j+1].occupata == True and scacchiera[i-1][j+1].pezzo.squadra != s):
            x = Cordinata(i-1,j+1,"mangiata",i,j)
            if(x):
                mosse.append(x)
            i = i-1
            j = j+1
        else:
            return mosse
    else:
        return mosse

def controlla_cavallo(pezzo,scacchiera):
    i = pezzo.colonna
    j = pezzo.riga
    s = pezzo.squadra
    mosse = []
    if(i-1 > -1 and j-2 >-1):
        if(type(scacchiera[i-1][j-2].pezzo) == None):
            x = Cordinata(i-1,j-2,None,i,j)
            if(x):
                mosse.append(x)
        elif(scacchiera[i-1][j-2].pezzo != None):
            if(scacchiera[i-1][j-2].pezzo.squadra != s):
                x = Cordinata(i-1,j-2,"mangiata",i,j)
                if(x):
                    mosse.append(x)

    if(i-2 > -1 and j-1 >-1):
        if(type(scacchiera[i-2][j-1].pezzo) == None):
            x = Cordinata(i-2,j-1,None,i,j)
            if(x):
                mosse.append(x)
        elif(scacchiera[i-2][j-1].pezzo != None):
            if(scacchiera[i-2][j-1].pezzo.squadra != s):
                x = Cordinata(i-2,j-1,"mangiata",i,j)
                if(x):
                    mosse.append(x)
    
    if(i-2 > -1 and j+1 < 8):
        if(type(scacchiera[i-2][j+1].pezzo) == None):
            x = Cordinata(i-2,j+1,None,i,j)
            if(x):
                mosse.append(x)
        elif(scacchiera[i-2][j+1].pezzo != None):
            if(scacchiera[i-2][j+1].pezzo.squadra != s):
                x = Cordinata(i-2,j+1,"mangiata",i,j)
                if(x):
                    mosse.append(x)
    
    if(i-1 > -1 and j+2 < 8):
        if(type(scacchiera[i-1][j+2].pezzo) == None):
            x = Cordinata(i-1,j+2,None,i,j)
            if(x):
                mosse.append(x)
        elif(scacchiera[i-1][j+2].pezzo != None):
            if(scacchiera[i-1][j+2].pezzo.squadra != s):
                x = Cordinata(i-1,j+2,"mangiata",i,j)
                if(x):
                    mosse.append(x)
    
    if(i+1 < 8 and j+2 < 8):
        if(type(scacchiera[i+1][j+2].pezzo) == None):
            x = Cordinata(i+1,j+2,None,i,j)
            if(x):
                mosse.append(x)
        elif(scacchiera[i+1][j+2].pezzo != None):
            if(scacchiera[i+1][j+2].pezzo.squadra != s):
                x = Cordinata(i+1,j+2,"mangiata",i,j)
                if(x):
                    mosse.append(x)

    if(i+2 < 8 and j+1 < 8):
        if(type(scacchiera[i+2][j+1].pezzo) == None):
            x = Cordinata(i+2,j+1,None,i,j)
            if(x):
                mosse.append(x)
        elif(scacchiera[i+2][j+1].pezzo != None):
            if(scacchiera[i+2][j+1].pezzo.squadra != s):
                x = Cordinata(i+2,j+1,"mangiata",i,j)
                if(x):
                    mosse.append(x)

    if(i+2 < 8 and j-1 > -1):
        if(type(scacchiera[i+2][j-1].pezzo) == None):
            x = Cordinata(i+2,j-1,None,i,j)
            if(x):
                mosse.append(x)
        elif(scacchiera[i+2][j-1].pezzo != None):
            if(scacchiera[i+2][j-1].pezzo.squadra != s):
                x = Cordinata(i+2,j-1,"mangiata",i,j)
                if(x):
                    mosse.append(x)

    if(i+1 < 8 and j-2 > -1):
        if(type(scacchiera[i+1][j-2].pezzo) == None):
            x = Cordinata(i+1,j-2,None,i,j)
            if(x):
                mosse.append(x)
        elif(scacchiera[i+1][j-2].pezzo != None):
            if(scacchiera[i+1][j-2].pezzo.squadra != s):
                x = Cordinata(i+1,j-2,"mangiata",i,j)
                if(x):
                    mosse.append(x)

    return mosse

def controlla_arrocco(pezzo,scacchiera):
    if (type(pezzo) == Torre or type(pezzo) == Re):
        i = pezzo.colonna
        j = pezzo.riga
        s = pezzo.squadra
        p = pezzo.prima_mossa_fatta
        mosse = []
        if(p == False):
            if(s == "b"):
                if(type(scacchiera[4][0]) == Re):
                    if(scacchiera[4][0].pezzo.squadra == s):
                        if(scacchiera[4][0].pezzo.prima_mossa_fatta == False):
                            if((i == 0 and j == 0) or (i == 4 and j == 0)):
                                if(not(sotto_scacco(scacchiera[4][0].pezzo,scacchiera))):
                                    if(scacchiera[3][0].pezzo == None and scacchiera[2][0].pezzo == None and scacchiera[1][0] == None):
                                        arrocco_flag = True
                                        for k in range(2):
                                            casella_finta = Pezzo(k+2,0,s)
                                            cordinate_che_sto_controllando = Cordinata(k+2,0,None,None,None)
                                            mosse_pezzo_finto = []
                                            x = controlla_altosinistra(casella_finta,scacchiera)
                                            if(x):
                                                mosse_pezzo_finto.extend(x)
                                            x = controlla_alto(casella_finta,scacchiera)
                                            if(x):
                                                mosse_pezzo_finto.extend(x)
                                            x = controlla_altodestra(casella_finta,scacchiera)
                                            if(x):
                                                mosse_pezzo_finto.extend(x)
                                            x = controlla_cavallo(casella_finta,scacchiera)
                                            if(x):
                                                mosse_pezzo_finto.extend(x)
                                            for mossa in mosse_pezzo_finto:
                                                if(mossa.tipo_mossa == "mangiata"):
                                                    mosse_pezzo_avversario = scacchiera[mossa.colonna][mossa.riga].pezzo.mosse_possibili()
                                                    if cordinate_che_sto_controllando in mosse_pezzo_avversario:
                                                        arrocco_flag = False
                                        if (arrocco_flag == True):
                                            if (type(pezzo) == Re):
                                                arrocco = Cordinata(2,0,"Arrocco_queenside",i,j)  # Arrocco Queenside
                                                mosse.append(arrocco)
                                            elif(type(pezzo) == Torre):
                                                arrocco = Cordinata(3,0,"Arrocco_queenside",i,j)
                                                mosse.append(arrocco)
                            if((i == 7 and j == 0) or (i == 4 and j == 0)):
                                if(not(sotto_scacco(scacchiera[4][0].pezzo,scacchiera))):
                                    if(scacchiera[5][0].pezzo == None and scacchiera[6][0].pezzo == None):
                                        arrocco_flag = True
                                        for k in range(2):
                                            casella_finta = Pezzo(k+5,0,s)
                                            cordinate_che_sto_controllando = Cordinata(k+5,0,None,None,None)
                                            mosse_pezzo_finto = []
                                            x = controlla_altosinistra(casella_finta,scacchiera)
                                            if(x):
                                                mosse_pezzo_finto.extend(x)
                                            x = controlla_alto(casella_finta,scacchiera)
                                            if(x):
                                                mosse_pezzo_finto.extend(x)
                                            x = controlla_altodestra(casella_finta,scacchiera)
                                            if(x):
                                                mosse_pezzo_finto.extend(x)
                                            x = controlla_cavallo(casella_finta,scacchiera)
                                            if(x):
                                                mosse_pezzo_finto.extend(x)
                                            for mossa in mosse_pezzo_finto:
                                                if(mossa.tipo_mossa == "mangiata"):
                                                    mosse_pezzo_avversario = scacchiera[mossa.colonna][mossa.riga].pezzo.mosse_possibili()
                                                    if cordinate_che_sto_controllando in mosse_pezzo_avversario:
                                                        arrocco_flag = False
                                        if (arrocco_flag == True):
                                            if (type(pezzo) == Re):
                                                arrocco = Cordinata(6,0,"Arrocco_kingside",i,j)  # Arrocco Kingside
                                                mosse.append(arrocco)
                                            elif(type(pezzo) == Torre):
                                                arrocco = Cordinata(5,0,"Arrocco_kingside",i,j)
                                                mosse.append(arrocco)
            else:
                if(type(scacchiera[4][7]) == Re):
                    if(scacchiera[4][7].pezzo.squadra == s):
                        if(scacchiera[4][7].pezzo.prima_mossa_fatta == False):
                            if((i == 0 and j == 7) or (i == 4 and j == 7)):
                                if(not(sotto_scacco(scacchiera[4][7].pezzo,scacchiera))):
                                    if(scacchiera[3][7].pezzo == None and scacchiera[2][7].pezzo == None and scacchiera[1][7] == None):
                                        arrocco_flag = True
                                        for k in range(2):
                                            casella_finta = Pezzo(k+2,7,s)
                                            cordinate_che_sto_controllando = Cordinata(k+2,7,None,None,None)
                                            mosse_pezzo_finto = []
                                            x = controlla_altosinistra(casella_finta,scacchiera)
                                            if(x):
                                                mosse_pezzo_finto.extend(x)
                                            x = controlla_alto(casella_finta,scacchiera)
                                            if(x):
                                                mosse_pezzo_finto.extend(x)
                                            x = controlla_altodestra(casella_finta,scacchiera)
                                            if(x):
                                                mosse_pezzo_finto.extend(x)
                                            x = controlla_cavallo(casella_finta,scacchiera)
                                            if(x):
                                                mosse_pezzo_finto.extend(x)
                                            for mossa in mosse_pezzo_finto:
                                                if(mossa.tipo_mossa == "mangiata"):
                                                    mosse_pezzo_avversario = scacchiera[mossa.colonna][mossa.riga].pezzo.mosse_possibili()
                                                    if cordinate_che_sto_controllando in mosse_pezzo_avversario:
                                                        arrocco_flag = False
                                        if (arrocco_flag == True):
                                            if (type(pezzo) == Re):
                                                arrocco = Cordinata(2,7,"Arrocco_queenside",i,j)  # Arrocco Queenside
                                                mosse.append(arrocco)                                            
                                            elif(type(pezzo) == Torre):
                                                arrocco = Cordinata(3,7,"Arrocco_queenside",i,j)
                                                mosse.append(arrocco)
                            if((i == 7 and j == 7) or (i == 4 and j == 7)):
                                if(not(sotto_scacco(scacchiera[4][7].pezzo,scacchiera))):
                                    if(scacchiera[5][7].pezzo == None and scacchiera[6][7].pezzo == None):
                                        arrocco_flag = True
                                        for k in range(2):
                                            casella_finta = Pezzo(k+5,7,s)
                                            cordinate_che_sto_controllando = Cordinata(k+5,7,None,None,None)
                                            mosse_pezzo_finto = []
                                            x = controlla_altosinistra(casella_finta,scacchiera)
                                            if(x):
                                                mosse_pezzo_finto.extend(x)
                                            x = controlla_alto(casella_finta,scacchiera)
                                            if(x):
                                                mosse_pezzo_finto.extend(x)
                                            x = controlla_altodestra(casella_finta,scacchiera)
                                            if(x):
                                                mosse_pezzo_finto.extend(x)
                                            x = controlla_cavallo(casella_finta,scacchiera)
                                            if(x):
                                                mosse_pezzo_finto.extend(x)
                                            for mossa in mosse_pezzo_finto:
                                                if(mossa.tipo_mossa == "mangiata"):
                                                    mosse_pezzo_avversario = scacchiera[mossa.colonna][mossa.riga].pezzo.mosse_possibili()
                                                    if cordinate_che_sto_controllando in mosse_pezzo_avversario:
                                                        arrocco_flag = False
                                        if (arrocco_flag == True):
                                            if (type(pezzo) == Re):
                                                arrocco = Cordinata(6,7,"Arrocco_kingside",i,j)  # Arrocco Kingside
                                                mosse.append(arrocco)
                                            elif(type(pezzo) == Torre):
                                                arrocco = Cordinata(5,7,"Arrocco_kingside",i,j)
                                                mosse.append(arrocco)
        return mosse             
    else:
        print("ERRORE: passato al controllo arrocco un pezzo che non è né torre né re")

def controlla_pedone(pezzo,scacchiera):
    i = pezzo.colonna
    j = pezzo.riga
    s = pezzo.squadra
    p = pezzo.prima_mossa_fatta
    mosse = []
    if(pezzo.squadra == "b"):
        if(scacchiera[i][j+1].pezzo == None):
            if(j == 6):
                x = Cordinata(i,7,"Promozione",i,j)
            else:
                x = Cordinata(i,j+1,None,i,j)
            mosse.append(x)
        if(i-1 > -1):
            if(scacchiera[i-1][j+1].pezzo != None):
                if(scacchiera[i-1][j+1].pezzo.squadra != s):
                    if(j == 6):
                        x = Cordinata(i-1,7,"mangiata_Promozione",i,j)
                    else:
                        x = Cordinata(i-1,j+1,"mangiata",i,j)
                    mosse.append(x)
        if(i+1 < 8):
            if(scacchiera[i+1][j+1].pezzo != None):
                if(scacchiera[i+1][j+1].pezzo.squadra != s):
                    if(j == 6):
                        x = Cordinata(i+1,7,"mangiata_Promozione",i,j)
                    else:
                        x = Cordinata(i+1,j+1,"mangiata",i,j)
                    mosse.append(x)
    else:
        if(scacchiera[i][j-1].pezzo == None):
            if(j == 1):
                x = Cordinata(i,0,"Promozione",i,j)
            else:
                x = Cordinata(i,j-1,None,i,j)
            mosse.append(x)
        if(i-1 > -1):
            if(scacchiera[i-1][j-1].pezzo != None):
                if(scacchiera[i-1][j-1].pezzo.squadra != s):
                    if(j == 1):
                        x = Cordinata(i-1,0,"mangiata_Promozione",i,j)
                    else:
                        x = Cordinata(i-1,j-1,"mangiata",i,j)
                    mosse.append(x)
        if(i+1 < 8):
            if(scacchiera[i+1][j-1].pezzo != None):
                if(scacchiera[i+1][j-1].pezzo.squadra != s):
                    if(j == 1):
                        x = Cordinata(i+1,-1,"mangiata_Promozione",i,j)
                    else:
                        x = Cordinata(i+1,j-1,"mangiata",i,j)
                    mosse.append(x)
    if(p == False):
        if(scacchiera[i][j+1].pezzo == None and scacchiera[i][j+2].pezzo == None):
            x=Cordinata(i,j+2,"pedone_doppio",i,j)
            mosse.append(x)
    return mosse

def controlla_enpassant(pezzo,scacchiera,log_scacchiera):
    i = pezzo.colonna
    j = pezzo.riga
    s = pezzo.squadra
    mosse = []
    if(len(log_scacchiera) > 0):
        if(s == "b" and j == 4):
            if(i+1 < 8):
                if(type(scacchiera[i+1][j].pezzo) == Pedone):
                    if(log_scacchiera[-1].colonna == i+1 and log_scacchiera[-1].riga == j and log_scacchiera[-1].tipo_mossa == "pedone_doppio"):
                        x = Cordinata(i+1,j+1,"en_passant",i,j)
                        mosse.append(x)
            if(i-1 > -1):
                if(type(scacchiera[i-1][j].pezzo) == Pedone):
                    if(log_scacchiera[-1].colonna == i-1 and log_scacchiera[-1].riga == j and log_scacchiera[-1].tipo_mossa == "pedone_doppio"):
                        x = Cordinata(i-1,j+1,"en_passant",i,j)
                        mosse.append(x)
        if(s == "n" and j == 3):
            if(i+1 < 8):
                if(type(scacchiera[i+1][j].pezzo) == Pedone):
                    if(log_scacchiera[-1].colonna == i+1 and log_scacchiera[-1].riga == j and log_scacchiera[-1].tipo_mossa == "pedone_doppio"):
                        x = Cordinata(i+1,j-1,"en_passant",i,j)
                        mosse.append(x)
            if(i-1 > -1):
                if(type(scacchiera[i-1][j].pezzo) == Pedone):
                    if(log_scacchiera[-1].colonna == i-1 and log_scacchiera[-1].riga == j and log_scacchiera[-1].tipo_mossa == "pedone_doppio"):
                        x = Cordinata(i-1,j-1,"en_passant",i,j)
                        mosse.append(x)
    return mosse

def controlla_re(pezzo,scacchiera):
    i = pezzo.colonna
    j = pezzo.riga
    s = pezzo.squadra
    mosse = []
    if(i-1 > -1):
        for k in range(3):
            if(j-1+k > -1 and j-1+k < 8):
                casella_finta = Pezzo(i-1,j-1+k,s)
                cordinate_che_sto_controllando = Cordinata(i-1,j-1+k,None,None,None)
                mosse_pezzo_finto = []
                x = controlla_altosinistra(casella_finta,scacchiera)
                if (x):
                    mosse_pezzo_finto.extend(x)
                x = controlla_alto(casella_finta,scacchiera)
                if (x):
                    mosse_pezzo_finto.extend(x)
                x = controlla_altodestra(casella_finta,scacchiera)
                if (x):
                    mosse_pezzo_finto.extend(x)
                x = controlla_destra(casella_finta,scacchiera)
                if (x):
                    mosse_pezzo_finto.extend(x)
                x = controlla_bassodestra(casella_finta,scacchiera)
                if (x):
                    mosse_pezzo_finto.extend(x)
                x = controlla_basso(casella_finta,scacchiera)
                if (x):
                    mosse_pezzo_finto.extend(x)
                x = controlla_bassosinistra(casella_finta,scacchiera)
                if (x):
                    mosse_pezzo_finto.extend(x)
                x = controlla_sinistra(casella_finta,scacchiera)
                if (x):
                    mosse_pezzo_finto.extend(x)
                for mossa in mosse_pezzo_finto:
                    if(mossa.tipo_mossa == "mangiata"):
                        mosse_pezzo_avversario = scacchiera[mossa.colonna][mossa.riga].pezzo.mosse_possibili()
                        if not(cordinate_che_sto_controllando in mosse_pezzo_avversario):
                            if (scacchiera[cordinate_che_sto_controllando.colonna][cordinate_che_sto_controllando.riga].pezzo == None):
                                x = Cordinata(i-1,j-1+k,None,i,j)
                            elif (scacchiera[cordinate_che_sto_controllando.colonna][cordinate_che_sto_controllando.riga].pezzo.squadra != s):
                                x = Cordinata(i-1,j-1+k,"mangiata",i,j)
                            mosse.append(x)
    if(i+1 < 8):
        for k in range(3):
            if(j-1+k > -1 and j-1+k < 8):
                casella_finta = Pezzo(i+1,j-1+k,s)
                cordinate_che_sto_controllando = Cordinata(i+1,j-1+k,None,None,None)
                mosse_pezzo_finto = []
                x = controlla_altosinistra(casella_finta,scacchiera)
                if(x):
                    mosse_pezzo_finto.extend(x)
                x = controlla_alto(casella_finta,scacchiera)
                if(x):
                    mosse_pezzo_finto.extend(x)
                x = controlla_altodestra(casella_finta,scacchiera)
                if(x):
                    mosse_pezzo_finto.extend(x)
                x = controlla_destra(casella_finta,scacchiera)
                if(x):
                    mosse_pezzo_finto.extend(x)
                x = controlla_bassodestra(casella_finta,scacchiera)
                if(x):
                    mosse_pezzo_finto.extend(x)
                x = controlla_basso(casella_finta,scacchiera)
                if(x):
                    mosse_pezzo_finto.extend(x)
                x = controlla_bassosinistra(casella_finta,scacchiera)
                if(x):
                    mosse_pezzo_finto.extend(x)
                x = controlla_sinistra(casella_finta,scacchiera)
                if(x):
                    mosse_pezzo_finto.extend(x)
                for mossa in mosse_pezzo_finto:
                    if(mossa.tipo_mossa == "mangiata"):
                        mosse_pezzo_avversario = scacchiera[mossa.colonna][mossa.riga].pezzo.mosse_possibili()
                        if not(cordinate_che_sto_controllando in mosse_pezzo_avversario):
                            if (scacchiera[cordinate_che_sto_controllando.colonna][cordinate_che_sto_controllando.riga].pezzo == None):
                                x = Cordinata(i+1,j-1+k,None,i,j)
                            elif (scacchiera[cordinate_che_sto_controllando.colonna][cordinate_che_sto_controllando.riga].pezzo.squadra != s):
                                x = Cordinata(i+1,j-1+k,"mangiata",i,j)
                            mosse.append(x)
    if(j-1 > -1):
        casella_finta = Pezzo(i,j-1,s)
        cordinate_che_sto_controllando = Cordinata(i,j-1,None,None,None)
        mosse_pezzo_finto = []
        x = controlla_altosinistra(casella_finta,scacchiera)
        if(x):
            mosse_pezzo_finto.extend(x)
        x = controlla_alto(casella_finta,scacchiera)
        if(x):
            mosse_pezzo_finto.extend(x)
        x = controlla_altodestra(casella_finta,scacchiera)
        if(x):
            mosse_pezzo_finto.extend(x)
        x = controlla_destra(casella_finta,scacchiera)
        if(x):
            mosse_pezzo_finto.extend(x)
        x = controlla_bassodestra(casella_finta,scacchiera)
        if(x):
            mosse_pezzo_finto.extend(x)
        x = controlla_basso(casella_finta,scacchiera)
        if(x):
            mosse_pezzo_finto.extend(x)
        x = controlla_bassosinistra(casella_finta,scacchiera)
        if(x):
            mosse_pezzo_finto.extend(x)
        x = controlla_sinistra(casella_finta,scacchiera)
        if(x):
            mosse_pezzo_finto.extend(x)
        for mossa in mosse_pezzo_finto:
            if(mossa.tipo_mossa == "mangiata"):
                mosse_pezzo_avversario = scacchiera[mossa.colonna][mossa.riga].pezzo.mosse_possibili()
                if not(cordinate_che_sto_controllando in mosse_pezzo_avversario):
                    if (scacchiera[cordinate_che_sto_controllando.colonna][cordinate_che_sto_controllando.riga].pezzo == None):
                        x = Cordinata(i,j-1,None,i,j)
                    elif (scacchiera[cordinate_che_sto_controllando.colonna][cordinate_che_sto_controllando.riga].pezzo.squadra != s):
                        x = Cordinata(i,j-1,"mangiata",i,j)
                    mosse.append(x)
    if(j+1 < 8):
        casella_finta = Pezzo(i,j+1,s)
        cordinate_che_sto_controllando = Cordinata(i,j+1,None,None,None)
        mosse_pezzo_finto = []
        x = controlla_altosinistra(casella_finta,scacchiera)
        if(x):
            mosse_pezzo_finto.extend(x)
        x = controlla_alto(casella_finta,scacchiera)
        if(x):
            mosse_pezzo_finto.extend(x)
        x = controlla_altodestra(casella_finta,scacchiera)
        if(x):
            mosse_pezzo_finto.extend(x)
        x = controlla_destra(casella_finta,scacchiera)
        if(x):
            mosse_pezzo_finto.extend(x)
        x = controlla_bassodestra(casella_finta,scacchiera)
        if(x):
            mosse_pezzo_finto.extend(x)
        x = controlla_basso(casella_finta,scacchiera)
        if(x):
            mosse_pezzo_finto.extend(x)
        x = controlla_bassosinistra(casella_finta,scacchiera)
        if(x):
            mosse_pezzo_finto.extend(x)
        x = controlla_sinistra(casella_finta,scacchiera)
        if(x):
            mosse_pezzo_finto.extend(x)
        for mossa in mosse_pezzo_finto:
            if(mossa.tipo_mossa == "mangiata"):
                mosse_pezzo_avversario = scacchiera[mossa.colonna][mossa.riga].pezzo.mosse_possibili()
                if not(cordinate_che_sto_controllando in mosse_pezzo_avversario):
                    if (scacchiera[cordinate_che_sto_controllando.colonna][cordinate_che_sto_controllando.riga].pezzo == None):
                        x = Cordinata(i,j+1,None,i,j)
                    elif (scacchiera[cordinate_che_sto_controllando.colonna][cordinate_che_sto_controllando.riga].pezzo.squadra != s):
                        x = Cordinata(i,j+1,"mangiata",i,j)
                    mosse.append(x)
    return mosse

def controlla_difesa_scacco(pezzo, cordinate_pezzi_che_stanno_dando_scacco, scacchiera):
    i = pezzo.colonna
    j = pezzo.riga
    s = pezzo.squadra
    mosse = []
    if(len(cordinate_pezzi_che_stanno_dando_scacco)>1):
        x = controlla_re(pezzo,scacchiera)
        if(x):
            mosse.extend(x)
    elif(len(cordinate_pezzi_che_stanno_dando_scacco) == 0):
        print("Errore: passato alla funzione difesa scacco, un array dei penzi che stanno dando scacco vuoto")
    else:
        isc = cordinate_pezzi_che_stanno_dando_scacco[0].colonna
        jsc = cordinate_pezzi_che_stanno_dando_scacco[0].riga
        if(type(scacchiera[isc][jsc].pezzo) == Cavallo or type(scacchiera[isc][jsc].pezzo) == Pedone or (i-isc == 1 and -2 < j-jsc < 2) or (i-isc == 1 and -2 < j-jsc < 2) or (i == isc and (j == jsc+1 or j == jsc-1))):
            x = controlla_re(pezzo,scacchiera)
            if(x):
                mosse.extend(x)
        else:
            cordinate_caselle_per_la_difesa = []
            if(i == isc):
                if(jsc < j):
                    for p in range(j-jsc-1):
                        x = Cordinata(i,jsc+p+1,None,None,None)
                        cordinate_caselle_per_la_difesa.append(x)
                if(jsc > j):
                    for p in range(jsc-j-1):
                        x = Cordinata(i,jsc-p-1,None,None,None)
                        cordinate_caselle_per_la_difesa.append(x)
            elif(j == jsc):
                if(isc < i):
                    for p in range(i-isc-1):
                        x = Cordinata(isc+p+1,j,None,None,None)
                        cordinate_caselle_per_la_difesa.append(x)
                if(isc > i):
                    for p in range(isc-i-1):
                        x = Cordinata(isc-p-1,j,None,None,None)
                        cordinate_caselle_per_la_difesa.append(x)
            elif(isc > i):
                if(jsc > j):
                    for p in range(isc-i-1):
                        x = Cordinata(isc-p-1,jsc-p-1,None,None,None)
                        cordinate_caselle_per_la_difesa.append(x)
                if(jsc < j):
                    for p in range(isc-i-1):
                        x = Cordinata(isc-p-1,jsc+p+1,None,None,None)
                        cordinate_caselle_per_la_difesa.append(x)
            elif(isc < i):
                if(jsc > j):
                    for p in range(i-isc-1):
                        x = Cordinata(isc+p+1,jsc-p-1,None,None,None)
                        cordinate_caselle_per_la_difesa.append(x)
                if(jsc < j):
                    for p in range(i-isc-1):
                        x = Cordinata(isc+p+1,jsc+p+1,None,None,None)
                        cordinate_caselle_per_la_difesa.append(x)
            else:
                print("ERRORE: passaggio pezzo in una posizione inattesa, controllo difesa scacco")
            for a in range(8):
                for b in range(8):
                    if(scacchiera[a][b].pezzo != None):
                        if(scacchiera[a][b].pezzo.squadra == s):
                            x = scacchiera[a][b].pezzo.mosse_possibili(scacchiera)
                            for cordinata in x:
                                for cordinata_casella in cordinate_caselle_per_la_difesa:
                                    if(cordinata.colonna == cordinata_casella.colonna and cordinata.riga == cordinata_casella.riga):
                                        y = Cordinata(cordinata.colonna,cordinata.riga,None,a,b)
                                        mosse.append(y)
    return mosse

#definizione funzione per convertire gli input in cordinate della scacchiera

def da_input_a_cordinate(input):
    if(len(input) == 2):  #controllo lunghezza stringa
        lettera = input[0]   #da lettera a numero
        lettera = lettera.upper()
        if(lettera.isalpha()):
            posizione = ord(lettera) - ord('A')
            if(-1 < posizione < 8):
                pass
            else:
                return None
        else:
            return None
        numero = input[1]   #numero -1 per la poszione array
        if(numero.isdigit()):
            numero = int(numero)
            if(0 < numero < 9 ):
                numero = numero -1
            else:
                return None
        else:
            return None
        x = Cordinata(posizione,numero,None,None,None)
        return x
    else:
        return None

def scacco_matto(scacchiera):
    Rebianco = posizione_re("b",scacchiera)
    Renero = posizione_re("n",scacchiera)
    x = scacchiera[Rebianco.colonna][Rebianco.riga].pezzo.mosse_possibili(scacchiera)
    if(sotto_scacco(Rebianco,scacchiera) and not(x)):
        return True
    x = scacchiera[Renero.colonna][Renero.riga].pezzo.mosse_possibili(scacchiera)
    if(sotto_scacco(Renero,scacchiera) and not(x)):
        return True

#definizione e creazione della scacchiera

class Cordinata:
    def __init__(self,colonna,riga,tipo_mossa,colonna_vecchia,riga_vecchia):
        self.colonna = colonna
        self.riga = riga
        self.tipo_mossa = tipo_mossa
        self.colonna_vecchia = colonna_vecchia
        self.riga_vecchia = riga_vecchia

class Casella: #Non Davide
    def __init__(self, pezzo, colonna, riga, occupata):
        self.pezzo=pezzo
        self.colonna=colonna
        self.riga=riga
        self.occupata=occupata

def inizializza_scacchiera():
    scacchiera = []
    for i in range(8):
        n = []
        for j in range(8):
            n.insert(i,0)
        scacchiera.append(n)

    i = 0
    while(i<8):
        if(i == 0):
            scacchiera[0][0] = Casella(Torre(0,0,"b",False),0,0,True)
            scacchiera[1][0] = Casella(Cavallo(1,0,"b"),1,0,True)
            scacchiera[2][0] = Casella(Alfiere(2,0,"b"),2,0,True)
            scacchiera[3][0] = Casella(Regina(3,0,"b"),3,0,True)
            scacchiera[4][0] = Casella(Re(4,0,"b",False, False),4,0,True)
            scacchiera[5][0] = Casella(Alfiere(5,0,"b"),5,0,True)
            scacchiera[6][0] = Casella(Cavallo(6,0,"b"),6,0,True)
            scacchiera[7][0] = Casella(Torre(7,0,"b",False),7,0,True)

        elif(i == 1):
            j = 0
            while(j<8):
                scacchiera[j][1] = Casella(Pedone(j,1,"b",False,False),j,1,True)
                j = j+1
        
        elif(i == 6):
            j = 0
            while(j<8):
                scacchiera[j][6] = Casella(Pedone(j,6,"n",False,False),j,6,True)
                j = j+1
        
        elif(i == 7):
            scacchiera[0][7] = Casella(Torre(0,7,"n",False),0,7,True)
            scacchiera[1][7] = Casella(Cavallo(1,7,"n"),1,7,True)
            scacchiera[2][7] = Casella(Alfiere(2,7,"n"),2,7,True)
            scacchiera[3][7] = Casella(Regina(3,7,"n"),3,7,True)
            scacchiera[4][7] = Casella(Re(4,7,"n",False, False),4,7,True)
            scacchiera[5][7] = Casella(Alfiere(5,7,"n"),5,7,True)
            scacchiera[6][7] = Casella(Cavallo(6,7,"n"),6,7,True)
            scacchiera[7][7] = Casella(Torre(7,7,"n",False),7,7,True)

        else:
            j = 0
            while(j<8):
                scacchiera[j][i] = Casella(None,j,i,False)
                j = j+1

        i = i+1

    return scacchiera

def print_scacchiera(scacchiera):
    for i in range(8):  #creazione riga per riga della stampa
        print("---------------------------------")
        riga = "|{}|{}|{}|{}|{}|{}|{}|{}| {}."
        arraypezzi = []
        for j in range(8):  #creazione array con le lettere dei pezzi
            if(scacchiera[j][7-i].occupata == True):
                lettera = scacchiera[j][7-i].pezzo.stampa_lettera()
                if(scacchiera[j][7-i].pezzo.squadra == "b"):
                    arraypezzi.append(" "+lettera+" ")
                elif(scacchiera[j][7-i].pezzo.squadra == "n"):
                    arraypezzi.append("'"+lettera+"'")
                else:
                    print("Errore nel raggiungere la squadra del pezzo")
            elif(scacchiera[j][7-i].occupata == False):
                arraypezzi.append("   ")
            else:
                print("Errore nel print scacchiera")
        print(riga.format(arraypezzi[0],arraypezzi[1],arraypezzi[2],arraypezzi[3],arraypezzi[4],arraypezzi[5],arraypezzi[6],arraypezzi[7],8-i))
    print("---------------------------------")
    print("  A   B   C   D   E   F   G   H  ")

# funzione per spostare un pezzo

def muovi_pezzo(cordinata,scacchiera):
    colonna_vecchia = cordinata.colonna_vecchia
    riga_vecchia = cordinata.riga_vecchia
    colonna_nuova = cordinata.colonna
    riga_nuova = cordinata.riga
    pezzo = type(scacchiera[colonna_vecchia][riga_vecchia].pezzo)
    s = scacchiera[colonna_vecchia][riga_vecchia].pezzo.squadra
    if (cordinata.tipo_mossa == "Arrocco_queenside"):
        scacchiera[colonna_vecchia][riga_vecchia].pezzo.colonna = colonna_nuova
        scacchiera[colonna_vecchia][riga_vecchia].pezzo.riga = riga_nuova
        scacchiera[colonna_vecchia][riga_vecchia].pezzo = None
        scacchiera[colonna_vecchia][riga_vecchia].occupata = False
        scacchiera[colonna_nuova][riga_nuova].occupata = True
        if(pezzo == Re):
            if(s == "b"):
                scacchiera[0][0].pezzo.colonna = 3
                scacchiera[0][0].pezzo.riga = 0
            else:
                scacchiera[0][7].pezzo.colonna = 3
                scacchiera[0][7].pezzo.riga = 7
        if(pezzo == Torre):
            if(s == "b"):
                scacchiera[4][0].pezzo.colonna = 2
                scacchiera[4][0].pezzo.riga = 0
            else:
                scacchiera[4][7].pezzo.colonna = 2
                scacchiera[4][7].pezzo.riga = 7
    elif (cordinata.tipo_mossa == "Arrocco_kingside"):
        scacchiera[colonna_vecchia][riga_vecchia].pezzo.colonna = colonna_nuova
        scacchiera[colonna_vecchia][riga_vecchia].pezzo.riga = riga_nuova
        scacchiera[colonna_vecchia][riga_vecchia].pezzo = None
        scacchiera[colonna_vecchia][riga_vecchia].occupata = False
        scacchiera[colonna_nuova][riga_nuova].occupata = True
        if(pezzo == Re):
            if(s == "b"):
                scacchiera[7][0].pezzo.colonna = 5
                scacchiera[7][0].pezzo.riga = 0
            else:
                scacchiera[7][7].pezzo.colonna = 5
                scacchiera[7][7].pezzo.riga = 7
        if(pezzo == Torre):
            if(s == "b"):
                scacchiera[4][0].pezzo.colonna = 6
                scacchiera[4][0].pezzo.riga = 0
            else:
                scacchiera[4][7].pezzo.colonna = 6
                scacchiera[4][7].pezzo.riga = 7
    elif (cordinata.tipo_mossa == "en_passant"):
        scacchiera[colonna_vecchia][riga_vecchia].pezzo.colonna = colonna_nuova
        scacchiera[colonna_vecchia][riga_vecchia].pezzo.riga = riga_nuova
        scacchiera[colonna_vecchia][riga_vecchia].pezzo = None
        scacchiera[colonna_vecchia][riga_vecchia].occupata = False
        scacchiera[colonna_nuova][riga_nuova].occupata = True
        if(s == "b"):
            scacchiera[colonna_nuova][riga_nuova-1].pezzo = None
            scacchiera[colonna_nuova][riga_nuova-1].occupata = False
        if(s == "n"):
            scacchiera[colonna_nuova][riga_nuova+1].pezzo = None
            scacchiera[colonna_nuova][riga_nuova+1].occupata = False
    elif (cordinata.tipo_mossa == "mangiata"):
        scacchiera[colonna_vecchia][riga_vecchia].pezzo.colonna = colonna_nuova
        scacchiera[colonna_vecchia][riga_vecchia].pezzo.riga = riga_nuova
        scacchiera[colonna_vecchia][riga_vecchia].pezzo = None
        scacchiera[colonna_vecchia][riga_vecchia].occupata = False
    elif (cordinata.tipo_mossa == None and cordinata.tipo_mossa == "pedone_doppio"):
        scacchiera[colonna_vecchia][riga_vecchia].pezzo.colonna = colonna_nuova
        scacchiera[colonna_vecchia][riga_vecchia].pezzo.riga = riga_nuova
        scacchiera[colonna_vecchia][riga_vecchia].pezzo = None
        scacchiera[colonna_vecchia][riga_vecchia].occupata = False
    else:
        print("ERRORE: tipo mossa sbagliata")
    log_scacchiera.append(cordinata)
    
def muovi_pezzo_promozione(cordinata,scacchiera,pezzo_in_cui_promuovere):
    colonna_vecchia = cordinata.colonna_vecchia
    riga_vecchia = cordinata.riga_vecchia
    colonna_nuova = cordinata.colonna
    riga_nuova = cordinata.riga
    s = scacchiera[colonna_vecchia][riga_vecchia].pezzo.squadra
    if (cordinata.tipo_mossa == "Promozione" or cordinata.tipo_mossa == "mangiata_promozione"):
        if (pezzo_in_cui_promuovere == "T"):
            pezzo_promosso = Torre(colonna_nuova,riga_nuova,s,True)
        if (pezzo_in_cui_promuovere == "C"):
            pezzo_promosso = Cavallo(colonna_nuova,riga_nuova,s)
        if (pezzo_in_cui_promuovere == "A"):
            pezzo_promosso = Alfiere(colonna_nuova,riga_nuova,s)
        if (pezzo_in_cui_promuovere == "D"):
            pezzo_promosso = Regina(colonna_nuova,riga_nuova,s)
        scacchiera[colonna_nuova][riga_nuova].pezzo = pezzo_promosso
        scacchiera[colonna_nuova][riga_nuova].occupata = True
        scacchiera[colonna_vecchia][riga_vecchia].pezzo = None
        scacchiera[colonna_vecchia][riga_vecchia].occupata = False
    else:
        print("ERRORE: tipo mossa sbagliata in promozione")
    log_scacchiera.append(cordinata)

def stampa_cordinate(cordinata,indice):
    colonna_vecchia = cordinata.colonna_vecchia
    riga_vecchia = cordinata.riga_vecchia
    colonna_nuova = cordinata.colonna
    riga_nuova = cordinata.riga
    colonna_vecchia = chr(ord('A')+colonna_vecchia)
    riga_vecchia = riga_vecchia+1
    colonna_nuova = chr(ord('A')+colonna_nuova)
    riga_nuova = riga_nuova + 1
    if(cordinata.tipo_mossa == "Arrocco_queenside"):
        print(f"{indice}) {colonna_vecchia}{riga_vecchia} -> 0-0-0")
    elif(cordinata.tipo_mossa == "Arrocco_kingside"):
        print(f"{indice}) {colonna_vecchia}{riga_vecchia} -> 0-0-0")
    elif(cordinata.tipo_mossa == "en_passant"):
        print(f"{indice}) {colonna_vecchia}{riga_vecchia} -> {colonna_nuova}{riga_nuova} e.p.")
    elif(cordinata.tipo_mossa == "Promozione"):
        print(f"{indice}) {colonna_vecchia}{riga_vecchia} -> {colonna_nuova}{riga_nuova} promozione")
    elif(cordinata.tipo_mossa == "mangiata_promozione"):
        print(f"{indice}) {colonna_vecchia}{riga_vecchia} -> {colonna_nuova}{riga_nuova}x promozione")
    elif(cordinata.tipo_mossa == "mangiata"):
        print(f"{indice}) {colonna_vecchia}{riga_vecchia} -> {colonna_nuova}{riga_nuova}x")
    else:
        print(f"{indice}) {colonna_vecchia}{riga_vecchia} -> {colonna_nuova}{riga_nuova}")

def cordinata_posizione_presente(cordinata,s,scacchiera):
    if(cordinata != None):
        colonna = cordinata.colonna
        riga = cordinata.riga
        if(scacchiera[colonna][riga].pezzo != None):
            if(scacchiera[colonna][riga].pezzo.squadra == s):
                return True
        else:
            return False
    else:
        return False

def cordinata_mossa_presente (numero, mosse):
    n = int(numero)
    l = len(mosse)
    if(-1 < n <= l):
        return True
    else:
        return False

def promozione():
    y = 1
    print("0 per tornare indietro")
    k = input("Scegliere il pezzo in cui promuovere\nT - C - A - D\n")
    if(k == 0):
        y = 0
    else:
        while (not(k == "T" or k == "C" or k == "A" or k == "D" or y == 0)):
            if(k == 0):
                y = 0
            else:
                print("ERRORE: pezzo errato")
                print("0 per tornare indietro")
                k = input("Scegliere il pezzo in cui promuovere\nT - C - A - D\n")
    return y


