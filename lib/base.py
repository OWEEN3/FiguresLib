from abc import ABC, abstractmethod

class Figure(ABC):
    
    @property
    @abstractmethod
    def area(self) -> float:
        pass