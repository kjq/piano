"""
:mod:`piano.lib.dif`
-------------------------------

.. autofunction:: diff
         
"""
def diff(source, target, ctx='base'):
    """Compares a source and target dictionary and returns the changes.
    """
    print 'Changes in ' + ctx
    for k in source:
        if k not in target:
            print k + ' removed from target'
    for k in target:
        if k not in source:
            print k + ' added in target'
            continue
        if target[k] != source[k]:
            if type(target[k]) not in (dict, list):
                print k + ' changed in target to ' + str(target[k])
            else:
                if type(source[k]) != type(target[k]):
                    print k + ' changed to ' + str(target[k])
                    continue
                else:
                    if type(target[k]) == dict:
                        diff(source[k], target[k], k)
                        continue
                    elif type(target[k]) == list:
                        diff(list_to_dict(source[k]), list_to_dict(target[k]), k)
    print 'Done with changes in ' + ctx
    return

def list_to_dict(l):
    return dict(zip(map(str, range(len(l))), l))