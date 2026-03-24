class SqueakyDescriptor:

    def __set_name__(self, owner, name):
        print(f"Squeak! Set name {name=} on {owner=}")
        self.name = f"_{name}"

    def __get__(self, obj, objtype=None):
        print(f"Squeak! Get value from {obj=} of type {objtype=}")
        if obj:
            return getattr(obj, self.name, "Default")
        return getattr(objtype, self.name, "Default")

    def __set__(self, obj, value):
        print(f"Squeak! Set {value=} on {obj=}")
        setattr(obj, self.name, value)

    # def __delete__(self, obj): ...