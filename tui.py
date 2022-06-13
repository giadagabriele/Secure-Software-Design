#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import datetime
import sys
from typing import Any, Tuple, Callable

from valid8 import validate, ValidationError

from folderApp.domain import ListOfObjects, Objects, Object1, Object2, Object3, Object4, Object5
from folderApp.menu import Menu, Description, Entry


class TUI:

    def __init__(self):
        self.__menu = Menu.Builder(Description('List of Objects'), auto_select=lambda: self.__print_objectslist())\
            .with_entry(Entry.create('1', 'Add session', on_selected=lambda: self.__add_object()))\
            .with_entry(Entry.create('2', 'Remove session', on_selected=lambda: self.__remove_object()))\
            .with_entry(Entry.create('0', 'Exit', on_selected=lambda: print('Bye!'), is_exit=True))\
            .build()
        self.__list = ListOfObjects()

    def __print_objectslist(self) -> None:
        print_sep = lambda: print('-' * 100)
        print_sep()
        fmt = '%3s %-10s %-20s %-20s %-20s %10s'
        print(fmt % ('#', 'VAR_1', 'VAR_2', 'VAR_3', 'VAR_4', 'VAR_5'))
        print_sep()
        for index in range(self.__list.length_objectslist()):
            singleobjectlist = self.__list.indexof_objectslist(index)
            print(fmt % (index + 1, singleobjectlist.string_1.value, singleobjectlist.string_2.value, singleobjectlist.user.value, singleobjectlist.datetime_1.value, singleobjectlist.datetime_2.value))
        print_sep()

    def __add_object(self) -> None:
        new_object= Objects(*self.__read_object())
        self.__list.add_object(new_object)
        print('Object added!')

    def __remove_object(self) -> None:
        def builder(value: str) -> int:
            validate('value', int(value), min_value=0, max_value=self.__list.length_objectslist())
            return int(value)

        index = self.__read('Index (0 to cancel)', builder)
        if index == 0:
            print('Cancelled!')
            return
        self.__list.remove_object(index - 1)
        print('Object removed!')

    def run(self) -> None:
        try:
            self.__menu.run()
        except:
            print('Panic error!', file=sys.stderr)

    @staticmethod
    def __read(prompt: str, builder: Callable) -> Any:
        while True:
            try:
                line = input(f'{prompt}: ')
                res = builder(line.strip())
                return res
            except (TypeError, ValueError, ValidationError) as e:
                print(e)

    def __read_object(self) -> Tuple[Object1, Object2, Object3, Object4, Object5]:
        first = self.__read('VAR1', Object1)
        second = self.__read('VAR2', Object2)
        third = self.__read('VAR3', Object3)
        fourth = self.__read('VAR4', Object4)
        fifth = self.__read('VAR5', Object5)
        return first, second, third, fourth, fifth


def main(name: str):
    if name == '__main__':
        TUI().run()

main(__name__)
