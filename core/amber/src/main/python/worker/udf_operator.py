from abc import ABC
from typing import Union, Iterable

from .data_tuple import DataTuple, InputExhausted, ITuple
from .link_identity import LinkIdentity


class UDFOperator(ABC):
    """
    Base class for row-oriented one-table input, one-table output user-defined operators. This must be implemented
    before using.
    """

    def __init__(self):
        pass

    def open(self, *args, **kwargs) -> None:
        pass

    def process_texera_tuple(self, tuple: Union[DataTuple, InputExhausted],
                             input: LinkIdentity) -> Iterable[ITuple]:
        pass

    def close(self) -> None:
        pass
