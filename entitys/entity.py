class Entity:
    def __init__(self, entity_type):
        self.entity_type
        self._components = {}

    def add_component(self, name: str, component: object) -> None:
        self._components[name] = component

    def get_component(self, component_name: str) -> object:
        component = self._components.get(component_name)
        if component:
            return component
        else:
            raise ValueError(f"Component \"{component_name}\" not found")

    def has_component(self, component_name: str) -> bool:
        return component_name in self._components
