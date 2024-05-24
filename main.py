from lab6adtN3150 import MyDict


my_dict = MyDict([('key1', 'М111КХ11')])
my_dict['key3'] = 'М322КХ33'
my_dict['key2'] = 'М222КХ22'
my_dict['key4'] = 'М444КХ44'
my_dict['key5'] = 'М555КХ55'


my_dict.popitem()

print(my_dict)
my_dict.undo()
print(my_dict)
my_dict['key5'] = 'М666КХ66'
