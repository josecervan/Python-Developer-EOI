# Constants
ENTRANCE_A = 'A'
ENTRANCE_B = 'B'


class Client:
    def __init__(self, id, mask, entrance, exit, gel, gloves, still_in):
        self.id = id
        self.mask = mask
        self.entrance = entrance
        self.exit = exit
        self.gel = gel
        self.gloves = gloves
        self.still_in = still_in

    def wearing_mask(self):
        return self.mask

    def client_entrance(self):
        return self.entrance

    def client_exit(self):
        return self.exit

    def gel_on(self):
        return self.gel

    def wearing_gloves(self):
        return self.gloves

    def is_still_in(self):
        return self.still_in

    def refactor_mask(self):
        self.mask = not(self.wearing_mask())
        return self

    def refactor_entrance(self):
        if self.entrance == ENTRANCE_B:
            self.entrance = ENTRANCE_A
            print('Atención, cliente ' + str(self.id) + ', se debe entrar por la puerta A y salir por la puerta B')

        return self

    def refactor_exit(self):
        if self.exit == ENTRANCE_A:
            self.exit = ENTRANCE_B
        return self

    def refactor_gel(self):
        self.gel = not(self.gel_on())
        return self

    def refactor_gloves(self):
        self.gloves = not(self.wearing_gloves())
        return self

    def refactor_is_still_in(self):
        self.still_in = not(self.is_still_in())
        return self


if __name__ == '__main__':

    client1 = Client(1, True, ENTRANCE_A, ENTRANCE_B, True, False, False)
    client2 = Client(2, False, ENTRANCE_A, ENTRANCE_B, False, False, False)
    client3 = Client(3, False, ENTRANCE_B, ENTRANCE_A, False, False, False)

    clients = [client1, client2, client3]

    while False in [client1.still_in, client2.still_in, client3.still_in]:
        for client in clients:
            if client.entrance == ENTRANCE_A:
                client.refactor_is_still_in()
            elif client.entrance == ENTRANCE_B:
                client.refactor_entrance()
                client.refactor_is_still_in()

            if client.is_still_in():
                print('El cliente', client.id, 'ha entrado en el centro comercial')

            .
            .
            .





