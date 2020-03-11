from p5 import *


class Vehicle:
    def __init__(self, x, y):
        super().__init__()
        self.acceleration = Vector(0, 0)
        self.velocity = Vector(0, 0)
        self.position = Vector(x, y)
        self.size = 8
        self.maxspeed = 8
        self.maxforce = 2.0

    def update(self):

        # Atualizando velocidade atual
        self.velocity += self.acceleration
        # Limitando a velocidade do ser para seu máximo
        self.velocity.limit(upper_limit=self.maxspeed,
                            lower_limit=-self.maxspeed)
        self.position += self.velocity

        # Resetando a aceleração a cada ciclo
        self.acceleration *= 0

    def applyForce(self, force):
        self.acceleration += force

    def eat(self, vFood):
        record = float("inf")
        closestIndex = -1

        for i in range(len(vFood)):
            d = self.position.dist(vFood[i])
            if(d < record):
                record = d
                closestIndex = i

        self.seek(vFood[closestIndex])

        if(record < 5):
            del vFood[closestIndex]

    def seek(self, target):
        # Gerando vetor velocidade que aponta para o target
        desired = target - self.position
        # Limitando a magnitude do vetor gerado para a velocidade máxima aplicavel no corpo
        desired.magnitude = self.maxspeed

        # Vetor Steer apontando para o ponto desejavel, para girar e transladar o ser para o ponto desejado
        # Vetor aceleração a ser aplicado no corpo
        steer = desired - self.acceleration
        # Limitando o vetor para a forma máxima do corpo
        steer.limit(upper_limit=self.maxforce, lower_limit=-self.maxforce)

        self.applyForce(steer)

    def display(self):
        theta = (self.velocity.angle) + (PI / 2)

        # Estilizando o ser
        fill(127)
        stroke(200)
        stroke_weight(1)

        # Iniciando o desenho do ser
        push_matrix()

        # Transformações de posição no canvas
        translate(self.position.x, self.position.y)
        rotate(theta)

        # Iniciando o desenho da forma
        begin_shape()
        vertex(0, -self.size * 2)
        vertex(-self.size, self.size * 2)
        vertex(self.size, self.size * 2)
        end_shape(mode='CLOSE')

        # finalizando desenho
        pop_matrix()
