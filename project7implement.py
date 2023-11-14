# Define the base Starship class
class Starship:
    def __init__(self, name):
        self.name = name
        self.sublight_engines_operational = True

    def is_fully_operational(self):
        return self.sublight_engines_operational

    def status_report(self):
        print(f"{self.name} Status Report: Sublight Engines={'Operational' if self.sublight_engines_operational else 'Not Operational'}.")

# Define the base exception class
class StarshipMalfunctionError(Exception):
    pass

# Define exception subclasses
class HyperdriveFailureError(StarshipMalfunctionError):
    pass

class ShieldFailureError(StarshipMalfunctionError):
    pass

class SublightEngineError(StarshipMalfunctionError):
    pass

# Define the Starship subclasses
class XWing(Starship):
    def __init__(self, name):
        super().__init__(name)
        self.hyperdrive = True
        self.shields = True

    def is_fully_operational(self):
        return (super().is_fully_operational() and self.hyperdrive and self.shields)

    def status_report(self):
        super().status_report()
        print(f"Hyperdrive={'Operational' if self.hyperdrive else 'Not Operational'}, "
              f"Shields={'Up' if self.shields else 'Down'}.")

class TIEFighter(Starship):
    # TIEFighter does not have hyperdrive or shields by default
    def status_report(self):
        super().status_report()

# Instantiate starships
red_five = XWing("Red Five")
black_leader = TIEFighter("Black Leader")

# Simulate a shield malfunction on the X-Wing
red_five.shields = False

# Print the status of all starships
starships = [red_five, black_leader]
print("Starship Status Reports:")
for ship in starships:
    ship.status_report()

# Demonstrate exceptions being raised, caught, and handled
print("\nSimulated Malfunctions:")
for ship in starships:
    try:
        if not ship.is_fully_operational():
            if isinstance(ship, XWing):
                if not ship.hyperdrive:
                    raise HyperdriveFailureError(f"{ship.name} has a hyperdrive failure.")
                if not ship.shields:
                    raise ShieldFailureError(f"{ship.name} has a shield failure.")
            else:
                raise SublightEngineError(f"{ship.name} is not fully operational due to sublight engine failure.")
    except StarshipMalfunctionError as e:
        print(f"Exception caught: {e}")

# An exception that is not handled and crashes the program
# print("\nUnhandled Exception Simulation:")
# raise SublightEngineError("Critical failure: All engines are down!")
