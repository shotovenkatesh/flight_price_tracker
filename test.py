# languages = ['Python', 'C', 'C++', 'C#', 'Java']
#
#
# d1 = None
# d2 = None
#
# for i in languages:
#     print(i)

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# MAX_VALUES=2
# d = dict(list(d.items())[2:])
# print(d)

target_dict = {'k1':'v1', 'k2':'v2', 'k3':'v3'}
new_keys = ['k4','k5','k6']

for key,n_key in zip(target_dict.keys(), new_keys):
    target_dict[n_key] = target_dict.pop(key)

print(target_dict)