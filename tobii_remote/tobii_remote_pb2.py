# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tobii_remote.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12tobii_remote.proto\x1a\x1bgoogle/protobuf/empty.proto\"/\n\x0fGazePosOnScreen\x12\r\n\x05pos_x\x18\x01 \x01(\x01\x12\r\n\x05pos_y\x18\x02 \x01(\x01\"-\n\x0e\x45yeTrackerInfo\x12\x1b\n\x13\x65yetracker_model_id\x18\x01 \x01(\t2\x8f\x01\n\x0bTobiiRemote\x12@\n\x12GetGazePosOnScreen\x12\x16.google.protobuf.Empty\x1a\x10.GazePosOnScreen\"\x00\x12>\n\x11GetEyeTrackerInfo\x12\x16.google.protobuf.Empty\x1a\x0f.EyeTrackerInfo\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tobii_remote_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GAZEPOSONSCREEN._serialized_start=51
  _GAZEPOSONSCREEN._serialized_end=98
  _EYETRACKERINFO._serialized_start=100
  _EYETRACKERINFO._serialized_end=145
  _TOBIIREMOTE._serialized_start=148
  _TOBIIREMOTE._serialized_end=291
# @@protoc_insertion_point(module_scope)
