# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# This is the base class.
class Vehicle:
    pass


class FlightVehicle(Vehicle):
    pass


class Starship(FlightVehicle):
    pass


class Airplane(FlightVehicle):
    pass

# Ground Vehicles

# These are the subclasses. They will hitch it's wagon onto the base class of vehicle ↓


class GroundVehicle(Vehicle):
    pass


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass
