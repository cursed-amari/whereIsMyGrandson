from core.settings import COMPONENTS


class Entity:
    _components = {}

    def add_component(self, component: str) -> None:
        if component in COMPONENTS:
            self._components[component] = ...
        else:
            raise ValueError(f"Component {component} not found in COMPONENTS")

    def get_component(self, component: str) -> object:
        component = self._components.get(component)
        if component:
            return component
        else:
            raise ValueError(f"Component {component} not found")

    def has_component(self, component: str) -> bool:
        return component in self._components
