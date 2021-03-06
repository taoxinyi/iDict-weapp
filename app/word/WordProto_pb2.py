# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WordProto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WordProto.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0fWordProto.proto\"Q\n\x08WordList\x12\x1f\n\x0bword_briefs\x18\x01 \x03(\x0b\x32\n.WordBrief\x12$\n\x10word_suggestions\x18\x02 \x03(\x0b\x32\n.WordBrief\"\x93\x03\n\tWordBrief\x12\x0f\n\x07word_in\x18\x01 \x01(\t\x12\x10\n\x08word_out\x18\x02 \x01(\t\x12)\n\x07uk_pron\x18\x03 \x01(\x0b\x32\x18.WordBrief.Pronunciation\x12)\n\x07us_pron\x18\x04 \x01(\x0b\x32\x18.WordBrief.Pronunciation\x12.\n\x0f\x63hn_definitions\x18\x05 \x03(\x0b\x32\x15.WordBrief.Definition\x12.\n\x0f\x65ng_definitions\x18\x06 \x03(\x0b\x32\x15.WordBrief.Definition\x12\x0c\n\x04tags\x18\x07 \x03(\x08\x12\x1f\n\x05lemma\x18\x08 \x01(\x0b\x32\x10.WordBrief.Lemma\x1a(\n\rPronunciation\x12\n\n\x02ps\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x1a*\n\nDefinition\x12\x0b\n\x03pos\x18\x01 \x01(\t\x12\x0f\n\x07meaning\x18\x02 \x01(\t\x1a(\n\x05Lemma\x12\r\n\x05lemma\x18\x01 \x01(\t\x12\x10\n\x08relation\x18\x02 \x01(\t\"\xcd\x03\n\nWordDetail\x12\x1e\n\nword_brief\x18\x01 \x01(\x0b\x32\n.WordBrief\x12\x0f\n\x07\x63ollins\x18\x02 \x01(\x05\x12\x0b\n\x03\x62nc\x18\x03 \x01(\x05\x12\x0b\n\x03\x66rq\x18\x04 \x01(\x05\x12\x30\n\x0esentence_lists\x18\x05 \x03(\x0b\x32\x18.WordDetail.SentenceList\x12+\n\x0b\x64\x65rivatives\x18\x06 \x03(\x0b\x32\x16.WordDetail.Derivative\x1a\xe6\x01\n\x0cSentenceList\x12/\n\x06source\x18\x01 \x01(\x0e\x32\x1f.WordDetail.SentenceList.Source\x12\x34\n\tsentences\x18\x02 \x03(\x0b\x32!.WordDetail.SentenceList.Sentence\x1a$\n\x08Sentence\x12\x0b\n\x03\x65ng\x18\x01 \x01(\t\x12\x0b\n\x03\x63hn\x18\x02 \x01(\t\"I\n\x06Source\x12\n\n\x06OXFORD\x10\x00\x12\r\n\tCAMBRIDGE\x10\x01\x12\x0b\n\x07LONGMAN\x10\x02\x12\x0b\n\x07\x43OLLINS\x10\x03\x12\n\n\x06ONLINE\x10\x04\x1a,\n\nDerivative\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x10\n\x08relation\x18\x02 \x01(\tb\x06proto3')
)



_WORDDETAIL_SENTENCELIST_SOURCE = _descriptor.EnumDescriptor(
  name='Source',
  full_name='WordDetail.SentenceList.Source',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OXFORD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMBRIDGE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LONGMAN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLINS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONLINE', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=851,
  serialized_end=924,
)
_sym_db.RegisterEnumDescriptor(_WORDDETAIL_SENTENCELIST_SOURCE)


_WORDLIST = _descriptor.Descriptor(
  name='WordList',
  full_name='WordList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word_briefs', full_name='WordList.word_briefs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='word_suggestions', full_name='WordList.word_suggestions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=19,
  serialized_end=100,
)


_WORDBRIEF_PRONUNCIATION = _descriptor.Descriptor(
  name='Pronunciation',
  full_name='WordBrief.Pronunciation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ps', full_name='WordBrief.Pronunciation.ps', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='WordBrief.Pronunciation.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=380,
  serialized_end=420,
)

_WORDBRIEF_DEFINITION = _descriptor.Descriptor(
  name='Definition',
  full_name='WordBrief.Definition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos', full_name='WordBrief.Definition.pos', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meaning', full_name='WordBrief.Definition.meaning', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=422,
  serialized_end=464,
)

_WORDBRIEF_LEMMA = _descriptor.Descriptor(
  name='Lemma',
  full_name='WordBrief.Lemma',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lemma', full_name='WordBrief.Lemma.lemma', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation', full_name='WordBrief.Lemma.relation', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=466,
  serialized_end=506,
)

_WORDBRIEF = _descriptor.Descriptor(
  name='WordBrief',
  full_name='WordBrief',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word_in', full_name='WordBrief.word_in', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='word_out', full_name='WordBrief.word_out', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uk_pron', full_name='WordBrief.uk_pron', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='us_pron', full_name='WordBrief.us_pron', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chn_definitions', full_name='WordBrief.chn_definitions', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eng_definitions', full_name='WordBrief.eng_definitions', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='WordBrief.tags', index=6,
      number=7, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lemma', full_name='WordBrief.lemma', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WORDBRIEF_PRONUNCIATION, _WORDBRIEF_DEFINITION, _WORDBRIEF_LEMMA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=506,
)


_WORDDETAIL_SENTENCELIST_SENTENCE = _descriptor.Descriptor(
  name='Sentence',
  full_name='WordDetail.SentenceList.Sentence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='eng', full_name='WordDetail.SentenceList.Sentence.eng', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chn', full_name='WordDetail.SentenceList.Sentence.chn', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=813,
  serialized_end=849,
)

_WORDDETAIL_SENTENCELIST = _descriptor.Descriptor(
  name='SentenceList',
  full_name='WordDetail.SentenceList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='WordDetail.SentenceList.source', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sentences', full_name='WordDetail.SentenceList.sentences', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WORDDETAIL_SENTENCELIST_SENTENCE, ],
  enum_types=[
    _WORDDETAIL_SENTENCELIST_SOURCE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=694,
  serialized_end=924,
)

_WORDDETAIL_DERIVATIVE = _descriptor.Descriptor(
  name='Derivative',
  full_name='WordDetail.Derivative',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='WordDetail.Derivative.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation', full_name='WordDetail.Derivative.relation', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=926,
  serialized_end=970,
)

_WORDDETAIL = _descriptor.Descriptor(
  name='WordDetail',
  full_name='WordDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word_brief', full_name='WordDetail.word_brief', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collins', full_name='WordDetail.collins', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bnc', full_name='WordDetail.bnc', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frq', full_name='WordDetail.frq', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sentence_lists', full_name='WordDetail.sentence_lists', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='derivatives', full_name='WordDetail.derivatives', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WORDDETAIL_SENTENCELIST, _WORDDETAIL_DERIVATIVE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=509,
  serialized_end=970,
)

_WORDLIST.fields_by_name['word_briefs'].message_type = _WORDBRIEF
_WORDLIST.fields_by_name['word_suggestions'].message_type = _WORDBRIEF
_WORDBRIEF_PRONUNCIATION.containing_type = _WORDBRIEF
_WORDBRIEF_DEFINITION.containing_type = _WORDBRIEF
_WORDBRIEF_LEMMA.containing_type = _WORDBRIEF
_WORDBRIEF.fields_by_name['uk_pron'].message_type = _WORDBRIEF_PRONUNCIATION
_WORDBRIEF.fields_by_name['us_pron'].message_type = _WORDBRIEF_PRONUNCIATION
_WORDBRIEF.fields_by_name['chn_definitions'].message_type = _WORDBRIEF_DEFINITION
_WORDBRIEF.fields_by_name['eng_definitions'].message_type = _WORDBRIEF_DEFINITION
_WORDBRIEF.fields_by_name['lemma'].message_type = _WORDBRIEF_LEMMA
_WORDDETAIL_SENTENCELIST_SENTENCE.containing_type = _WORDDETAIL_SENTENCELIST
_WORDDETAIL_SENTENCELIST.fields_by_name['source'].enum_type = _WORDDETAIL_SENTENCELIST_SOURCE
_WORDDETAIL_SENTENCELIST.fields_by_name['sentences'].message_type = _WORDDETAIL_SENTENCELIST_SENTENCE
_WORDDETAIL_SENTENCELIST.containing_type = _WORDDETAIL
_WORDDETAIL_SENTENCELIST_SOURCE.containing_type = _WORDDETAIL_SENTENCELIST
_WORDDETAIL_DERIVATIVE.containing_type = _WORDDETAIL
_WORDDETAIL.fields_by_name['word_brief'].message_type = _WORDBRIEF
_WORDDETAIL.fields_by_name['sentence_lists'].message_type = _WORDDETAIL_SENTENCELIST
_WORDDETAIL.fields_by_name['derivatives'].message_type = _WORDDETAIL_DERIVATIVE
DESCRIPTOR.message_types_by_name['WordList'] = _WORDLIST
DESCRIPTOR.message_types_by_name['WordBrief'] = _WORDBRIEF
DESCRIPTOR.message_types_by_name['WordDetail'] = _WORDDETAIL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WordList = _reflection.GeneratedProtocolMessageType('WordList', (_message.Message,), dict(
  DESCRIPTOR = _WORDLIST,
  __module__ = 'WordProto_pb2'
  # @@protoc_insertion_point(class_scope:WordList)
  ))
_sym_db.RegisterMessage(WordList)

WordBrief = _reflection.GeneratedProtocolMessageType('WordBrief', (_message.Message,), dict(

  Pronunciation = _reflection.GeneratedProtocolMessageType('Pronunciation', (_message.Message,), dict(
    DESCRIPTOR = _WORDBRIEF_PRONUNCIATION,
    __module__ = 'WordProto_pb2'
    # @@protoc_insertion_point(class_scope:WordBrief.Pronunciation)
    ))
  ,

  Definition = _reflection.GeneratedProtocolMessageType('Definition', (_message.Message,), dict(
    DESCRIPTOR = _WORDBRIEF_DEFINITION,
    __module__ = 'WordProto_pb2'
    # @@protoc_insertion_point(class_scope:WordBrief.Definition)
    ))
  ,

  Lemma = _reflection.GeneratedProtocolMessageType('Lemma', (_message.Message,), dict(
    DESCRIPTOR = _WORDBRIEF_LEMMA,
    __module__ = 'WordProto_pb2'
    # @@protoc_insertion_point(class_scope:WordBrief.Lemma)
    ))
  ,
  DESCRIPTOR = _WORDBRIEF,
  __module__ = 'WordProto_pb2'
  # @@protoc_insertion_point(class_scope:WordBrief)
  ))
_sym_db.RegisterMessage(WordBrief)
_sym_db.RegisterMessage(WordBrief.Pronunciation)
_sym_db.RegisterMessage(WordBrief.Definition)
_sym_db.RegisterMessage(WordBrief.Lemma)

WordDetail = _reflection.GeneratedProtocolMessageType('WordDetail', (_message.Message,), dict(

  SentenceList = _reflection.GeneratedProtocolMessageType('SentenceList', (_message.Message,), dict(

    Sentence = _reflection.GeneratedProtocolMessageType('Sentence', (_message.Message,), dict(
      DESCRIPTOR = _WORDDETAIL_SENTENCELIST_SENTENCE,
      __module__ = 'WordProto_pb2'
      # @@protoc_insertion_point(class_scope:WordDetail.SentenceList.Sentence)
      ))
    ,
    DESCRIPTOR = _WORDDETAIL_SENTENCELIST,
    __module__ = 'WordProto_pb2'
    # @@protoc_insertion_point(class_scope:WordDetail.SentenceList)
    ))
  ,

  Derivative = _reflection.GeneratedProtocolMessageType('Derivative', (_message.Message,), dict(
    DESCRIPTOR = _WORDDETAIL_DERIVATIVE,
    __module__ = 'WordProto_pb2'
    # @@protoc_insertion_point(class_scope:WordDetail.Derivative)
    ))
  ,
  DESCRIPTOR = _WORDDETAIL,
  __module__ = 'WordProto_pb2'
  # @@protoc_insertion_point(class_scope:WordDetail)
  ))
_sym_db.RegisterMessage(WordDetail)
_sym_db.RegisterMessage(WordDetail.SentenceList)
_sym_db.RegisterMessage(WordDetail.SentenceList.Sentence)
_sym_db.RegisterMessage(WordDetail.Derivative)


# @@protoc_insertion_point(module_scope)
