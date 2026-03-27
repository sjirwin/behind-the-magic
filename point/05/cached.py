class CachedProperty:
    """A descriptor that caches computed values and invalidates when dependencies change."""

    def __init__(self, compute_func, *dependencies):
        self.compute_func = compute_func
        self.dependencies = dependencies

    def __set_name__(self, owner, name):
        self.name = name
        self.cache_name = f"_cache_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self

        if not hasattr(obj, self.cache_name):
            print(f"Computing {self.name} ...")
            value = self.compute_func(obj)
            setattr(obj, self.cache_name, value)

        return getattr(obj, self.cache_name)

    def invalidate(self, obj):
        """Remove cached value."""
        if hasattr(obj, self.cache_name):
            delattr(obj, self.cache_name)


class InvalidatingAttribute:
    """An attribute that invalidates cached properties when set."""

    def __init__(self):
        self.cached_properties = []

    def __set_name__(self, owner, name):
        self.name = f"_{name}"
        # Find all CachedProperty descriptors that depend on this attribute
        for attr_name in dir(owner):
            attr = getattr(owner, attr_name, None)
            if isinstance(attr, CachedProperty) and name in attr.dependencies:
                self.cached_properties.append(attr)

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        setattr(obj, self.name, value)
        # Invalidate all dependent cached properties
        for cached_prop in self.cached_properties:
            cached_prop.invalidate(obj)
