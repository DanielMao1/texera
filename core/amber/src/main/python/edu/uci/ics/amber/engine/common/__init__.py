# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: edu/uci/ics/amber/engine/common/ambermessage2.proto, edu/uci/ics/amber/engine/common/statetransition2.proto, edu/uci/ics/amber/engine/common/virtualidentity.proto
# plugin: python-betterproto
import betterproto
from dataclasses import dataclass


@dataclass(eq=False, repr=False)
class ActorVirtualIdentity(betterproto.Message):
    """sealed trait ActorVirtualIdentity"""

    worker_actor_virtual_identity: "WorkerActorVirtualIdentity" = (
        betterproto.message_field(1, group="sealed_value")
    )
    controller_virtual_identity: "ControllerVirtualIdentity" = (
        betterproto.message_field(2, group="sealed_value")
    )
    self_virtual_identity: "SelfVirtualIdentity" = betterproto.message_field(
        3, group="sealed_value"
    )
    client_virtual_identity: "ClientVirtualIdentity" = betterproto.message_field(
        4, group="sealed_value"
    )


@dataclass(eq=False, repr=False)
class WorkerActorVirtualIdentity(betterproto.Message):
    """
    final case class WorkerActorVirtualIdentity (    name: String ) extends
    ActorVirtualIdentity
    """

    name: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ControllerVirtualIdentity(betterproto.Message):
    """
    final case class ControllerVirtualIdentity extends ActorVirtualIdentity
    """

    name: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class SelfVirtualIdentity(betterproto.Message):
    """final case class SelfVirtualIdentity extends ActorVirtualIdentity"""

    name: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ClientVirtualIdentity(betterproto.Message):
    """final case class ClientVirtualIdentity extends ActorVirtualIdentity"""

    name: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class LayerIdentity(betterproto.Message):
    """
    final case class LayerIdentity (    workflow: String,    operator: String,
    layerID: String )
    """

    workflow: str = betterproto.string_field(1)
    operator: str = betterproto.string_field(2)
    layer_id: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class LinkIdentity(betterproto.Message):
    """
    final case class LinkIdentity (    from: LayerIdentity,    to:
    LayerIdentity )
    """

    from_: "LayerIdentity" = betterproto.message_field(1)
    to: "LayerIdentity" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class OperatorIdentity(betterproto.Message):
    """
    final case class LinkIdentity (    workflow: String,    operator: String )
    """

    workflow: str = betterproto.string_field(1)
    operator: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class WorkflowIdentity(betterproto.Message):
    """final case class WorkflowIdentity (    id: String )"""

    id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class Uninitialized(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class Ready(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class Running(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class Paused(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class Completed(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class Recovering(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class WorkerState(betterproto.Message):
    uninitialized: "Uninitialized" = betterproto.message_field(1, group="sealed_value")
    ready: "Ready" = betterproto.message_field(2, group="sealed_value")
    running: "Running" = betterproto.message_field(3, group="sealed_value")
    paused: "Paused" = betterproto.message_field(4, group="sealed_value")
    completed: "Completed" = betterproto.message_field(5, group="sealed_value")
    recovering: "Recovering" = betterproto.message_field(6, group="sealed_value")


@dataclass(eq=False, repr=False)
class DataPayload(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class ControlInvocation(betterproto.Message):
    command_id: int = betterproto.int64_field(1)
    command: "_architecture_worker__.ControlCommand" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class ControlPayload(betterproto.Message):
    control_invocation: "ControlInvocation" = betterproto.message_field(
        1, group="sealed_value"
    )
    return_payload: "ReturnPayload" = betterproto.message_field(2, group="sealed_value")


@dataclass(eq=False, repr=False)
class ReturnPayload(betterproto.Message):
    original_command_id: int = betterproto.int64_field(1)
    return_value: "_architecture_worker__.ControlCommand" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class WorkflowDataMessage(betterproto.Message):
    from_: "ActorVirtualIdentity" = betterproto.message_field(1)
    sequence_number: int = betterproto.int64_field(2)
    payload: "DataPayload" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class WorkflowControlMessage(betterproto.Message):
    from_: "ActorVirtualIdentity" = betterproto.message_field(1)
    sequence_number: int = betterproto.int64_field(2)
    payload: "ControlPayload" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class WorkflowMessage(betterproto.Message):
    """sealed trait WorkflowMessage"""

    workflow_data_message: "WorkflowDataMessage" = betterproto.message_field(
        1, group="sealed_value"
    )
    workflow_control_message: "WorkflowControlMessage" = betterproto.message_field(
        2, group="sealed_value"
    )


from ..architecture import worker as _architecture_worker__
