def dict_intersection(a: dict, b: dict):
    """Elements that are the same in a and b"""
    return {k: v for k, v in a.items() if k in b and b[k] == v}


def dict_change(a: dict, b: dict):
    """Elements of b that are not the same in a"""
    return {k: v for k, v in b.items() if k not in a or a[k] != v}


def dict_delete(a: dict, b: dict):
    """Elements that are in a but not in b"""
    return [k for k in a if k not in b]