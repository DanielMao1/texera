# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: virtualidentity.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='virtualidentity.proto',
  package='edu.uci.ics.amber.engine.common',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15virtualidentity.proto\x12\x1f\x65\x64u.uci.ics.amber.engine.common\"\x98\x03\n\x14\x41\x63torVirtualIdentity\x12\x61\n\x1aworkerActorVirtualIdentity\x18\x01 \x01(\x0b\x32;.edu.uci.ics.amber.engine.common.WorkerActorVirtualIdentityH\x00\x12_\n\x19\x63ontrollerVirtualIdentity\x18\x02 \x01(\x0b\x32:.edu.uci.ics.amber.engine.common.ControllerVirtualIdentityH\x00\x12S\n\x13selfVirtualIdentity\x18\x03 \x01(\x0b\x32\x34.edu.uci.ics.amber.engine.common.SelfVirtualIdentityH\x00\x12W\n\x15\x63lientVirtualIdentity\x18\x04 \x01(\x0b\x32\x36.edu.uci.ics.amber.engine.common.ClientVirtualIdentityH\x00\x42\x0e\n\x0csealed_value\"*\n\x1aWorkerActorVirtualIdentity\x12\x0c\n\x04name\x18\x01 \x02(\t\"\x1b\n\x19\x43ontrollerVirtualIdentity\"\x15\n\x13SelfVirtualIdentity\"\x17\n\x15\x43lientVirtualIdentity\"D\n\rLayerIdentity\x12\x10\n\x08workflow\x18\x01 \x02(\t\x12\x10\n\x08operator\x18\x02 \x02(\t\x12\x0f\n\x07layerID\x18\x03 \x02(\t\"\x88\x01\n\x0cLinkIdentity\x12<\n\x04\x66rom\x18\x01 \x02(\x0b\x32..edu.uci.ics.amber.engine.common.LayerIdentity\x12:\n\x02to\x18\x02 \x02(\x0b\x32..edu.uci.ics.amber.engine.common.LayerIdentity\"6\n\x10OperatorIdentity\x12\x10\n\x08workflow\x18\x01 \x02(\t\x12\x10\n\x08operator\x18\x02 \x02(\t\"\x1e\n\x10WorkflowIdentity\x12\n\n\x02id\x18\x01 \x02(\t'
)




_ACTORVIRTUALIDENTITY = _descriptor.Descriptor(
  name='ActorVirtualIdentity',
  full_name='edu.uci.ics.amber.engine.common.ActorVirtualIdentity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='workerActorVirtualIdentity', full_name='edu.uci.ics.amber.engine.common.ActorVirtualIdentity.workerActorVirtualIdentity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='controllerVirtualIdentity', full_name='edu.uci.ics.amber.engine.common.ActorVirtualIdentity.controllerVirtualIdentity', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='selfVirtualIdentity', full_name='edu.uci.ics.amber.engine.common.ActorVirtualIdentity.selfVirtualIdentity', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clientVirtualIdentity', full_name='edu.uci.ics.amber.engine.common.ActorVirtualIdentity.clientVirtualIdentity', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='sealed_value', full_name='edu.uci.ics.amber.engine.common.ActorVirtualIdentity.sealed_value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=59,
  serialized_end=467,
)


_WORKERACTORVIRTUALIDENTITY = _descriptor.Descriptor(
  name='WorkerActorVirtualIdentity',
  full_name='edu.uci.ics.amber.engine.common.WorkerActorVirtualIdentity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='edu.uci.ics.amber.engine.common.WorkerActorVirtualIdentity.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=469,
  serialized_end=511,
)


_CONTROLLERVIRTUALIDENTITY = _descriptor.Descriptor(
  name='ControllerVirtualIdentity',
  full_name='edu.uci.ics.amber.engine.common.ControllerVirtualIdentity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=513,
  serialized_end=540,
)


_SELFVIRTUALIDENTITY = _descriptor.Descriptor(
  name='SelfVirtualIdentity',
  full_name='edu.uci.ics.amber.engine.common.SelfVirtualIdentity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=542,
  serialized_end=563,
)


_CLIENTVIRTUALIDENTITY = _descriptor.Descriptor(
  name='ClientVirtualIdentity',
  full_name='edu.uci.ics.amber.engine.common.ClientVirtualIdentity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=565,
  serialized_end=588,
)


_LAYERIDENTITY = _descriptor.Descriptor(
  name='LayerIdentity',
  full_name='edu.uci.ics.amber.engine.common.LayerIdentity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='workflow', full_name='edu.uci.ics.amber.engine.common.LayerIdentity.workflow', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operator', full_name='edu.uci.ics.amber.engine.common.LayerIdentity.operator', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='layerID', full_name='edu.uci.ics.amber.engine.common.LayerIdentity.layerID', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=590,
  serialized_end=658,
)


_LINKIDENTITY = _descriptor.Descriptor(
  name='LinkIdentity',
  full_name='edu.uci.ics.amber.engine.common.LinkIdentity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='edu.uci.ics.amber.engine.common.LinkIdentity.from', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to', full_name='edu.uci.ics.amber.engine.common.LinkIdentity.to', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=661,
  serialized_end=797,
)


_OPERATORIDENTITY = _descriptor.Descriptor(
  name='OperatorIdentity',
  full_name='edu.uci.ics.amber.engine.common.OperatorIdentity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='workflow', full_name='edu.uci.ics.amber.engine.common.OperatorIdentity.workflow', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operator', full_name='edu.uci.ics.amber.engine.common.OperatorIdentity.operator', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=799,
  serialized_end=853,
)


_WORKFLOWIDENTITY = _descriptor.Descriptor(
  name='WorkflowIdentity',
  full_name='edu.uci.ics.amber.engine.common.WorkflowIdentity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='edu.uci.ics.amber.engine.common.WorkflowIdentity.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=855,
  serialized_end=885,
)

_ACTORVIRTUALIDENTITY.fields_by_name['workerActorVirtualIdentity'].message_type = _WORKERACTORVIRTUALIDENTITY
_ACTORVIRTUALIDENTITY.fields_by_name['controllerVirtualIdentity'].message_type = _CONTROLLERVIRTUALIDENTITY
_ACTORVIRTUALIDENTITY.fields_by_name['selfVirtualIdentity'].message_type = _SELFVIRTUALIDENTITY
_ACTORVIRTUALIDENTITY.fields_by_name['clientVirtualIdentity'].message_type = _CLIENTVIRTUALIDENTITY
_ACTORVIRTUALIDENTITY.oneofs_by_name['sealed_value'].fields.append(
  _ACTORVIRTUALIDENTITY.fields_by_name['workerActorVirtualIdentity'])
_ACTORVIRTUALIDENTITY.fields_by_name['workerActorVirtualIdentity'].containing_oneof = _ACTORVIRTUALIDENTITY.oneofs_by_name['sealed_value']
_ACTORVIRTUALIDENTITY.oneofs_by_name['sealed_value'].fields.append(
  _ACTORVIRTUALIDENTITY.fields_by_name['controllerVirtualIdentity'])
_ACTORVIRTUALIDENTITY.fields_by_name['controllerVirtualIdentity'].containing_oneof = _ACTORVIRTUALIDENTITY.oneofs_by_name['sealed_value']
_ACTORVIRTUALIDENTITY.oneofs_by_name['sealed_value'].fields.append(
  _ACTORVIRTUALIDENTITY.fields_by_name['selfVirtualIdentity'])
_ACTORVIRTUALIDENTITY.fields_by_name['selfVirtualIdentity'].containing_oneof = _ACTORVIRTUALIDENTITY.oneofs_by_name['sealed_value']
_ACTORVIRTUALIDENTITY.oneofs_by_name['sealed_value'].fields.append(
  _ACTORVIRTUALIDENTITY.fields_by_name['clientVirtualIdentity'])
_ACTORVIRTUALIDENTITY.fields_by_name['clientVirtualIdentity'].containing_oneof = _ACTORVIRTUALIDENTITY.oneofs_by_name['sealed_value']
_LINKIDENTITY.fields_by_name['from'].message_type = _LAYERIDENTITY
_LINKIDENTITY.fields_by_name['to'].message_type = _LAYERIDENTITY
DESCRIPTOR.message_types_by_name['ActorVirtualIdentity'] = _ACTORVIRTUALIDENTITY
DESCRIPTOR.message_types_by_name['WorkerActorVirtualIdentity'] = _WORKERACTORVIRTUALIDENTITY
DESCRIPTOR.message_types_by_name['ControllerVirtualIdentity'] = _CONTROLLERVIRTUALIDENTITY
DESCRIPTOR.message_types_by_name['SelfVirtualIdentity'] = _SELFVIRTUALIDENTITY
DESCRIPTOR.message_types_by_name['ClientVirtualIdentity'] = _CLIENTVIRTUALIDENTITY
DESCRIPTOR.message_types_by_name['LayerIdentity'] = _LAYERIDENTITY
DESCRIPTOR.message_types_by_name['LinkIdentity'] = _LINKIDENTITY
DESCRIPTOR.message_types_by_name['OperatorIdentity'] = _OPERATORIDENTITY
DESCRIPTOR.message_types_by_name['WorkflowIdentity'] = _WORKFLOWIDENTITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActorVirtualIdentity = _reflection.GeneratedProtocolMessageType('ActorVirtualIdentity', (_message.Message,), {
  'DESCRIPTOR' : _ACTORVIRTUALIDENTITY,
  '__module__' : 'virtualidentity_pb2'
  # @@protoc_insertion_point(class_scope:edu.uci.ics.amber.engine.common.ActorVirtualIdentity)
  })
_sym_db.RegisterMessage(ActorVirtualIdentity)

WorkerActorVirtualIdentity = _reflection.GeneratedProtocolMessageType('WorkerActorVirtualIdentity', (_message.Message,), {
  'DESCRIPTOR' : _WORKERACTORVIRTUALIDENTITY,
  '__module__' : 'virtualidentity_pb2'
  # @@protoc_insertion_point(class_scope:edu.uci.ics.amber.engine.common.WorkerActorVirtualIdentity)
  })
_sym_db.RegisterMessage(WorkerActorVirtualIdentity)

ControllerVirtualIdentity = _reflection.GeneratedProtocolMessageType('ControllerVirtualIdentity', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLLERVIRTUALIDENTITY,
  '__module__' : 'virtualidentity_pb2'
  # @@protoc_insertion_point(class_scope:edu.uci.ics.amber.engine.common.ControllerVirtualIdentity)
  })
_sym_db.RegisterMessage(ControllerVirtualIdentity)

SelfVirtualIdentity = _reflection.GeneratedProtocolMessageType('SelfVirtualIdentity', (_message.Message,), {
  'DESCRIPTOR' : _SELFVIRTUALIDENTITY,
  '__module__' : 'virtualidentity_pb2'
  # @@protoc_insertion_point(class_scope:edu.uci.ics.amber.engine.common.SelfVirtualIdentity)
  })
_sym_db.RegisterMessage(SelfVirtualIdentity)

ClientVirtualIdentity = _reflection.GeneratedProtocolMessageType('ClientVirtualIdentity', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTVIRTUALIDENTITY,
  '__module__' : 'virtualidentity_pb2'
  # @@protoc_insertion_point(class_scope:edu.uci.ics.amber.engine.common.ClientVirtualIdentity)
  })
_sym_db.RegisterMessage(ClientVirtualIdentity)

LayerIdentity = _reflection.GeneratedProtocolMessageType('LayerIdentity', (_message.Message,), {
  'DESCRIPTOR' : _LAYERIDENTITY,
  '__module__' : 'virtualidentity_pb2'
  # @@protoc_insertion_point(class_scope:edu.uci.ics.amber.engine.common.LayerIdentity)
  })
_sym_db.RegisterMessage(LayerIdentity)

LinkIdentity = _reflection.GeneratedProtocolMessageType('LinkIdentity', (_message.Message,), {
  'DESCRIPTOR' : _LINKIDENTITY,
  '__module__' : 'virtualidentity_pb2'
  # @@protoc_insertion_point(class_scope:edu.uci.ics.amber.engine.common.LinkIdentity)
  })
_sym_db.RegisterMessage(LinkIdentity)

OperatorIdentity = _reflection.GeneratedProtocolMessageType('OperatorIdentity', (_message.Message,), {
  'DESCRIPTOR' : _OPERATORIDENTITY,
  '__module__' : 'virtualidentity_pb2'
  # @@protoc_insertion_point(class_scope:edu.uci.ics.amber.engine.common.OperatorIdentity)
  })
_sym_db.RegisterMessage(OperatorIdentity)

WorkflowIdentity = _reflection.GeneratedProtocolMessageType('WorkflowIdentity', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWIDENTITY,
  '__module__' : 'virtualidentity_pb2'
  # @@protoc_insertion_point(class_scope:edu.uci.ics.amber.engine.common.WorkflowIdentity)
  })
_sym_db.RegisterMessage(WorkflowIdentity)


# @@protoc_insertion_point(module_scope)
