from franchise import Franchise


class Simulation:
    def run_simulation(self):
        franchises = [Franchise("Pizza"), Franchise("Pasta"), Franchise("Salad")]

        for i in range(5):
            for franchise in franchises:
                print(f"\nWelcome to Frank's food court! we have: Pizza, Pasta, or Salad!")
                franchise.place_order()
