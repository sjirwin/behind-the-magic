class CachedProperty:
    """A descriptor that caches computed values and invalidates when dependencies change."""

    def __init__(self, compute_func, *dependencies):
        self.compute_func = compute_func
        self.dependencies = dependencies

    def __set_name__(self, owner, name):
        self.name = name
        self.cache_name = f"_cache_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self

        # Check if cache is valid
        if not hasattr(instance, self.cache_name):
            # Compute and cache the value
            value = self.compute_func(instance)
            setattr(instance, self.cache_name, value)

        return getattr(instance, self.cache_name)

    def invalidate(self, instance):
        """Remove cached value."""
        if hasattr(instance, self.cache_name):
            delattr(instance, self.cache_name)


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

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)
        # Invalidate all dependent cached properties
        for cached_prop in self.cached_properties:
            cached_prop.invalidate(instance)
