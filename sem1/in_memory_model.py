from abc import ABC, abstractmethod
from typing import List

class IModelChangeObserver(ABC):
    @abstractmethod
    def apply_update_model(self) -> None:
        pass

class IModelChanger(ABC):
    @abstractmethod
    def notify_change(self, sender) -> None:
        pass

class Texture:
    pass

class Poligon:
    pass

class PoligonalModel:
    def __init__(self, texture: Texture, poligon: Poligon):
        self.texture = texture
        self.poligon = poligon

class Flash:
    pass

class Camera:
    pass

class Scene:
    def __init__(self, scene_id):
        self.id = scene_id
        self.models = []
        self.cameras = []
        self.flashes = []

class ModelStore(IModelChanger):
    def __init__(self, changeObservers: List[IModelChangeObserver]):
        self.models = []
        self.scenes = []
        self.flashes = []
        self.cameras = []
        self.change_observers = changeObservers  # Store observers

    def add_observer(self, observer: IModelChangeObserver):
        self.change_observers.append(observer)

    def remove_observer(self, observer: IModelChangeObserver):
        self.change_observers.remove(observer)

    def notify_change(self, sender) -> None:
        for observer in self.change_observers:
            observer.apply_update_model()

    def get_scene(self, scene_id):
        for scene in self.scenes:
            if scene.id == scene_id:
                return scene
        return None

    def add_scene(self, scene: Scene):
        self.scenes.append(scene)

    def remove_scene(self, scene_id):
        scene = self.get_scene(scene_id)
        if scene:
            self.scenes.remove(scene)

    def add_model(self, model: PoligonalModel):
        self.models.append(model)

    def add_camera(self, camera: Camera):
        self.cameras.append(camera)

    def add_flash(self, flash: Flash):
        self.flashes.append(flash)
