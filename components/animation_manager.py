from components.animation import Animation
from core.settings import ANIMATION_PATH, ENTITY_SIZE
from service.asset_loader import AssetLoader
from service.utils import mirror_surface


class AnimationManager:
    def __init__(self, state):
        """

        :param state: type = AnimationState
        """
        self.state = state
        self.animation = {}

        self.check_animation()

    def check_animation(self):
        if not (self.state.name+"_"+self.state.current_state) in ANIMATION_PATH:
            raise ValueError("idle анимация не найдена в путях анимации")

    def load_all_animations(self) -> None:
        for key, value in ANIMATION_PATH.items():
            if self.state.name in key:
                self.animation[key] = Animation(AssetLoader().load_tile_map(*value, size=ENTITY_SIZE[self.state.name]))

    def load_animation(self, state: str) -> None:
        name = self.state.name + "_" + state
        if name in ANIMATION_PATH and self.state.name in ENTITY_SIZE:
            self.animation[name] = Animation(AssetLoader().load_tile_map(*ANIMATION_PATH[name], size=ENTITY_SIZE[self.state.name]))

    def create_mirror(self, name: str) -> None:
        self.animation[name+"_mirror"] = Animation(mirror_surface(self.animation[name].frames))

    def create_mirror_for_all(self) -> None:
        for key in list(self.animation.keys()):
            self.animation[key + "_mirror"] = Animation(mirror_surface(self.animation[key].frames))

    def get_current_animation(self):
        name = self.state.name+"_"+self.state.current_state
        if name in self.animation:
            return self.animation[name]
        else:
            raise ValueError(
                f"Текущего состояния {self.state.current_state} не найденно в анимациях. Доступные: {list(self.animation.keys())}"
            )

    def get_animation(self, state) -> Animation:
        """
        Возвращает объект анимации
        :param state: имя состояния, анимация для которого должна быть анимация в списке загруженных
        :return: объект анимации
        """
        name = self.state.name + "_" + state
        if name in self.animation:
            return self.animation[name]
        else:
            raise ValueError(f"Имя {name} не найденно в анимациях. Доступные: {list(self.animation.keys())}")

    def get_list_animation(self) -> tuple:
        """
        Получить список всех анимаций
        :return: dict_keys
        """
        return tuple(self.animation.keys())
