from entitys.entity import Entity


##################### Доделать когда будет CameraSystem
class RenderSystem:
    @staticmethod
    def sort_entities_by_pos(entities: list[Entity]) -> list[Entity]:
        return sorted(entities, key=lambda e: (
            e.get_component("transform").position.x**2 + e.get_component("transform").position.y**2
            ))

    @staticmethod
    def draw_player(screen, entities: list[Entity], camera_system) -> None:
        entities = RenderSystem.sort_entities_by_pos(entities)
        offset = camera_system.get_final_offset()
        for entity in entities:
            if entity.has_component("transform") and entity.has_component("animation") and entity.entity_type == "player":
                pos = entity.get_component("transform").position - offset
                image = entity.get_component("animation").get_frame()
                screen.blit(image, (pos.x, pos.y))

    @staticmethod
    def draw_all_enemies(screen, entities: list[Entity], camera_system) -> None:
        entities = RenderSystem.sort_entities_by_pos(entities)
        offset = camera_system.get_final_offset()
        for entity in entities:
            if entity.has_component("transform") and entity.has_component(
                    "animation") and entity.entity_type != "player":
                pos = entity.get_component("transform").position - offset
                image = entity.get_component("animation").get_frame()
                screen.blit(image, (pos.x, pos.y))

    @staticmethod
    def draw_all_entities(screen, entities: list[Entity], camera_system) -> None:
        """Отрисовка всех типов сущностей (игрок + враги)."""
        RenderSystem.draw_player(screen, entities, camera_system)
        RenderSystem.draw_all_enemies(screen, entities, camera_system)

