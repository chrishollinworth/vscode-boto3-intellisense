"""
Type annotations for clouddirectory service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_clouddirectory.type_defs import ObjectReferenceTypeDef

    data: ObjectReferenceTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    BatchReadExceptionTypeType,
    ConsistencyLevelType,
    DirectoryStateType,
    FacetAttributeTypeType,
    FacetStyleType,
    ObjectTypeType,
    RangeModeType,
    RequiredAttributeBehaviorType,
    RuleTypeType,
    UpdateActionTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AddFacetToObjectRequestTypeDef",
    "ApplySchemaRequestTypeDef",
    "ApplySchemaResponseTypeDef",
    "AttachObjectRequestTypeDef",
    "AttachObjectResponseTypeDef",
    "AttachPolicyRequestTypeDef",
    "AttachToIndexRequestTypeDef",
    "AttachToIndexResponseTypeDef",
    "AttachTypedLinkRequestTypeDef",
    "AttachTypedLinkResponseTypeDef",
    "AttributeKeyAndValueOutputTypeDef",
    "AttributeKeyAndValueTypeDef",
    "AttributeKeyAndValueUnionTypeDef",
    "AttributeKeyTypeDef",
    "AttributeNameAndValueOutputTypeDef",
    "AttributeNameAndValueTypeDef",
    "AttributeNameAndValueUnionTypeDef",
    "BatchAddFacetToObjectTypeDef",
    "BatchAttachObjectResponseTypeDef",
    "BatchAttachObjectTypeDef",
    "BatchAttachPolicyTypeDef",
    "BatchAttachToIndexResponseTypeDef",
    "BatchAttachToIndexTypeDef",
    "BatchAttachTypedLinkResponseTypeDef",
    "BatchAttachTypedLinkTypeDef",
    "BatchCreateIndexResponseTypeDef",
    "BatchCreateIndexTypeDef",
    "BatchCreateObjectResponseTypeDef",
    "BatchCreateObjectTypeDef",
    "BatchDeleteObjectTypeDef",
    "BatchDetachFromIndexResponseTypeDef",
    "BatchDetachFromIndexTypeDef",
    "BatchDetachObjectResponseTypeDef",
    "BatchDetachObjectTypeDef",
    "BatchDetachPolicyTypeDef",
    "BatchDetachTypedLinkTypeDef",
    "BatchGetLinkAttributesResponseTypeDef",
    "BatchGetLinkAttributesTypeDef",
    "BatchGetObjectAttributesResponseTypeDef",
    "BatchGetObjectAttributesTypeDef",
    "BatchGetObjectInformationResponseTypeDef",
    "BatchGetObjectInformationTypeDef",
    "BatchListAttachedIndicesResponseTypeDef",
    "BatchListAttachedIndicesTypeDef",
    "BatchListIncomingTypedLinksResponseTypeDef",
    "BatchListIncomingTypedLinksTypeDef",
    "BatchListIndexResponseTypeDef",
    "BatchListIndexTypeDef",
    "BatchListObjectAttributesResponseTypeDef",
    "BatchListObjectAttributesTypeDef",
    "BatchListObjectChildrenResponseTypeDef",
    "BatchListObjectChildrenTypeDef",
    "BatchListObjectParentPathsResponseTypeDef",
    "BatchListObjectParentPathsTypeDef",
    "BatchListObjectParentsResponseTypeDef",
    "BatchListObjectParentsTypeDef",
    "BatchListObjectPoliciesResponseTypeDef",
    "BatchListObjectPoliciesTypeDef",
    "BatchListOutgoingTypedLinksResponseTypeDef",
    "BatchListOutgoingTypedLinksTypeDef",
    "BatchListPolicyAttachmentsResponseTypeDef",
    "BatchListPolicyAttachmentsTypeDef",
    "BatchLookupPolicyResponseTypeDef",
    "BatchLookupPolicyTypeDef",
    "BatchReadExceptionTypeDef",
    "BatchReadOperationResponseTypeDef",
    "BatchReadOperationTypeDef",
    "BatchReadRequestTypeDef",
    "BatchReadResponseTypeDef",
    "BatchReadSuccessfulResponseTypeDef",
    "BatchRemoveFacetFromObjectTypeDef",
    "BatchUpdateLinkAttributesTypeDef",
    "BatchUpdateObjectAttributesResponseTypeDef",
    "BatchUpdateObjectAttributesTypeDef",
    "BatchWriteOperationResponseTypeDef",
    "BatchWriteOperationTypeDef",
    "BatchWriteRequestTypeDef",
    "BatchWriteResponseTypeDef",
    "BlobTypeDef",
    "CreateDirectoryRequestTypeDef",
    "CreateDirectoryResponseTypeDef",
    "CreateFacetRequestTypeDef",
    "CreateIndexRequestTypeDef",
    "CreateIndexResponseTypeDef",
    "CreateObjectRequestTypeDef",
    "CreateObjectResponseTypeDef",
    "CreateSchemaRequestTypeDef",
    "CreateSchemaResponseTypeDef",
    "CreateTypedLinkFacetRequestTypeDef",
    "DeleteDirectoryRequestTypeDef",
    "DeleteDirectoryResponseTypeDef",
    "DeleteFacetRequestTypeDef",
    "DeleteObjectRequestTypeDef",
    "DeleteSchemaRequestTypeDef",
    "DeleteSchemaResponseTypeDef",
    "DeleteTypedLinkFacetRequestTypeDef",
    "DetachFromIndexRequestTypeDef",
    "DetachFromIndexResponseTypeDef",
    "DetachObjectRequestTypeDef",
    "DetachObjectResponseTypeDef",
    "DetachPolicyRequestTypeDef",
    "DetachTypedLinkRequestTypeDef",
    "DirectoryTypeDef",
    "DisableDirectoryRequestTypeDef",
    "DisableDirectoryResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableDirectoryRequestTypeDef",
    "EnableDirectoryResponseTypeDef",
    "FacetAttributeDefinitionOutputTypeDef",
    "FacetAttributeDefinitionTypeDef",
    "FacetAttributeDefinitionUnionTypeDef",
    "FacetAttributeOutputTypeDef",
    "FacetAttributeReferenceTypeDef",
    "FacetAttributeTypeDef",
    "FacetAttributeUnionTypeDef",
    "FacetAttributeUpdateTypeDef",
    "FacetTypeDef",
    "GetAppliedSchemaVersionRequestTypeDef",
    "GetAppliedSchemaVersionResponseTypeDef",
    "GetDirectoryRequestTypeDef",
    "GetDirectoryResponseTypeDef",
    "GetFacetRequestTypeDef",
    "GetFacetResponseTypeDef",
    "GetLinkAttributesRequestTypeDef",
    "GetLinkAttributesResponseTypeDef",
    "GetObjectAttributesRequestTypeDef",
    "GetObjectAttributesResponseTypeDef",
    "GetObjectInformationRequestTypeDef",
    "GetObjectInformationResponseTypeDef",
    "GetSchemaAsJsonRequestTypeDef",
    "GetSchemaAsJsonResponseTypeDef",
    "GetTypedLinkFacetInformationRequestTypeDef",
    "GetTypedLinkFacetInformationResponseTypeDef",
    "IndexAttachmentTypeDef",
    "LinkAttributeActionTypeDef",
    "LinkAttributeUpdateTypeDef",
    "ListAppliedSchemaArnsRequestPaginateTypeDef",
    "ListAppliedSchemaArnsRequestTypeDef",
    "ListAppliedSchemaArnsResponseTypeDef",
    "ListAttachedIndicesRequestPaginateTypeDef",
    "ListAttachedIndicesRequestTypeDef",
    "ListAttachedIndicesResponseTypeDef",
    "ListDevelopmentSchemaArnsRequestPaginateTypeDef",
    "ListDevelopmentSchemaArnsRequestTypeDef",
    "ListDevelopmentSchemaArnsResponseTypeDef",
    "ListDirectoriesRequestPaginateTypeDef",
    "ListDirectoriesRequestTypeDef",
    "ListDirectoriesResponseTypeDef",
    "ListFacetAttributesRequestPaginateTypeDef",
    "ListFacetAttributesRequestTypeDef",
    "ListFacetAttributesResponseTypeDef",
    "ListFacetNamesRequestPaginateTypeDef",
    "ListFacetNamesRequestTypeDef",
    "ListFacetNamesResponseTypeDef",
    "ListIncomingTypedLinksRequestPaginateTypeDef",
    "ListIncomingTypedLinksRequestTypeDef",
    "ListIncomingTypedLinksResponseTypeDef",
    "ListIndexRequestPaginateTypeDef",
    "ListIndexRequestTypeDef",
    "ListIndexResponseTypeDef",
    "ListManagedSchemaArnsRequestPaginateTypeDef",
    "ListManagedSchemaArnsRequestTypeDef",
    "ListManagedSchemaArnsResponseTypeDef",
    "ListObjectAttributesRequestPaginateTypeDef",
    "ListObjectAttributesRequestTypeDef",
    "ListObjectAttributesResponseTypeDef",
    "ListObjectChildrenRequestTypeDef",
    "ListObjectChildrenResponseTypeDef",
    "ListObjectParentPathsRequestPaginateTypeDef",
    "ListObjectParentPathsRequestTypeDef",
    "ListObjectParentPathsResponseTypeDef",
    "ListObjectParentsRequestTypeDef",
    "ListObjectParentsResponseTypeDef",
    "ListObjectPoliciesRequestPaginateTypeDef",
    "ListObjectPoliciesRequestTypeDef",
    "ListObjectPoliciesResponseTypeDef",
    "ListOutgoingTypedLinksRequestPaginateTypeDef",
    "ListOutgoingTypedLinksRequestTypeDef",
    "ListOutgoingTypedLinksResponseTypeDef",
    "ListPolicyAttachmentsRequestPaginateTypeDef",
    "ListPolicyAttachmentsRequestTypeDef",
    "ListPolicyAttachmentsResponseTypeDef",
    "ListPublishedSchemaArnsRequestPaginateTypeDef",
    "ListPublishedSchemaArnsRequestTypeDef",
    "ListPublishedSchemaArnsResponseTypeDef",
    "ListTagsForResourceRequestPaginateTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTypedLinkFacetAttributesRequestPaginateTypeDef",
    "ListTypedLinkFacetAttributesRequestTypeDef",
    "ListTypedLinkFacetAttributesResponseTypeDef",
    "ListTypedLinkFacetNamesRequestPaginateTypeDef",
    "ListTypedLinkFacetNamesRequestTypeDef",
    "ListTypedLinkFacetNamesResponseTypeDef",
    "LookupPolicyRequestPaginateTypeDef",
    "LookupPolicyRequestTypeDef",
    "LookupPolicyResponseTypeDef",
    "ObjectAttributeActionTypeDef",
    "ObjectAttributeRangeTypeDef",
    "ObjectAttributeUpdateTypeDef",
    "ObjectIdentifierAndLinkNameTupleTypeDef",
    "ObjectReferenceTypeDef",
    "PaginatorConfigTypeDef",
    "PathToObjectIdentifiersTypeDef",
    "PolicyAttachmentTypeDef",
    "PolicyToPathTypeDef",
    "PublishSchemaRequestTypeDef",
    "PublishSchemaResponseTypeDef",
    "PutSchemaFromJsonRequestTypeDef",
    "PutSchemaFromJsonResponseTypeDef",
    "RemoveFacetFromObjectRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RuleOutputTypeDef",
    "RuleTypeDef",
    "RuleUnionTypeDef",
    "SchemaFacetTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "TypedAttributeValueOutputTypeDef",
    "TypedAttributeValueRangeTypeDef",
    "TypedAttributeValueTypeDef",
    "TypedAttributeValueUnionTypeDef",
    "TypedLinkAttributeDefinitionOutputTypeDef",
    "TypedLinkAttributeDefinitionTypeDef",
    "TypedLinkAttributeDefinitionUnionTypeDef",
    "TypedLinkAttributeRangeTypeDef",
    "TypedLinkFacetAttributeUpdateTypeDef",
    "TypedLinkFacetTypeDef",
    "TypedLinkSchemaAndFacetNameTypeDef",
    "TypedLinkSpecifierOutputTypeDef",
    "TypedLinkSpecifierTypeDef",
    "TypedLinkSpecifierUnionTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateFacetRequestTypeDef",
    "UpdateLinkAttributesRequestTypeDef",
    "UpdateObjectAttributesRequestTypeDef",
    "UpdateObjectAttributesResponseTypeDef",
    "UpdateSchemaRequestTypeDef",
    "UpdateSchemaResponseTypeDef",
    "UpdateTypedLinkFacetRequestTypeDef",
    "UpgradeAppliedSchemaRequestTypeDef",
    "UpgradeAppliedSchemaResponseTypeDef",
    "UpgradePublishedSchemaRequestTypeDef",
    "UpgradePublishedSchemaResponseTypeDef",
)

class ObjectReferenceTypeDef(TypedDict):
    Selector: NotRequired[str]

class SchemaFacetTypeDef(TypedDict):
    SchemaArn: NotRequired[str]
    FacetName: NotRequired[str]

class ApplySchemaRequestTypeDef(TypedDict):
    PublishedSchemaArn: str
    DirectoryArn: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class TypedLinkSchemaAndFacetNameTypeDef(TypedDict):
    SchemaArn: str
    TypedLinkName: str

class AttributeKeyTypeDef(TypedDict):
    SchemaArn: str
    FacetName: str
    Name: str

class TypedAttributeValueOutputTypeDef(TypedDict):
    StringValue: NotRequired[str]
    BinaryValue: NotRequired[bytes]
    BooleanValue: NotRequired[bool]
    NumberValue: NotRequired[str]
    DatetimeValue: NotRequired[datetime]

class BatchAttachObjectResponseTypeDef(TypedDict):
    attachedObjectIdentifier: NotRequired[str]

class BatchAttachToIndexResponseTypeDef(TypedDict):
    AttachedObjectIdentifier: NotRequired[str]

class BatchCreateIndexResponseTypeDef(TypedDict):
    ObjectIdentifier: NotRequired[str]

class BatchCreateObjectResponseTypeDef(TypedDict):
    ObjectIdentifier: NotRequired[str]

class BatchDetachFromIndexResponseTypeDef(TypedDict):
    DetachedObjectIdentifier: NotRequired[str]

class BatchDetachObjectResponseTypeDef(TypedDict):
    detachedObjectIdentifier: NotRequired[str]

class BatchListObjectChildrenResponseTypeDef(TypedDict):
    Children: NotRequired[Dict[str, str]]
    NextToken: NotRequired[str]

class PathToObjectIdentifiersTypeDef(TypedDict):
    Path: NotRequired[str]
    ObjectIdentifiers: NotRequired[List[str]]

class ObjectIdentifierAndLinkNameTupleTypeDef(TypedDict):
    ObjectIdentifier: NotRequired[str]
    LinkName: NotRequired[str]

class BatchListObjectPoliciesResponseTypeDef(TypedDict):
    AttachedPolicyIds: NotRequired[List[str]]
    NextToken: NotRequired[str]

class BatchListPolicyAttachmentsResponseTypeDef(TypedDict):
    ObjectIdentifiers: NotRequired[List[str]]
    NextToken: NotRequired[str]

BatchReadExceptionTypeDef = TypedDict(
    "BatchReadExceptionTypeDef",
    {
        "Type": NotRequired[BatchReadExceptionTypeType],
        "Message": NotRequired[str],
    },
)

class BatchUpdateObjectAttributesResponseTypeDef(TypedDict):
    ObjectIdentifier: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CreateDirectoryRequestTypeDef(TypedDict):
    Name: str
    SchemaArn: str

class CreateSchemaRequestTypeDef(TypedDict):
    Name: str

class DeleteDirectoryRequestTypeDef(TypedDict):
    DirectoryArn: str

class DeleteFacetRequestTypeDef(TypedDict):
    SchemaArn: str
    Name: str

class DeleteSchemaRequestTypeDef(TypedDict):
    SchemaArn: str

class DeleteTypedLinkFacetRequestTypeDef(TypedDict):
    SchemaArn: str
    Name: str

class DirectoryTypeDef(TypedDict):
    Name: NotRequired[str]
    DirectoryArn: NotRequired[str]
    State: NotRequired[DirectoryStateType]
    CreationDateTime: NotRequired[datetime]

class DisableDirectoryRequestTypeDef(TypedDict):
    DirectoryArn: str

class EnableDirectoryRequestTypeDef(TypedDict):
    DirectoryArn: str

RuleOutputTypeDef = TypedDict(
    "RuleOutputTypeDef",
    {
        "Type": NotRequired[RuleTypeType],
        "Parameters": NotRequired[Dict[str, str]],
    },
)

class FacetAttributeReferenceTypeDef(TypedDict):
    TargetFacetName: str
    TargetAttributeName: str

class FacetTypeDef(TypedDict):
    Name: NotRequired[str]
    ObjectType: NotRequired[ObjectTypeType]
    FacetStyle: NotRequired[FacetStyleType]

class GetAppliedSchemaVersionRequestTypeDef(TypedDict):
    SchemaArn: str

class GetDirectoryRequestTypeDef(TypedDict):
    DirectoryArn: str

class GetFacetRequestTypeDef(TypedDict):
    SchemaArn: str
    Name: str

class GetSchemaAsJsonRequestTypeDef(TypedDict):
    SchemaArn: str

class GetTypedLinkFacetInformationRequestTypeDef(TypedDict):
    SchemaArn: str
    Name: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAppliedSchemaArnsRequestTypeDef(TypedDict):
    DirectoryArn: str
    SchemaArn: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDevelopmentSchemaArnsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDirectoriesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    state: NotRequired[DirectoryStateType]

class ListFacetAttributesRequestTypeDef(TypedDict):
    SchemaArn: str
    Name: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListFacetNamesRequestTypeDef(TypedDict):
    SchemaArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListManagedSchemaArnsRequestTypeDef(TypedDict):
    SchemaArn: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListPublishedSchemaArnsRequestTypeDef(TypedDict):
    SchemaArn: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class ListTypedLinkFacetAttributesRequestTypeDef(TypedDict):
    SchemaArn: str
    Name: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTypedLinkFacetNamesRequestTypeDef(TypedDict):
    SchemaArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class PolicyAttachmentTypeDef(TypedDict):
    PolicyId: NotRequired[str]
    ObjectIdentifier: NotRequired[str]
    PolicyType: NotRequired[str]

class PublishSchemaRequestTypeDef(TypedDict):
    DevelopmentSchemaArn: str
    Version: str
    MinorVersion: NotRequired[str]
    Name: NotRequired[str]

class PutSchemaFromJsonRequestTypeDef(TypedDict):
    SchemaArn: str
    Document: str

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Type": NotRequired[RuleTypeType],
        "Parameters": NotRequired[Mapping[str, str]],
    },
)
TimestampTypeDef = Union[datetime, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateSchemaRequestTypeDef(TypedDict):
    SchemaArn: str
    Name: str

class UpgradeAppliedSchemaRequestTypeDef(TypedDict):
    PublishedSchemaArn: str
    DirectoryArn: str
    DryRun: NotRequired[bool]

class UpgradePublishedSchemaRequestTypeDef(TypedDict):
    DevelopmentSchemaArn: str
    PublishedSchemaArn: str
    MinorVersion: str
    DryRun: NotRequired[bool]

class AttachObjectRequestTypeDef(TypedDict):
    DirectoryArn: str
    ParentReference: ObjectReferenceTypeDef
    ChildReference: ObjectReferenceTypeDef
    LinkName: str

class AttachPolicyRequestTypeDef(TypedDict):
    DirectoryArn: str
    PolicyReference: ObjectReferenceTypeDef
    ObjectReference: ObjectReferenceTypeDef

class AttachToIndexRequestTypeDef(TypedDict):
    DirectoryArn: str
    IndexReference: ObjectReferenceTypeDef
    TargetReference: ObjectReferenceTypeDef

class BatchAttachObjectTypeDef(TypedDict):
    ParentReference: ObjectReferenceTypeDef
    ChildReference: ObjectReferenceTypeDef
    LinkName: str

class BatchAttachPolicyTypeDef(TypedDict):
    PolicyReference: ObjectReferenceTypeDef
    ObjectReference: ObjectReferenceTypeDef

class BatchAttachToIndexTypeDef(TypedDict):
    IndexReference: ObjectReferenceTypeDef
    TargetReference: ObjectReferenceTypeDef

class BatchDeleteObjectTypeDef(TypedDict):
    ObjectReference: ObjectReferenceTypeDef

class BatchDetachFromIndexTypeDef(TypedDict):
    IndexReference: ObjectReferenceTypeDef
    TargetReference: ObjectReferenceTypeDef

class BatchDetachObjectTypeDef(TypedDict):
    ParentReference: ObjectReferenceTypeDef
    LinkName: str
    BatchReferenceName: NotRequired[str]

class BatchDetachPolicyTypeDef(TypedDict):
    PolicyReference: ObjectReferenceTypeDef
    ObjectReference: ObjectReferenceTypeDef

class BatchGetObjectInformationTypeDef(TypedDict):
    ObjectReference: ObjectReferenceTypeDef

class BatchListAttachedIndicesTypeDef(TypedDict):
    TargetReference: ObjectReferenceTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class BatchListObjectChildrenTypeDef(TypedDict):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class BatchListObjectParentPathsTypeDef(TypedDict):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class BatchListObjectParentsTypeDef(TypedDict):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class BatchListObjectPoliciesTypeDef(TypedDict):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class BatchListPolicyAttachmentsTypeDef(TypedDict):
    PolicyReference: ObjectReferenceTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class BatchLookupPolicyTypeDef(TypedDict):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DeleteObjectRequestTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef

class DetachFromIndexRequestTypeDef(TypedDict):
    DirectoryArn: str
    IndexReference: ObjectReferenceTypeDef
    TargetReference: ObjectReferenceTypeDef

class DetachObjectRequestTypeDef(TypedDict):
    DirectoryArn: str
    ParentReference: ObjectReferenceTypeDef
    LinkName: str

class DetachPolicyRequestTypeDef(TypedDict):
    DirectoryArn: str
    PolicyReference: ObjectReferenceTypeDef
    ObjectReference: ObjectReferenceTypeDef

class GetObjectInformationRequestTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    ConsistencyLevel: NotRequired[ConsistencyLevelType]

class ListAttachedIndicesRequestTypeDef(TypedDict):
    DirectoryArn: str
    TargetReference: ObjectReferenceTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ConsistencyLevel: NotRequired[ConsistencyLevelType]

class ListObjectChildrenRequestTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ConsistencyLevel: NotRequired[ConsistencyLevelType]

class ListObjectParentPathsRequestTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListObjectParentsRequestTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ConsistencyLevel: NotRequired[ConsistencyLevelType]
    IncludeAllLinksToEachParent: NotRequired[bool]

class ListObjectPoliciesRequestTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ConsistencyLevel: NotRequired[ConsistencyLevelType]

class ListPolicyAttachmentsRequestTypeDef(TypedDict):
    DirectoryArn: str
    PolicyReference: ObjectReferenceTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ConsistencyLevel: NotRequired[ConsistencyLevelType]

class LookupPolicyRequestTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class BatchGetObjectAttributesTypeDef(TypedDict):
    ObjectReference: ObjectReferenceTypeDef
    SchemaFacet: SchemaFacetTypeDef
    AttributeNames: Sequence[str]

class BatchGetObjectInformationResponseTypeDef(TypedDict):
    SchemaFacets: NotRequired[List[SchemaFacetTypeDef]]
    ObjectIdentifier: NotRequired[str]

class BatchListObjectAttributesTypeDef(TypedDict):
    ObjectReference: ObjectReferenceTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    FacetFilter: NotRequired[SchemaFacetTypeDef]

class BatchRemoveFacetFromObjectTypeDef(TypedDict):
    SchemaFacet: SchemaFacetTypeDef
    ObjectReference: ObjectReferenceTypeDef

class GetObjectAttributesRequestTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    SchemaFacet: SchemaFacetTypeDef
    AttributeNames: Sequence[str]
    ConsistencyLevel: NotRequired[ConsistencyLevelType]

class ListObjectAttributesRequestTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ConsistencyLevel: NotRequired[ConsistencyLevelType]
    FacetFilter: NotRequired[SchemaFacetTypeDef]

class RemoveFacetFromObjectRequestTypeDef(TypedDict):
    DirectoryArn: str
    SchemaFacet: SchemaFacetTypeDef
    ObjectReference: ObjectReferenceTypeDef

class ApplySchemaResponseTypeDef(TypedDict):
    AppliedSchemaArn: str
    DirectoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttachObjectResponseTypeDef(TypedDict):
    AttachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttachToIndexResponseTypeDef(TypedDict):
    AttachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDirectoryResponseTypeDef(TypedDict):
    DirectoryArn: str
    Name: str
    ObjectIdentifier: str
    AppliedSchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIndexResponseTypeDef(TypedDict):
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateObjectResponseTypeDef(TypedDict):
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSchemaResponseTypeDef(TypedDict):
    SchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDirectoryResponseTypeDef(TypedDict):
    DirectoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSchemaResponseTypeDef(TypedDict):
    SchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetachFromIndexResponseTypeDef(TypedDict):
    DetachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetachObjectResponseTypeDef(TypedDict):
    DetachedObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableDirectoryResponseTypeDef(TypedDict):
    DirectoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class EnableDirectoryResponseTypeDef(TypedDict):
    DirectoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppliedSchemaVersionResponseTypeDef(TypedDict):
    AppliedSchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetObjectInformationResponseTypeDef(TypedDict):
    SchemaFacets: List[SchemaFacetTypeDef]
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaAsJsonResponseTypeDef(TypedDict):
    Name: str
    Document: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTypedLinkFacetInformationResponseTypeDef(TypedDict):
    IdentityAttributeOrder: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppliedSchemaArnsResponseTypeDef(TypedDict):
    SchemaArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDevelopmentSchemaArnsResponseTypeDef(TypedDict):
    SchemaArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListFacetNamesResponseTypeDef(TypedDict):
    FacetNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListManagedSchemaArnsResponseTypeDef(TypedDict):
    SchemaArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListObjectChildrenResponseTypeDef(TypedDict):
    Children: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListObjectPoliciesResponseTypeDef(TypedDict):
    AttachedPolicyIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPolicyAttachmentsResponseTypeDef(TypedDict):
    ObjectIdentifiers: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPublishedSchemaArnsResponseTypeDef(TypedDict):
    SchemaArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTypedLinkFacetNamesResponseTypeDef(TypedDict):
    FacetNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PublishSchemaResponseTypeDef(TypedDict):
    PublishedSchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutSchemaFromJsonResponseTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateObjectAttributesResponseTypeDef(TypedDict):
    ObjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSchemaResponseTypeDef(TypedDict):
    SchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpgradeAppliedSchemaResponseTypeDef(TypedDict):
    UpgradedSchemaArn: str
    DirectoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpgradePublishedSchemaResponseTypeDef(TypedDict):
    UpgradedSchemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateIndexTypeDef(TypedDict):
    OrderedIndexedAttributeList: Sequence[AttributeKeyTypeDef]
    IsUnique: bool
    ParentReference: NotRequired[ObjectReferenceTypeDef]
    LinkName: NotRequired[str]
    BatchReferenceName: NotRequired[str]

class CreateIndexRequestTypeDef(TypedDict):
    DirectoryArn: str
    OrderedIndexedAttributeList: Sequence[AttributeKeyTypeDef]
    IsUnique: bool
    ParentReference: NotRequired[ObjectReferenceTypeDef]
    LinkName: NotRequired[str]

class AttributeKeyAndValueOutputTypeDef(TypedDict):
    Key: AttributeKeyTypeDef
    Value: TypedAttributeValueOutputTypeDef

class AttributeNameAndValueOutputTypeDef(TypedDict):
    AttributeName: str
    Value: TypedAttributeValueOutputTypeDef

class BatchListObjectParentPathsResponseTypeDef(TypedDict):
    PathToObjectIdentifiersList: NotRequired[List[PathToObjectIdentifiersTypeDef]]
    NextToken: NotRequired[str]

class ListObjectParentPathsResponseTypeDef(TypedDict):
    PathToObjectIdentifiersList: List[PathToObjectIdentifiersTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchListObjectParentsResponseTypeDef(TypedDict):
    ParentLinks: NotRequired[List[ObjectIdentifierAndLinkNameTupleTypeDef]]
    NextToken: NotRequired[str]

class ListObjectParentsResponseTypeDef(TypedDict):
    Parents: Dict[str, str]
    ParentLinks: List[ObjectIdentifierAndLinkNameTupleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetDirectoryResponseTypeDef(TypedDict):
    Directory: DirectoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDirectoriesResponseTypeDef(TypedDict):
    Directories: List[DirectoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

FacetAttributeDefinitionOutputTypeDef = TypedDict(
    "FacetAttributeDefinitionOutputTypeDef",
    {
        "Type": FacetAttributeTypeType,
        "DefaultValue": NotRequired[TypedAttributeValueOutputTypeDef],
        "IsImmutable": NotRequired[bool],
        "Rules": NotRequired[Dict[str, RuleOutputTypeDef]],
    },
)
TypedLinkAttributeDefinitionOutputTypeDef = TypedDict(
    "TypedLinkAttributeDefinitionOutputTypeDef",
    {
        "Name": str,
        "Type": FacetAttributeTypeType,
        "RequiredBehavior": RequiredAttributeBehaviorType,
        "DefaultValue": NotRequired[TypedAttributeValueOutputTypeDef],
        "IsImmutable": NotRequired[bool],
        "Rules": NotRequired[Dict[str, RuleOutputTypeDef]],
    },
)

class GetFacetResponseTypeDef(TypedDict):
    Facet: FacetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppliedSchemaArnsRequestPaginateTypeDef(TypedDict):
    DirectoryArn: str
    SchemaArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAttachedIndicesRequestPaginateTypeDef(TypedDict):
    DirectoryArn: str
    TargetReference: ObjectReferenceTypeDef
    ConsistencyLevel: NotRequired[ConsistencyLevelType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDevelopmentSchemaArnsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDirectoriesRequestPaginateTypeDef(TypedDict):
    state: NotRequired[DirectoryStateType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFacetAttributesRequestPaginateTypeDef(TypedDict):
    SchemaArn: str
    Name: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFacetNamesRequestPaginateTypeDef(TypedDict):
    SchemaArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListManagedSchemaArnsRequestPaginateTypeDef(TypedDict):
    SchemaArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListObjectAttributesRequestPaginateTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    ConsistencyLevel: NotRequired[ConsistencyLevelType]
    FacetFilter: NotRequired[SchemaFacetTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListObjectParentPathsRequestPaginateTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListObjectPoliciesRequestPaginateTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    ConsistencyLevel: NotRequired[ConsistencyLevelType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPolicyAttachmentsRequestPaginateTypeDef(TypedDict):
    DirectoryArn: str
    PolicyReference: ObjectReferenceTypeDef
    ConsistencyLevel: NotRequired[ConsistencyLevelType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPublishedSchemaArnsRequestPaginateTypeDef(TypedDict):
    SchemaArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceRequestPaginateTypeDef(TypedDict):
    ResourceArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTypedLinkFacetAttributesRequestPaginateTypeDef(TypedDict):
    SchemaArn: str
    Name: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTypedLinkFacetNamesRequestPaginateTypeDef(TypedDict):
    SchemaArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class LookupPolicyRequestPaginateTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class PolicyToPathTypeDef(TypedDict):
    Path: NotRequired[str]
    Policies: NotRequired[List[PolicyAttachmentTypeDef]]

RuleUnionTypeDef = Union[RuleTypeDef, RuleOutputTypeDef]

class TypedAttributeValueTypeDef(TypedDict):
    StringValue: NotRequired[str]
    BinaryValue: NotRequired[BlobTypeDef]
    BooleanValue: NotRequired[bool]
    NumberValue: NotRequired[str]
    DatetimeValue: NotRequired[TimestampTypeDef]

class BatchGetLinkAttributesResponseTypeDef(TypedDict):
    Attributes: NotRequired[List[AttributeKeyAndValueOutputTypeDef]]

class BatchGetObjectAttributesResponseTypeDef(TypedDict):
    Attributes: NotRequired[List[AttributeKeyAndValueOutputTypeDef]]

class BatchListObjectAttributesResponseTypeDef(TypedDict):
    Attributes: NotRequired[List[AttributeKeyAndValueOutputTypeDef]]
    NextToken: NotRequired[str]

class GetLinkAttributesResponseTypeDef(TypedDict):
    Attributes: List[AttributeKeyAndValueOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetObjectAttributesResponseTypeDef(TypedDict):
    Attributes: List[AttributeKeyAndValueOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IndexAttachmentTypeDef(TypedDict):
    IndexedAttributes: NotRequired[List[AttributeKeyAndValueOutputTypeDef]]
    ObjectIdentifier: NotRequired[str]

class ListObjectAttributesResponseTypeDef(TypedDict):
    Attributes: List[AttributeKeyAndValueOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TypedLinkSpecifierOutputTypeDef(TypedDict):
    TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef
    SourceObjectReference: ObjectReferenceTypeDef
    TargetObjectReference: ObjectReferenceTypeDef
    IdentityAttributeValues: List[AttributeNameAndValueOutputTypeDef]

class FacetAttributeOutputTypeDef(TypedDict):
    Name: str
    AttributeDefinition: NotRequired[FacetAttributeDefinitionOutputTypeDef]
    AttributeReference: NotRequired[FacetAttributeReferenceTypeDef]
    RequiredBehavior: NotRequired[RequiredAttributeBehaviorType]

class ListTypedLinkFacetAttributesResponseTypeDef(TypedDict):
    Attributes: List[TypedLinkAttributeDefinitionOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchLookupPolicyResponseTypeDef(TypedDict):
    PolicyToPathList: NotRequired[List[PolicyToPathTypeDef]]
    NextToken: NotRequired[str]

class LookupPolicyResponseTypeDef(TypedDict):
    PolicyToPathList: List[PolicyToPathTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

TypedAttributeValueUnionTypeDef = Union[
    TypedAttributeValueTypeDef, TypedAttributeValueOutputTypeDef
]

class BatchListAttachedIndicesResponseTypeDef(TypedDict):
    IndexAttachments: NotRequired[List[IndexAttachmentTypeDef]]
    NextToken: NotRequired[str]

class BatchListIndexResponseTypeDef(TypedDict):
    IndexAttachments: NotRequired[List[IndexAttachmentTypeDef]]
    NextToken: NotRequired[str]

class ListAttachedIndicesResponseTypeDef(TypedDict):
    IndexAttachments: List[IndexAttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListIndexResponseTypeDef(TypedDict):
    IndexAttachments: List[IndexAttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AttachTypedLinkResponseTypeDef(TypedDict):
    TypedLinkSpecifier: TypedLinkSpecifierOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchAttachTypedLinkResponseTypeDef(TypedDict):
    TypedLinkSpecifier: NotRequired[TypedLinkSpecifierOutputTypeDef]

class BatchListIncomingTypedLinksResponseTypeDef(TypedDict):
    LinkSpecifiers: NotRequired[List[TypedLinkSpecifierOutputTypeDef]]
    NextToken: NotRequired[str]

class BatchListOutgoingTypedLinksResponseTypeDef(TypedDict):
    TypedLinkSpecifiers: NotRequired[List[TypedLinkSpecifierOutputTypeDef]]
    NextToken: NotRequired[str]

class ListIncomingTypedLinksResponseTypeDef(TypedDict):
    LinkSpecifiers: List[TypedLinkSpecifierOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListOutgoingTypedLinksResponseTypeDef(TypedDict):
    TypedLinkSpecifiers: List[TypedLinkSpecifierOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListFacetAttributesResponseTypeDef(TypedDict):
    Attributes: List[FacetAttributeOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AttributeKeyAndValueTypeDef(TypedDict):
    Key: AttributeKeyTypeDef
    Value: TypedAttributeValueUnionTypeDef

class AttributeNameAndValueTypeDef(TypedDict):
    AttributeName: str
    Value: TypedAttributeValueUnionTypeDef

FacetAttributeDefinitionTypeDef = TypedDict(
    "FacetAttributeDefinitionTypeDef",
    {
        "Type": FacetAttributeTypeType,
        "DefaultValue": NotRequired[TypedAttributeValueUnionTypeDef],
        "IsImmutable": NotRequired[bool],
        "Rules": NotRequired[Mapping[str, RuleUnionTypeDef]],
    },
)

class LinkAttributeActionTypeDef(TypedDict):
    AttributeActionType: NotRequired[UpdateActionTypeType]
    AttributeUpdateValue: NotRequired[TypedAttributeValueUnionTypeDef]

class ObjectAttributeActionTypeDef(TypedDict):
    ObjectAttributeActionType: NotRequired[UpdateActionTypeType]
    ObjectAttributeUpdateValue: NotRequired[TypedAttributeValueUnionTypeDef]

class TypedAttributeValueRangeTypeDef(TypedDict):
    StartMode: RangeModeType
    EndMode: RangeModeType
    StartValue: NotRequired[TypedAttributeValueUnionTypeDef]
    EndValue: NotRequired[TypedAttributeValueUnionTypeDef]

TypedLinkAttributeDefinitionTypeDef = TypedDict(
    "TypedLinkAttributeDefinitionTypeDef",
    {
        "Name": str,
        "Type": FacetAttributeTypeType,
        "RequiredBehavior": RequiredAttributeBehaviorType,
        "DefaultValue": NotRequired[TypedAttributeValueUnionTypeDef],
        "IsImmutable": NotRequired[bool],
        "Rules": NotRequired[Mapping[str, RuleUnionTypeDef]],
    },
)

class BatchWriteOperationResponseTypeDef(TypedDict):
    CreateObject: NotRequired[BatchCreateObjectResponseTypeDef]
    AttachObject: NotRequired[BatchAttachObjectResponseTypeDef]
    DetachObject: NotRequired[BatchDetachObjectResponseTypeDef]
    UpdateObjectAttributes: NotRequired[BatchUpdateObjectAttributesResponseTypeDef]
    DeleteObject: NotRequired[Dict[str, Any]]
    AddFacetToObject: NotRequired[Dict[str, Any]]
    RemoveFacetFromObject: NotRequired[Dict[str, Any]]
    AttachPolicy: NotRequired[Dict[str, Any]]
    DetachPolicy: NotRequired[Dict[str, Any]]
    CreateIndex: NotRequired[BatchCreateIndexResponseTypeDef]
    AttachToIndex: NotRequired[BatchAttachToIndexResponseTypeDef]
    DetachFromIndex: NotRequired[BatchDetachFromIndexResponseTypeDef]
    AttachTypedLink: NotRequired[BatchAttachTypedLinkResponseTypeDef]
    DetachTypedLink: NotRequired[Dict[str, Any]]
    UpdateLinkAttributes: NotRequired[Dict[str, Any]]

class BatchReadSuccessfulResponseTypeDef(TypedDict):
    ListObjectAttributes: NotRequired[BatchListObjectAttributesResponseTypeDef]
    ListObjectChildren: NotRequired[BatchListObjectChildrenResponseTypeDef]
    GetObjectInformation: NotRequired[BatchGetObjectInformationResponseTypeDef]
    GetObjectAttributes: NotRequired[BatchGetObjectAttributesResponseTypeDef]
    ListAttachedIndices: NotRequired[BatchListAttachedIndicesResponseTypeDef]
    ListObjectParentPaths: NotRequired[BatchListObjectParentPathsResponseTypeDef]
    ListObjectPolicies: NotRequired[BatchListObjectPoliciesResponseTypeDef]
    ListPolicyAttachments: NotRequired[BatchListPolicyAttachmentsResponseTypeDef]
    LookupPolicy: NotRequired[BatchLookupPolicyResponseTypeDef]
    ListIndex: NotRequired[BatchListIndexResponseTypeDef]
    ListOutgoingTypedLinks: NotRequired[BatchListOutgoingTypedLinksResponseTypeDef]
    ListIncomingTypedLinks: NotRequired[BatchListIncomingTypedLinksResponseTypeDef]
    GetLinkAttributes: NotRequired[BatchGetLinkAttributesResponseTypeDef]
    ListObjectParents: NotRequired[BatchListObjectParentsResponseTypeDef]

AttributeKeyAndValueUnionTypeDef = Union[
    AttributeKeyAndValueTypeDef, AttributeKeyAndValueOutputTypeDef
]

class BatchCreateObjectTypeDef(TypedDict):
    SchemaFacet: Sequence[SchemaFacetTypeDef]
    ObjectAttributeList: Sequence[AttributeKeyAndValueTypeDef]
    ParentReference: NotRequired[ObjectReferenceTypeDef]
    LinkName: NotRequired[str]
    BatchReferenceName: NotRequired[str]

AttributeNameAndValueUnionTypeDef = Union[
    AttributeNameAndValueTypeDef, AttributeNameAndValueOutputTypeDef
]
FacetAttributeDefinitionUnionTypeDef = Union[
    FacetAttributeDefinitionTypeDef, FacetAttributeDefinitionOutputTypeDef
]

class LinkAttributeUpdateTypeDef(TypedDict):
    AttributeKey: NotRequired[AttributeKeyTypeDef]
    AttributeAction: NotRequired[LinkAttributeActionTypeDef]

class ObjectAttributeUpdateTypeDef(TypedDict):
    ObjectAttributeKey: NotRequired[AttributeKeyTypeDef]
    ObjectAttributeAction: NotRequired[ObjectAttributeActionTypeDef]

class ObjectAttributeRangeTypeDef(TypedDict):
    AttributeKey: NotRequired[AttributeKeyTypeDef]
    Range: NotRequired[TypedAttributeValueRangeTypeDef]

class TypedLinkAttributeRangeTypeDef(TypedDict):
    Range: TypedAttributeValueRangeTypeDef
    AttributeName: NotRequired[str]

TypedLinkAttributeDefinitionUnionTypeDef = Union[
    TypedLinkAttributeDefinitionTypeDef, TypedLinkAttributeDefinitionOutputTypeDef
]

class BatchWriteResponseTypeDef(TypedDict):
    Responses: List[BatchWriteOperationResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchReadOperationResponseTypeDef(TypedDict):
    SuccessfulResponse: NotRequired[BatchReadSuccessfulResponseTypeDef]
    ExceptionResponse: NotRequired[BatchReadExceptionTypeDef]

class AddFacetToObjectRequestTypeDef(TypedDict):
    DirectoryArn: str
    SchemaFacet: SchemaFacetTypeDef
    ObjectReference: ObjectReferenceTypeDef
    ObjectAttributeList: NotRequired[Sequence[AttributeKeyAndValueUnionTypeDef]]

class BatchAddFacetToObjectTypeDef(TypedDict):
    SchemaFacet: SchemaFacetTypeDef
    ObjectAttributeList: Sequence[AttributeKeyAndValueUnionTypeDef]
    ObjectReference: ObjectReferenceTypeDef

class CreateObjectRequestTypeDef(TypedDict):
    DirectoryArn: str
    SchemaFacets: Sequence[SchemaFacetTypeDef]
    ObjectAttributeList: NotRequired[Sequence[AttributeKeyAndValueUnionTypeDef]]
    ParentReference: NotRequired[ObjectReferenceTypeDef]
    LinkName: NotRequired[str]

class AttachTypedLinkRequestTypeDef(TypedDict):
    DirectoryArn: str
    SourceObjectReference: ObjectReferenceTypeDef
    TargetObjectReference: ObjectReferenceTypeDef
    TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef
    Attributes: Sequence[AttributeNameAndValueUnionTypeDef]

class BatchAttachTypedLinkTypeDef(TypedDict):
    SourceObjectReference: ObjectReferenceTypeDef
    TargetObjectReference: ObjectReferenceTypeDef
    TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef
    Attributes: Sequence[AttributeNameAndValueUnionTypeDef]

class TypedLinkSpecifierTypeDef(TypedDict):
    TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef
    SourceObjectReference: ObjectReferenceTypeDef
    TargetObjectReference: ObjectReferenceTypeDef
    IdentityAttributeValues: Sequence[AttributeNameAndValueUnionTypeDef]

class FacetAttributeTypeDef(TypedDict):
    Name: str
    AttributeDefinition: NotRequired[FacetAttributeDefinitionUnionTypeDef]
    AttributeReference: NotRequired[FacetAttributeReferenceTypeDef]
    RequiredBehavior: NotRequired[RequiredAttributeBehaviorType]

class BatchUpdateObjectAttributesTypeDef(TypedDict):
    ObjectReference: ObjectReferenceTypeDef
    AttributeUpdates: Sequence[ObjectAttributeUpdateTypeDef]

class UpdateObjectAttributesRequestTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    AttributeUpdates: Sequence[ObjectAttributeUpdateTypeDef]

class BatchListIndexTypeDef(TypedDict):
    IndexReference: ObjectReferenceTypeDef
    RangesOnIndexedValues: NotRequired[Sequence[ObjectAttributeRangeTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListIndexRequestPaginateTypeDef(TypedDict):
    DirectoryArn: str
    IndexReference: ObjectReferenceTypeDef
    RangesOnIndexedValues: NotRequired[Sequence[ObjectAttributeRangeTypeDef]]
    ConsistencyLevel: NotRequired[ConsistencyLevelType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIndexRequestTypeDef(TypedDict):
    DirectoryArn: str
    IndexReference: ObjectReferenceTypeDef
    RangesOnIndexedValues: NotRequired[Sequence[ObjectAttributeRangeTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ConsistencyLevel: NotRequired[ConsistencyLevelType]

class BatchListIncomingTypedLinksTypeDef(TypedDict):
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: NotRequired[Sequence[TypedLinkAttributeRangeTypeDef]]
    FilterTypedLink: NotRequired[TypedLinkSchemaAndFacetNameTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class BatchListOutgoingTypedLinksTypeDef(TypedDict):
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: NotRequired[Sequence[TypedLinkAttributeRangeTypeDef]]
    FilterTypedLink: NotRequired[TypedLinkSchemaAndFacetNameTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListIncomingTypedLinksRequestPaginateTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: NotRequired[Sequence[TypedLinkAttributeRangeTypeDef]]
    FilterTypedLink: NotRequired[TypedLinkSchemaAndFacetNameTypeDef]
    ConsistencyLevel: NotRequired[ConsistencyLevelType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIncomingTypedLinksRequestTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: NotRequired[Sequence[TypedLinkAttributeRangeTypeDef]]
    FilterTypedLink: NotRequired[TypedLinkSchemaAndFacetNameTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ConsistencyLevel: NotRequired[ConsistencyLevelType]

class ListOutgoingTypedLinksRequestPaginateTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: NotRequired[Sequence[TypedLinkAttributeRangeTypeDef]]
    FilterTypedLink: NotRequired[TypedLinkSchemaAndFacetNameTypeDef]
    ConsistencyLevel: NotRequired[ConsistencyLevelType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOutgoingTypedLinksRequestTypeDef(TypedDict):
    DirectoryArn: str
    ObjectReference: ObjectReferenceTypeDef
    FilterAttributeRanges: NotRequired[Sequence[TypedLinkAttributeRangeTypeDef]]
    FilterTypedLink: NotRequired[TypedLinkSchemaAndFacetNameTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ConsistencyLevel: NotRequired[ConsistencyLevelType]

class TypedLinkFacetAttributeUpdateTypeDef(TypedDict):
    Attribute: TypedLinkAttributeDefinitionUnionTypeDef
    Action: UpdateActionTypeType

class TypedLinkFacetTypeDef(TypedDict):
    Name: str
    Attributes: Sequence[TypedLinkAttributeDefinitionUnionTypeDef]
    IdentityAttributeOrder: Sequence[str]

class BatchReadResponseTypeDef(TypedDict):
    Responses: List[BatchReadOperationResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

TypedLinkSpecifierUnionTypeDef = Union[TypedLinkSpecifierTypeDef, TypedLinkSpecifierOutputTypeDef]
FacetAttributeUnionTypeDef = Union[FacetAttributeTypeDef, FacetAttributeOutputTypeDef]

class UpdateTypedLinkFacetRequestTypeDef(TypedDict):
    SchemaArn: str
    Name: str
    AttributeUpdates: Sequence[TypedLinkFacetAttributeUpdateTypeDef]
    IdentityAttributeOrder: Sequence[str]

class CreateTypedLinkFacetRequestTypeDef(TypedDict):
    SchemaArn: str
    Facet: TypedLinkFacetTypeDef

class BatchDetachTypedLinkTypeDef(TypedDict):
    TypedLinkSpecifier: TypedLinkSpecifierUnionTypeDef

class BatchGetLinkAttributesTypeDef(TypedDict):
    TypedLinkSpecifier: TypedLinkSpecifierUnionTypeDef
    AttributeNames: Sequence[str]

class BatchUpdateLinkAttributesTypeDef(TypedDict):
    TypedLinkSpecifier: TypedLinkSpecifierUnionTypeDef
    AttributeUpdates: Sequence[LinkAttributeUpdateTypeDef]

class DetachTypedLinkRequestTypeDef(TypedDict):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierUnionTypeDef

class GetLinkAttributesRequestTypeDef(TypedDict):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierUnionTypeDef
    AttributeNames: Sequence[str]
    ConsistencyLevel: NotRequired[ConsistencyLevelType]

class UpdateLinkAttributesRequestTypeDef(TypedDict):
    DirectoryArn: str
    TypedLinkSpecifier: TypedLinkSpecifierUnionTypeDef
    AttributeUpdates: Sequence[LinkAttributeUpdateTypeDef]

class CreateFacetRequestTypeDef(TypedDict):
    SchemaArn: str
    Name: str
    Attributes: NotRequired[Sequence[FacetAttributeUnionTypeDef]]
    ObjectType: NotRequired[ObjectTypeType]
    FacetStyle: NotRequired[FacetStyleType]

class FacetAttributeUpdateTypeDef(TypedDict):
    Attribute: NotRequired[FacetAttributeUnionTypeDef]
    Action: NotRequired[UpdateActionTypeType]

class BatchReadOperationTypeDef(TypedDict):
    ListObjectAttributes: NotRequired[BatchListObjectAttributesTypeDef]
    ListObjectChildren: NotRequired[BatchListObjectChildrenTypeDef]
    ListAttachedIndices: NotRequired[BatchListAttachedIndicesTypeDef]
    ListObjectParentPaths: NotRequired[BatchListObjectParentPathsTypeDef]
    GetObjectInformation: NotRequired[BatchGetObjectInformationTypeDef]
    GetObjectAttributes: NotRequired[BatchGetObjectAttributesTypeDef]
    ListObjectParents: NotRequired[BatchListObjectParentsTypeDef]
    ListObjectPolicies: NotRequired[BatchListObjectPoliciesTypeDef]
    ListPolicyAttachments: NotRequired[BatchListPolicyAttachmentsTypeDef]
    LookupPolicy: NotRequired[BatchLookupPolicyTypeDef]
    ListIndex: NotRequired[BatchListIndexTypeDef]
    ListOutgoingTypedLinks: NotRequired[BatchListOutgoingTypedLinksTypeDef]
    ListIncomingTypedLinks: NotRequired[BatchListIncomingTypedLinksTypeDef]
    GetLinkAttributes: NotRequired[BatchGetLinkAttributesTypeDef]

class BatchWriteOperationTypeDef(TypedDict):
    CreateObject: NotRequired[BatchCreateObjectTypeDef]
    AttachObject: NotRequired[BatchAttachObjectTypeDef]
    DetachObject: NotRequired[BatchDetachObjectTypeDef]
    UpdateObjectAttributes: NotRequired[BatchUpdateObjectAttributesTypeDef]
    DeleteObject: NotRequired[BatchDeleteObjectTypeDef]
    AddFacetToObject: NotRequired[BatchAddFacetToObjectTypeDef]
    RemoveFacetFromObject: NotRequired[BatchRemoveFacetFromObjectTypeDef]
    AttachPolicy: NotRequired[BatchAttachPolicyTypeDef]
    DetachPolicy: NotRequired[BatchDetachPolicyTypeDef]
    CreateIndex: NotRequired[BatchCreateIndexTypeDef]
    AttachToIndex: NotRequired[BatchAttachToIndexTypeDef]
    DetachFromIndex: NotRequired[BatchDetachFromIndexTypeDef]
    AttachTypedLink: NotRequired[BatchAttachTypedLinkTypeDef]
    DetachTypedLink: NotRequired[BatchDetachTypedLinkTypeDef]
    UpdateLinkAttributes: NotRequired[BatchUpdateLinkAttributesTypeDef]

class UpdateFacetRequestTypeDef(TypedDict):
    SchemaArn: str
    Name: str
    AttributeUpdates: NotRequired[Sequence[FacetAttributeUpdateTypeDef]]
    ObjectType: NotRequired[ObjectTypeType]

class BatchReadRequestTypeDef(TypedDict):
    DirectoryArn: str
    Operations: Sequence[BatchReadOperationTypeDef]
    ConsistencyLevel: NotRequired[ConsistencyLevelType]

class BatchWriteRequestTypeDef(TypedDict):
    DirectoryArn: str
    Operations: Sequence[BatchWriteOperationTypeDef]
