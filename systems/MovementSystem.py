class MovementSystem:
    @staticmethod
    def update(dt, entities):
        for entity in entities:
            transform = entity.get_component("transform")
            movement = entity.get_component("movement")

            if movement.velocity.length_squared() > 0:
                movement.velocity = movement.velocity.normalize() * movement.speed

            transform.position += movement.velocity * dt