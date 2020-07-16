class Store:
    def __init__(self):
        self.shipments = list()

    def add_shipment(self, shipment):
        self.shipments.append(shipment)
        shipment.set_id(len(self.shipments))
        return self


class Shipment:
    def __init__(self, n_products=0):
        self.id = 0
        self.n_products = n_products
        self.total_cost = 6 + 1.5 * self.n_products

    def add_product(self, adds):
        self.n_products += adds
        return self

    def get_shipment_cost(self):
        return self.total_cost
    
    def set_id(self, id):
        self.id = id
        return self


if __name__ == '__main__':

    mi_tienda = Store()

    pedido1 = Shipment()
    pedido2 = Shipment(1)
    pedido3 = Shipment(3)
    pedido4 = Shipment(6)
    pedido5 = Shipment(10)

    mi_tienda.add_shipment(pedido1)
    mi_tienda.add_shipment(pedido2)
    mi_tienda.add_shipment(pedido3)
    mi_tienda.add_shipment(pedido4)
    mi_tienda.add_shipment(pedido5)

    for shipment in mi_tienda.shipments:
        print(f'Pedido {shipment.id}, precio {shipment.total_cost}')

