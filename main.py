#sınıflar
#self(self yerine başka birşey yazılabilir)--this,fonksiyondan class içine ulaşmanı sağlar

class Human:
    name="Veli"

    #built-in
    #constactor->nesne oluşturulduğunda çalışan alan
    #initialize
    def __init__(self,name):
        self.name=name
        print("bir human instance'i üretildi")
    def __str__(self) -> str:
        return f"srt fonksiyonundan dönen değer: {self.name}"
    def talk(self,sentence):
        name="Ali"
        #print(f"Human:{sentence}")
        print(f"{self.name}:{sentence}")

    def walk(self):
        #print("human is walking..")
        print(f"{self.name} is walking..")

    
#instance-->örnek
human1=Human("enes")
#human1.name="Enes"
human1.talk("Merhaba")
human1.walk()
print(human1)
################

human2=Human("halit")
human2.talk("selam")
human2.walk()
print(human2)

###############
Human("ali").talk("merhaba")