class CachedProperty:
    """Simple cached property descriptor."""

    def __init__(self, compute_func):
        self.compute_func = compute_func

    def __set_name__(self, owner, name):
        self.cached_name = f"_cache_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self

        if not hasattr(obj, self.cached_name):
            setattr(obj, self.cached_name, self.compute_func(obj))

        return getattr(obj, self.cached_name)
