import vehicles
import catalogue


fleet = list()

fleet.append(vehicles.Vehiculo('rojo', 2))
fleet.append(vehicles.Coche('azul', 4, 120, 1900))
fleet.append(vehicles.Camioneta('amarillo', 4, 100, 2500, 500))
fleet.append(vehicles.Bicicleta('negro', 2, 'deportiva'))
fleet.append(vehicles.Motocicleta('verde', 2, 'urbana', 110, 1500))

catalogue.catalogar(fleet.copy())

n_wheels = 2
catalogue.check_wheels(fleet.copy(), n_wheels=n_wheels)
