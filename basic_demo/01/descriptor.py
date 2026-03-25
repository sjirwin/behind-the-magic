class SqueakyDescriptor:

    def __get__(self, obj, objtype=None):
        print(f"Squeak! Get value from {obj=} of type {objtype=}")
        if obj:
            return getattr(obj, "_squeaky", "Default")
        return getattr(objtype, "_squeaky", "Default")