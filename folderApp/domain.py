from dataclasses import dataclass, field
from typing import List

from typeguard import typechecked
from valid8 import validate

from validation.dataclasses import validate_dataclass
from validation.regex import pattern


@typechecked
@dataclass(frozen=True, order=True)
class Object1:
    var_1: str

    def __post_init__(self):
        validate_dataclass(self)

    def __str__(self):
        return self.var_1


@typechecked
@dataclass(frozen=True, order=True)
class Object2:
    var_2: str

    def __post_init__(self):
        validate_dataclass(self)

    def __str__(self):
        return self.var_2


@typechecked
@dataclass(frozen=True, order=True)
class Object3:
    var_3: str

    def __post_init__(self):
        validate_dataclass(self)

    def __str__(self):
        return self.var_3


@typechecked
@dataclass(frozen=True, order=True)
class Object4:
    var_4: str

    def __post_init__(self):
        validate_dataclass(self)
        validate('var_4', self.var_4, min_len=10, max_len=25, custom=pattern('^[0-9]{2}[./-][0-9]{2}[./-][0-9]{4}$'))

    def __str__(self):
        return self.var_4


@typechecked
@dataclass(frozen=True, order=True)
class Object5:
    var_5: str

    def __post_init__(self):
        validate_dataclass(self)
        validate('var_5', self.var_5, min_len=5, max_len=25, custom=pattern('^[0-9]{2}[.:-][0-9]{2}$'))

    def __str__(self):
        return self.var_5


@typechecked
@dataclass(frozen=True, order=True)
class Objects:
    string_1: Object1
    string_2: Object2
    user: Object3
    date: Object4
    time: Object5


@typechecked
@dataclass(frozen=True, order=True)
class ListOfObjects:
    __list: List[Objects] = field(default_factory=list, init=False)

    def length_objectslist(self) -> int:
        return len(self.__list)

    def indexof_objectslist(self, index: int):
        validate('index', index, min_value=0, max_value=self.length_objectslist() - 1)
        return self.__list[index]

    def add_object(self, new_objects: Objects) -> None:
        self.__list.append(new_objects)

    def remove_object(self, index: int) -> None:
        validate('index', index, min_value=0, max_value=self.length_objectslist() - 1)
        del self.__list[index]

    '''
    def sort_by_producer(self) -> None:
        self.__vehicles.sort(key=lambda x: x.producer)

    def sort_by_price(self) -> None:
        self.__vehicles.sort(key=lambda x: x.price)
    '''