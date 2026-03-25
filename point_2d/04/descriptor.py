class CachedProperty:
    """Simple cached property descriptor."""

    def __init__(self, compute_func):
        self.compute_func = compute_func

    def __set_name__(self, owner, name):
        self.name = f"_cache_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if not hasattr(instance, self.name):
            setattr(instance, self.name, self.compute_func(instance))
        return getattr(instance, self.name)
