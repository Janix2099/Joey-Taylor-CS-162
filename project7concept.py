# Base Classes
class Starship:
    def __init__(self, name):
        self.name = name
        self.hyperdrive = False
        self.shields = False
        self.engines_operational = True

    def travel(self):
        if not self.engines_operational:
            raise SublightEngineError(f"{self.name}'s engines are not operational!")
        print(f"{self.name} is traveling through space...")

# Base Exception
class StarshipMalfunctionError(Exception):
    pass

# Exception Subclasses
class HyperdriveFailureError(StarshipMalfunctionError):
    pass

class ShieldFailureError(StarshipMalfunctionError):
    pass

class SublightEngineError(StarshipMalfunctionError):
    pass

# Starship Subclasses
class XWing(Starship):
    def __init__(self, name):
        super().__init__(name)
        self.hyperdrive = True
        self.shields = True

    def engage_hyperdrive(self):
        if not self.hyperdrive:
            raise HyperdriveFailureError(f"{self.name}'s hyperdrive has failed!")
        print(f"{self.name} is jumping to hyperspace!")

    def raise_shields(self):
        if not self.shields:
            raise ShieldFailureError(f"{self.name}'s shields are down!")
        else:
            print(f"{self.name}'s shields are up and running!")

class TIEFighter(Starship):
    # TIE Fighters have no hyperdrive or shields by default.
    pass

# Game Logic
def simulate_starship_operations(starship):
    try:
        starship.travel()
        if isinstance(starship, XWing):
            starship.engage_hyperdrive()
            starship.raise_shields()
    except StarshipMalfunctionError as e:
        print(f"Alert: {e}")

# Main Game Loop
def main():
    xwing = XWing("Red Five")
    tie_fighter = TIEFighter("Black Leader")

    # Simulate a shield failure for the X-Wing
    xwing.shields = False
    simulate_starship_operations(xwing)

    # TIE Fighter operations (they don't have hyperdrive or shields)
    simulate_starship_operations(tie_fighter)

if __name__ == "__main__":
    main()
