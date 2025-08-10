import pygame

from entitys.entity import Entity


##################### Доделать когда будет CameraSystem
class RenderSystem:
    @staticmethod
    def sort_entities_by_pos(entities: list[Entity]) -> list[Entity]:
        return sorted(entities, key=lambda e: (
            e.get_component("transform").position.x**2 + e.get_component("transform").position.y**2
            ))

    @staticmethod
    def _draw_entity(screen, entity: Entity, camera_system) -> None:
        if not (entity.has_component("transform") and entity.has_component("animation")):
            return

        pos: pygame.Vector2 = entity.get_component("transform").position
        image: pygame.Surface = entity.get_component("animation").get_frame()
        zoom = camera_system.current_zoom

        if zoom != 1.0:
            new_w = max(1, int(image.get_width() * zoom))
            new_h = max(1, int(image.get_height() * zoom))
            image = pygame.transform.smoothscale(image, (new_w, new_h))

        screen_pos = camera_system.world_to_screen(pos)

        screen.blit(image, (int(screen_pos.x), int(screen_pos.y)))

    @staticmethod
    def draw_player(screen, entities: list[Entity], camera_system) -> None:
        for entity in entities:
            if entity.entity_type == "player":
                RenderSystem._draw_entity(screen, entity, camera_system)

    @staticmethod
    def draw_all_enemies(screen, entities: list[Entity], camera_system) -> None:
        for entity in RenderSystem.sort_entities_by_pos(entities):
            if entity.entity_type == "enemy":
                RenderSystem._draw_entity(screen, entity, camera_system)

    @staticmethod
    def draw_all_entities(screen, entities: list[Entity], camera_system) -> None:
        """Отрисовка всех типов сущностей (игрок + враги)."""
        RenderSystem.draw_player(screen, entities, camera_system)
        RenderSystem.draw_all_enemies(screen, entities, camera_system)

    @staticmethod
    def draw_map_layers(screen, map_layers: list[pygame.Surface], camera_system) -> None:
        """
        Отрисовать слои карты. Ожидается, что слой начинается в мировых координатах (0,0).
        """
        zoom = camera_system.current_zoom

        for layer in map_layers:
            if zoom != 1.0:
                new_w = max(1, int(layer.get_width() * zoom))
                new_h = max(1, int(layer.get_height() * zoom))
                scaled = pygame.transform.smoothscale(layer, (new_w, new_h))
            else:
                scaled = layer

            top_left_screen = camera_system.world_to_screen(pygame.Vector2(0, 0))
            screen.blit(scaled, (int(top_left_screen.x), int(top_left_screen.y)))

