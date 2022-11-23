# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: discovery.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='discovery.proto',
  package='dronecode_sdk.rpc.discovery',
  syntax='proto3',
  serialized_options=_b('\n\032io.dronecode_sdk.discoveryB\016DiscoveryProto'),
  serialized_pb=_b('\n\x0f\x64iscovery.proto\x12\x1b\x64ronecode_sdk.rpc.discovery\"#\n!SubscribeDiscoveredSystemsRequest\"X\n\x18\x44iscoveredSystemResponse\x12<\n\x0bsystem_info\x18\x01 \x01(\x0b\x32\'.dronecode_sdk.rpc.discovery.SystemInfo\"S\n\nSystemInfo\x12\x0c\n\x04uuid\x18\x01 \x01(\x04\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\x18\n\x10is_core_instance\x18\x04 \x01(\x08\x32\xac\x01\n\x10\x44iscoveryService\x12\x97\x01\n\x1aSubscribeDiscoveredSystems\x12>.dronecode_sdk.rpc.discovery.SubscribeDiscoveredSystemsRequest\x1a\x35.dronecode_sdk.rpc.discovery.DiscoveredSystemResponse\"\x00\x30\x01\x42,\n\x1aio.dronecode_sdk.discoveryB\x0e\x44iscoveryProtob\x06proto3')
)




_SUBSCRIBEDISCOVEREDSYSTEMSREQUEST = _descriptor.Descriptor(
  name='SubscribeDiscoveredSystemsRequest',
  full_name='dronecode_sdk.rpc.discovery.SubscribeDiscoveredSystemsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=83,
)


_DISCOVEREDSYSTEMRESPONSE = _descriptor.Descriptor(
  name='DiscoveredSystemResponse',
  full_name='dronecode_sdk.rpc.discovery.DiscoveredSystemResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='system_info', full_name='dronecode_sdk.rpc.discovery.DiscoveredSystemResponse.system_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=173,
)


_SYSTEMINFO = _descriptor.Descriptor(
  name='SystemInfo',
  full_name='dronecode_sdk.rpc.discovery.SystemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='dronecode_sdk.rpc.discovery.SystemInfo.uuid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='dronecode_sdk.rpc.discovery.SystemInfo.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='dronecode_sdk.rpc.discovery.SystemInfo.port', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_core_instance', full_name='dronecode_sdk.rpc.discovery.SystemInfo.is_core_instance', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=258,
)

_DISCOVEREDSYSTEMRESPONSE.fields_by_name['system_info'].message_type = _SYSTEMINFO
DESCRIPTOR.message_types_by_name['SubscribeDiscoveredSystemsRequest'] = _SUBSCRIBEDISCOVEREDSYSTEMSREQUEST
DESCRIPTOR.message_types_by_name['DiscoveredSystemResponse'] = _DISCOVEREDSYSTEMRESPONSE
DESCRIPTOR.message_types_by_name['SystemInfo'] = _SYSTEMINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubscribeDiscoveredSystemsRequest = _reflection.GeneratedProtocolMessageType('SubscribeDiscoveredSystemsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBEDISCOVEREDSYSTEMSREQUEST,
  __module__ = 'discovery_pb2'
  # @@protoc_insertion_point(class_scope:dronecode_sdk.rpc.discovery.SubscribeDiscoveredSystemsRequest)
  ))
_sym_db.RegisterMessage(SubscribeDiscoveredSystemsRequest)

DiscoveredSystemResponse = _reflection.GeneratedProtocolMessageType('DiscoveredSystemResponse', (_message.Message,), dict(
  DESCRIPTOR = _DISCOVEREDSYSTEMRESPONSE,
  __module__ = 'discovery_pb2'
  # @@protoc_insertion_point(class_scope:dronecode_sdk.rpc.discovery.DiscoveredSystemResponse)
  ))
_sym_db.RegisterMessage(DiscoveredSystemResponse)

SystemInfo = _reflection.GeneratedProtocolMessageType('SystemInfo', (_message.Message,), dict(
  DESCRIPTOR = _SYSTEMINFO,
  __module__ = 'discovery_pb2'
  # @@protoc_insertion_point(class_scope:dronecode_sdk.rpc.discovery.SystemInfo)
  ))
_sym_db.RegisterMessage(SystemInfo)


DESCRIPTOR._options = None

_DISCOVERYSERVICE = _descriptor.ServiceDescriptor(
  name='DiscoveryService',
  full_name='dronecode_sdk.rpc.discovery.DiscoveryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=261,
  serialized_end=433,
  methods=[
  _descriptor.MethodDescriptor(
    name='SubscribeDiscoveredSystems',
    full_name='dronecode_sdk.rpc.discovery.DiscoveryService.SubscribeDiscoveredSystems',
    index=0,
    containing_service=None,
    input_type=_SUBSCRIBEDISCOVEREDSYSTEMSREQUEST,
    output_type=_DISCOVEREDSYSTEMRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DISCOVERYSERVICE)

DESCRIPTOR.services_by_name['DiscoveryService'] = _DISCOVERYSERVICE

# @@protoc_insertion_point(module_scope)
