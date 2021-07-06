from abc import ABC
from typing import List, Optional, Tuple, Iterable

from core.models.payload import DataPayload, DataFrame, EndOfUpstream
from core.models.tuple import ITuple
from edu.uci.ics.amber.engine.common import LinkIdentity, ActorVirtualIdentity


class DataSendingPolicyExec(ABC):

    def __init__(self, policy_tag: LinkIdentity, batch_size: int, receivers: list[ActorVirtualIdentity]):
        self.policy_tag = policy_tag
        self.batch_size = batch_size
        self.receivers = receivers

    def add_tuple_to_batch(self, tuple_: ITuple) -> Optional[Tuple[ActorVirtualIdentity, DataPayload]]:
        pass

    def no_more(self) -> Tuple[ActorVirtualIdentity, DataPayload]:
        pass

    def reset(self) -> None:
        pass

    def __repr__(self):
        return f"PolicyExec[policy_tag={self.policy_tag}, batch_size={self.batch_size}, receivers={self.receivers}"


class OneToOnePolicyExec(DataSendingPolicyExec):
    def __init__(self, policy_tag: LinkIdentity, batch_size: int, receivers: List[ActorVirtualIdentity]):
        super().__init__(policy_tag, batch_size, receivers)
        self.batch_size = 100
        self.batch = list()

    def add_tuple_to_batch(self, tuple_: ITuple) -> Optional[Tuple[ActorVirtualIdentity, DataPayload]]:
        self.batch.append(tuple_)
        if len(self.batch) == self.batch_size:
            ret_batch = self.batch
            self.reset()
            return self.receivers[0], DataFrame(ret_batch)
        else:
            return None

    def no_more(self) -> Iterable[Tuple[ActorVirtualIdentity, DataPayload]]:
        if len(self.batch) > 0:
            yield self.receivers[0], DataFrame(self.batch)
        yield self.receivers[0], EndOfUpstream()
        self.reset()

    def reset(self) -> None:
        self.batch = list()
#
#   override def reset(): Unit = {
#     batch = new Array[ITuple](batchSize)
#     currentSize = 0
#   }
