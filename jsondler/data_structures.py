import os
from collections import OrderedDict

import numpy as np
import psutil

from jsondler._lib.general_utils import generate_random_string
from jsondler._lib.abstract_structures import AbstractDict, AbstractList


class DataStructure(object):

    def __init__(self, seq, item_struct, item_block_s=100, low_memory='auto', memmap_path=None):
        if item_struct is None:
            print("ERROR: no valid values for 'seq' and 'item_struct' arguments")
            return
        try:
            seq_l = len(seq)
        except TypeError:
            seq_l = 0
        num_items_blocks = seq_l // item_block_s + 1
        shape = (num_items_blocks * item_block_s, *get_item_shape(item_struct))

        if low_memory.lower() == 'auto':
            needed_mem = 200 * np.prod(shape)
            avail_mem = psutil.virtual_memory().available
            if needed_mem >= avail_mem:
                low_memory = True
            else:
                low_memory = False
        if low_memory:
            if memmap_path is None:
                memmap_path = "ds_%s.memmap" % generate_random_string(10)
            if not os.path.exists(os.path.dirname(memmap_path)):
                os.makedirs(os.path.dirname(memmap_path))
            self.data_array = np.memmap()
        else:
            self.data_array = np.zeros()

        # inner keys


class DataDict(DataStructure, AbstractDict):

    def __init__(self, seq=None, item_struct=None, item_block_s=100, low_memory='auto', memmap_path=None, **kwargs):
        if seq is None:
            seq = ()
        if isinstance(seq, dict):
            seq_items = seq.items()
        else:
            seq_items = seq
        if seq_items and item_struct is None:
            item_struct = get_item_struct(item=seq_items[0][1])

        super(DataDict, self).__init__(seq=seq_items, item_struct=item_struct, item_block_s=item_block_s,
                                       low_memory=low_memory, memmap_path=memmap_path)

        self.keys_order = OrderedDict()
        i = 0
        for seq_ik, seq_iv in seq_items:
            self.keys_order[seq_ik] = i
            self[seq_ik] = seq_iv
            i += 1

    def keys(self):
        return self.keys_order.keys()

    def values(self):
        for key in self:
            yield self[key]

    def items(self):
        for key in self:
            yield key, self[key]

    def update(self, E=None, **F):
        return

    def copy(self):
        return

    def __deepcopy__(self, memodict={}):
        return

    def __getitem__(self, item):
        return

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __iter__(self):
        for key in self.keys_order.keys():
            yield key

    def __len__(self):
        return len(self.keys_order)

    def __contains__(self, item):
        if item in self.keys_order:
            return True
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, DataDict):
            if other.keys_order == self.keys_order:
                return True
        return False


class DataList(DataStructure, AbstractList):

    def __init__(self, seq=(), item_struct=None, item_block_s=100, low_memory='auto', memmap_path=None):
        if seq and item_struct is None:
            item_struct = get_item_struct(item=seq[0])

        super(DataList, self).__init__(seq=seq, item_struct=item_struct, item_block_s=item_block_s,
                                       low_memory=low_memory, memmap_path=memmap_path)

        for seq_i in seq:
            self.append(seq_i)

    def append(self, p_object):
        pass

    def extend(self, iterable):
        pass

    def insert(self, index, p_object):
        pass

    def reverse(self):
        pass

    def sort(self):
        pass

    def copy(self):
        return

    def __deepcopy__(self, memodict={}):
        return

    def __delitem__(self, key):
        pass

    def __getitem__(self, item):
        return

    def __setitem__(self, key, value):
        pass

    def __contains__(self, item):
        return

    def __eq__(self, other):
        return

    def __iter__(self):
        return

    def __len__(self):
        return

    def __add__(self, other):
        return

    def __iadd__(self, other):
        pass


def get_item_struct(item):
    if isinstance(item, dict):
        pass
    else:
        pass
    return


def get_item_shape(item_struct):

    return
