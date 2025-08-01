class EntityManager:
    def __init__(self):
        self._entities = {}

    def add_entity(self, entity) -> str | None:
        entity_id = id(entity)
        if entity_id not in self._entities:
            self._entities[entity_id] = {
                "type":  entity.entity_type,
                "entity": entity
            }
            return entity_id

    def get_all_entities_by_type(self, entity_type: str) -> list:
        all_entities = []

        for _, value in self._entities.items():
            if value["type"] == entity_type:
                all_entities.append(value["entity"])

        return all_entities

    def get_all_entities(self) -> list:
        all_entities = []

        for _, value in self._entities.items():
            all_entities.append(value["entity"])

        return all_entities

    def get_entity(self, entity_id) -> object | None:
        if entity_id in self._entities:
            return self._entities[entity_id]["entity"]

    def remove_entity(self, entity_id):
        if entity_id in self._entities:
            del self._entities[entity_id]
            return True
        else:
            return False


