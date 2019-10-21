from abc import ABCMeta, abstractmethod
from copy import deepcopy


class AbstractDict(object, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, seq=None, **kwargs):
        pass

    @abstractmethod
    def keys(self):
        return

    @abstractmethod
    def values(self):
        return

    @abstractmethod
    def items(self):
        return

    def clear(self):
        for k in list(self.keys()):
            del self[k]

    def get(self, k, d=None):
        if k in self:
            got = self[k]
        else:
            got = d
        return got

    def pop(self, k, d=None):
        popped = self.get(k, d)
        if k in self:
            del self[k]
        return popped

    @abstractmethod
    def update(self, E=None, **F):
        return

    @abstractmethod
    def copy(self):
        return

    def __copy__(self):
        return self.copy()

    @abstractmethod
    def __deepcopy__(self, memodict={}):
        return

    @abstractmethod
    def __getitem__(self, item):
        return

    @abstractmethod
    def __setitem__(self, key, value):
        pass

    @abstractmethod
    def __delitem__(self, key):
        pass

    @abstractmethod
    def __iter__(self):
        return

    @abstractmethod
    def __len__(self):
        return

    @abstractmethod
    def __contains__(self, item):
        return

    @abstractmethod
    def __eq__(self, other):
        return


class AbstractList(object, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, seq=()):
        pass

    @abstractmethod
    def append(self, p_object):
        pass

    @abstractmethod
    def extend(self, iterable):
        pass

    @abstractmethod
    def insert(self, index, p_object):
        pass

    def pop(self, index=None):
        popped = self[index]
        del self[index]
        return popped

    def clear(self):
        for i in range(len(self)):
            del self[i]

    @abstractmethod
    def reverse(self):
        pass

    @abstractmethod
    def sort(self):
        pass

    @abstractmethod
    def copy(self):
        return

    def __copy__(self):
        return self.copy()

    @abstractmethod
    def __deepcopy__(self, memodict={}):
        return

    @abstractmethod
    def __getitem__(self, item):
        return

    @abstractmethod
    def __setitem__(self, key, value):
        pass

    @abstractmethod
    def __delitem__(self, key):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __len__(self):
        return

    @abstractmethod
    def __add__(self, other):
        return

    @abstractmethod
    def __iadd__(self, other):
        pass

    @abstractmethod
    def __contains__(self, item):
        return

    @abstractmethod
    def __eq__(self, other):
        return

    def __reversed__(self):
        reversed_list = deepcopy(self)
        reversed_list.reverse()
        return reversed_list
