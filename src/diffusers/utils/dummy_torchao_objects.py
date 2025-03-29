# This file is autogenerated by the command `make fix-copies`, do not edit.
from ..utils import DummyObject, requires_backends


class TorchAoConfig(metaclass=DummyObject):
    _backends = ["torchao"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["torchao"])

    @classmethod
    def from_config(cls, *args, **kwargs):
        requires_backends(cls, ["torchao"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["torchao"])
