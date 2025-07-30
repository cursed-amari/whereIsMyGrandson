from pygame import Surface

from core.settings import ANIMATION_PATH, ENTITY_SIZE
from service.asset_loader import AssetLoader
from service.utils import mirror_surface


class AnimationResource:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._cache = {}
        return cls._instance

    def get_animation_frames(self, entity_type: str, state_name: str) -> list[Surface]:
        name = f"{entity_type}_{state_name}"
        if name not in self._cache:
            self._cache[name] = AssetLoader().load_tile_map(*ANIMATION_PATH[name], size=ENTITY_SIZE[entity_type])
        return self._cache[name]

    def get_mirror_frames(self, entity_type: str, state_name: str) -> list[Surface]:
        name_no_mirror = f"{entity_type}_{state_name}"
        name_mirror = f"{entity_type}_{state_name}_mirror"
        if name_mirror in self._cache:
            return self._cache[name_mirror]
        if name_no_mirror in self._cache:
            frames = mirror_surface(self._cache[name_no_mirror])
            self._cache[name_no_mirror + "_mirror"] = frames
            return frames
        else:
            original_frames = AssetLoader().load_tile_map(*ANIMATION_PATH[name_no_mirror], size=ENTITY_SIZE[entity_type])
            mirror_frames = mirror_surface(original_frames)
            self._cache[name_no_mirror] = original_frames
            self._cache[name_mirror] = mirror_frames
            return mirror_frames

    def get_all_animation_frames(self, entity_type: str) -> dict:
        animations = {}
        for key, value in ANIMATION_PATH.items():
            if entity_type in key:
                if key in self._cache:
                    animations[key] = self._cache[key]
                else:
                    frames = AssetLoader().load_tile_map(*ANIMATION_PATH[key], size=ENTITY_SIZE[entity_type])
                    self._cache[key] = frames
                    animations[key] = frames
        return animations

    def get_all_mirror_frames(self, entity_type: str) -> dict:
        mirror_animations = {}
        for key, value in ANIMATION_PATH.items():
            if entity_type in key:
                if key + "_mirror" in self._cache:
                    mirror_animations[key + "_mirror"] = self._cache[key + "_mirror"]
                else:
                    frames = mirror_surface(AssetLoader().load_tile_map(*ANIMATION_PATH[key],
                                                                        size=ENTITY_SIZE[entity_type]))
                    self._cache[key + "_mirror"] = frames
                    mirror_animations[key + "_mirror"] = frames
        return mirror_animations

    def get_list_animation(self) -> tuple:
        """
        Получить список всех анимаций
        :return: dict_keys
        """
        return tuple(self._cache.keys())
