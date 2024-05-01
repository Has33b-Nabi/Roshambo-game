import random
class giuoco:
    def gioca(self):
     mosse = ["sasso","carta","forbice"]
     mossa_scielta = random.choice(mosse)
     return mossa_scielta
    
    def utente(self):
     u_mossas = input("Inserisci la tua mossa tra sasso,carta,forbice:\t")    #u_mossa = mossa utente
     u_mossa = u_mossas.lower()
     if (u_mossa == "sasso" or u_mossa == "carta" or u_mossa == "forbice"):
       return u_mossa
     else:
       return None
    
    def paragone(self,mossa):
     #pari
     if (mossa == "sasso" and u_mossa == "sasso"):
       print("computer:%s you:%s"%(mossa,u_mossa))
       print("siete pari")
     elif(mossa == "carta" and u_mossa == "carta"):
       print("siete pari")
       print("computer:%s you:%s"%(mossa,u_mossa))
     elif(mossa == "forbice" and u_mossa == "forbice"):
         print("siete pari")
         print("computer:%s you:%s"%(mossa,u_mossa))
      #vince il computer
     elif(mossa == "carta" and u_mossa == "sasso"):
        print("vince il computer")
        print("computer:%s you:%s"%(mossa,u_mossa))
     elif(mossa == "forbice" and u_mossa == "carta"):
        print("vince il computer")
        print("computer:%s you:%s"%(mossa,u_mossa))
     elif(mossa == "sasso" and u_mossa == "forbice"):
        print("vince il computer")
        print("computer:%s you:%s"%(mossa,u_mossa))
         #vince l'utente
     elif(mossa == "sasso" and u_mossa == "carta"):
        print("vinci te")
        print("computer:%s you:%s"%(mossa,u_mossa))
     elif(mossa == "carta" and u_mossa == "forbice"):
        print("vinci te")
        print("computer:%s you:%s"%(mossa,u_mossa))
     elif(mossa == "forbice" and u_mossa == "sasso"):
        print("vinci te")    
        print("computer:%s you:%s"%(mossa,u_mossa))           
     else:
        print("error 404, no page found ")  
      
    def repeat(self,mossa):
       maybe = input("vuoi giocare di nuovo yes or no:\t").lower()
       
       if(maybe == "yes" or maybe ==  "no"):
          if(maybe == "yes"):
            mossa = gioco.gioca()
            u_mossa = gioco.utente()
            if ( u_mossa is None):
              print("misspelling or riprovare boomer")
            else:
              gioco.paragone(mossa)
            gioco.repeat(mossa)
          elif(maybe == "no"):
             print("\nfine esecuzione programma\n")
      
       else:
          print("impara a scrivere")
          maybe = input("vuoi giocare di nuovo yes or no:\t").lower()
          if(maybe == "yes" or maybe ==  "no"):
              if(maybe == "yes"):
                mossa = gioco.gioca()
                u_mossa = gioco.utente()
                if ( u_mossa is None):
                  print("misspelling or riprovare boomer")
                else:
                  gioco.paragone(mossa)
                gioco.repeat(mossa)
              elif(maybe == "no"):
                print("\nfine esecuzione programma\n")
          else:
            print("impara a scrivere")
            print("niente rigioco per te")

      
                
       
#main
print("\ninizio esecuzione programma\n")

gioco = giuoco()
mossa = gioco.gioca()
u_mossa = gioco.utente()
if ( u_mossa is None):
   print("misspelling or riprovare boomer")
else:
   gioco.paragone(mossa)
gioco.repeat(mossa)

print("\nfine esecuzione programma\n")
print("written by the honorable mister Haseeb Nabi")

