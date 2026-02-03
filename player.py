class player():
    def __init__ (self, username, health, shield, gold):
        self.username = username
        self.health = health
        self.shield = shield
        self.gold = gold

    @classmethod
    def from_dict(cls, data):
        return cls(
            username = data['username'],
            health = data['health'],
            shield = data['shield'],
            gold = data['gold']
            )
    
    def to_dict(self):
        return { 'username' : self.username, 'health' : self.health, 'shield' : self.shield, 'gold' : self.gold}
