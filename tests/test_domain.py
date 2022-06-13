import datetime
from unittest.mock import Mock

import pytest

from folderApp.domain import Objects, Object1, Object2, Object3, Object4, Object5, ListOfObjects
from folderApp.menu import Entry, Key, Description


@pytest.fixture
def objects():
    return [
        Objects(Object1('aksdkja'), Object2('ajksba'), Object3('giada'), Object4(datetime.datetime.now()), Object5(datetime.datetime.now())),
    ]


def test_add_object(objects):
    list_obj = ListOfObjects()
    size = 0
    for obj in objects:
        list_obj.add_object(obj)
        size += 1
        assert list_obj.length_objectslist() == size
        assert list_obj.indexof_objectslist(size - 1) == obj


def test_entry_on_selected():
    mocked_on_selected = Mock()
    entry = Entry(Key('1'), Description('Say hi'), on_selected=lambda: mocked_on_selected())
    entry.on_selected()
    mocked_on_selected.assert_called_once()