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