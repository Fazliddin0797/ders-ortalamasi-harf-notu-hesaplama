
def belge(ort):
  if 50<=ort<60:
      print("E")
  elif 60<=ort<70:
      print("D")
  elif 70<=ort<80:
      print("C")
  elif 80<=ort<90:
      print("B")
  elif ort>=90:
      print("A")
  else:
      print("yeterli puan alamadınız")

       
def ortalama(ders_sayısı):
    toplam=0
    for sayı in range(ders_sayısı):
       print(sayı+1,".ders notunu giriniz:")
       puan=int(input())
       toplam=toplam+puan
 
       
    ders_ortalaması=toplam/ders_sayısı
    return belge(ders_ortalaması)
ders_sayısı=int(input("Ders sayısını giriniz: "))
ortalama(ders_sayısı)
yakun = int(input ('programı bitirmek için enter tuşuna basınız'))      
    
            
    
        
    
    