class CCar(CVehicle):
    def __init__(self):
        self.fuel_flow = 0

    def set_fuel_flow(self, ff: float):
        self.fuel_flow = ff

    def get_fuel_flow(self):
        return self.fuel_flow