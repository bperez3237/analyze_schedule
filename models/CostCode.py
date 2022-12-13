


class CostCode:
    def __init__(self, bill_code, phase_code, name, qty, uom, mhs, forecast, spent, qtd, mtd):
        self.bill_code = bill_code
        self.phase_code = phase_code
        self.name = name
        self.qty = qty
        self.uom = uom
        self.mhs = mhs
        self.forecast = forecast
        self.spent = spent
        self.qtd = qtd
        self.mtd = mtd
    
    def __str__(self):
        return f'Cost Code: {self.code}'