class player():
    def __init__ (self, username, exp, level, health, shield, gold):
        self.exp = exp
        self.level = level
        self.username = username
        self.health = health
        self.shield = shield
        self.gold = gold

    @classmethod
    def from_dict(cls, data):
        return cls(
            username = data['username'],
            exp = data['exp'],
            level = data['level'],
            health = data['health'],
            shield = data['shield'],
            gold = data['gold']
            )
    
    def to_dict(self):
        return { 'username' :  self.username, 'exp' : self.exp, 'level' : self.level, 'health' : self.health, 'shield' : self.shield, 'gold' : self.gold}
