class CBird:
    def __init__(self, voice: str = ' ') -> None:
       self.voice = voice

    def set_name(self, voice: str):
        self.voice = voice

    def get_name(self):
        return self.voice

    def sing(self):
        return self.voice

a = CBird()
print(a.get_name())

class CDuck(CBird):
    def __init__(self, voice: str = ' ') -> None:
        self.voice = voice

    def sing(self) -> str:
        return 'Кря-Кря'
dolly = CDuck('ГАВ')
print(dolly.sing())