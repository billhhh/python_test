import numpy as np
import time
import collections


def gen_list_random():
    r_list = []
    for _ in range(10000000):
        r_list.append(np.random.randint(low=0, high=100))
    return r_list


def sorted_set_del_dup(r_list):
    return sorted(set(r_list), key=r_list.index)


def iter_del_dup(r_list):
    o_list = []
    for i in r_list:
        if not i in o_list:
            o_list.append(i)
    return o_list


def ordered_dict_del_dup(r_list):
    order_dict = collections.OrderedDict()
    for i in r_list:
        if i not in order_dict:
            order_dict[i] = 1
    return list(order_dict.keys())


def main():
    r_list = gen_list_random()

    # sorted(set())
    t0 = time.time()
    o_list = sorted_set_del_dup(r_list)
    print("sorted_set_del_dup() process time (seconds):", time.time() - t0)

    # iter
    t0 = time.time()
    o_list = iter_del_dup(r_list)
    print("iter_del_dup() process time (seconds):", time.time() - t0)

    # ordered dict
    t0 = time.time()
    o_list = ordered_dict_del_dup(r_list)
    print("ordered_dict_del_dup() process time (seconds):", time.time() - t0)


if __name__ == '__main__':
    main()
