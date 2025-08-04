from entitys.entity import Entity


##################### Доделать когда будет CameraSystem
class RenderSystem:
    @staticmethod
    def sort_entities_by_pos(entities: list[Entity]) -> list[Entity]:
        return sorted(entities, key=lambda e: (
            e.get_component("transform").position.x**2 + e.get_component("transform").position.y**2
            ))

    @staticmethod
    def draw_all_entities(screen, entities: list[Entity]) -> None:
        entities = RenderSystem.sort_entities_by_pos(entities)
        for entity in entities:
            if entity.has_component("transform") and entity.has_component("animation"):
                pos = entity.get_component("transform").position
                image = entity.get_component("animation").get_frame()
                screen.blit(image, (pos.x, pos.y))
