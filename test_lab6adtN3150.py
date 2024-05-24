from lab6adtN3150 import FormatError, RedoError, UndoError, MyDict


def test_add_element():
    try:
        my_dict = MyDict()
        my_dict['key'] = 'М111КХ11'
        assert my_dict == {'key': 'М111КХ11'}
    except:
        assert False


def test__init__():
    try:
        my_dict = MyDict([('key1', 'М111КХ11'), ('key2', 'М222КХ22')])
        assert my_dict == {'key1': 'М111КХ11', 'key2': 'М222КХ22'}
    except:
        assert False


def test_save_status():
    try:
        my_dict = MyDict([('key1', 'М111КХ11'), ('key2', 'М222КХ22')])
        my_dict.pop('key2')
        my_dict["key3"] = 'М333КХ33'
        assert my_dict.state_array == [{'key1': 'М111КХ11', 'key2': 'М222КХ22'},
                                       {'key1': 'М111КХ11'},
                                       {'key1': 'М111КХ11', 'key3': 'М333КХ33'}]
    except:
        assert False


def test_undo():
    try:
        my_dict = MyDict([('key1', 'М111КХ11'), ('key2', 'М222КХ22')])
        my_dict.pop('key2')
        my_dict["key3"] = 'М333КХ33'
        my_dict.undo()
        assert my_dict == {'key1': 'М111КХ11'}
        my_dict.undo()
        assert my_dict == {'key1': 'М111КХ11', 'key2': 'М222КХ22'}
    except:
        assert False


def test_redo():
    try:
        my_dict = MyDict([('key1', 'М111КХ11'), ('key2', 'М222КХ22')])
        my_dict.pop('key2')
        my_dict["key3"] = 'М333КХ33'
        my_dict.undo()
        my_dict.undo()
        my_dict.redo()
        assert my_dict == {'key1': 'М111КХ11'}
        my_dict.redo()
        assert my_dict == {'key1': 'М111КХ11', 'key3': 'М333КХ33'}
    except:
        assert False


def test_delete_states_after_change_previous_state():
    try:
        my_dict = MyDict([('key1', 'М111КХ11'), ('key2', 'М222КХ22')])
        my_dict.pop('key2')
        my_dict["key3"] = 'М333КХ33'
        my_dict.undo()
        my_dict.undo()
        my_dict["key4"] = 'М444КХ44'
        assert my_dict.state_array == [{'key1': 'М111КХ11', 'key2': 'М222КХ22'},
                                       {'key1': 'М111КХ11', 'key2': 'М222КХ22', 'key4': 'М444КХ44'}]
    except:
        assert False


def test_UndoError():
    try:
        my_dict = MyDict([('key1', 'М111КХ11'), ('key2', 'М222КХ22')])
        my_dict.undo()
        assert False
    except UndoError:
        assert True


def test_RedoError():
    try:
        my_dict = MyDict([('key1', 'М111КХ11'), ('key2', 'М222КХ22')])
        my_dict.redo()
        assert False
    except RedoError:
        assert True


def test_FormatError_in__init__():
    try:
        my_dict = MyDict([('key1', 'М111КХ11'), ('key2', 'что-то')])
        assert False
    except FormatError:
        assert True


def test_FormatError_in__setitem__():
    try:
        my_dict = MyDict()
        my_dict["key"] = 'что-то'
        assert False
    except FormatError:
        assert True


def test_TypeError_in__init__():
    try:
        my_dict = MyDict([('key', 1)])
        assert False
    except TypeError:
        assert True


def test_TypeError_in__setitem__():
    try:
        my_dict = MyDict()
        my_dict["key"] = 1
        assert False
    except TypeError:
        assert True

