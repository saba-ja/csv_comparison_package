def call_each(func):
    def func_wrapper(name):
        if isinstance(name, list):
            for val in name:
                func(val)
        else:
            func(name)

    return func_wrapper
