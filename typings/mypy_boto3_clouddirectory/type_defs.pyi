"""
Type annotations for clouddirectory service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/type_defs.html)

Usage::

    ```python
    from mypy_boto3_clouddirectory.type_defs import AddFacetToObjectRequestRequestTypeDef

    data: AddFacetToObjectRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

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

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddFacetToObjectRequestRequestTypeDef",
    "ApplySchemaRequestRequestTypeDef",
    "ApplySchemaResponseTypeDef",
    "AttachObjectRequestRequestTypeDef",
    "AttachObjectResponseTypeDef",
    "AttachPolicyRequestRequestTypeDef",
    "AttachToIndexRequestRequestTypeDef",
    "AttachToIndexResponseTypeDef",
    "AttachTypedLinkRequestRequestTypeDef",
    "AttachTypedLinkResponseTypeDef",
    "AttributeKeyAndValueTypeDef",
    "AttributeKeyTypeDef",
    "AttributeNameAndValueTypeDef",
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
    "BatchReadRequestRequestTypeDef",
    "BatchReadResponseTypeDef",
    "BatchReadSuccessfulResponseTypeDef",
    "BatchRemoveFacetFromObjectTypeDef",
    "BatchUpdateLinkAttributesTypeDef",
    "BatchUpdateObjectAttributesResponseTypeDef",
    "BatchUpdateObjectAttributesTypeDef",
    "BatchWriteOperationResponseTypeDef",
    "BatchWriteOperationTypeDef",
    "BatchWriteRequestRequestTypeDef",
    "BatchWriteResponseTypeDef",
    "CreateDirectoryRequestRequestTypeDef",
    "CreateDirectoryResponseTypeDef",
    "CreateFacetRequestRequestTypeDef",
    "CreateIndexRequestRequestTypeDef",
    "CreateIndexResponseTypeDef",
    "CreateObjectRequestRequestTypeDef",
    "CreateObjectResponseTypeDef",
    "CreateSchemaRequestRequestTypeDef",
    "CreateSchemaResponseTypeDef",
    "CreateTypedLinkFacetRequestRequestTypeDef",
    "DeleteDirectoryRequestRequestTypeDef",
    "DeleteDirectoryResponseTypeDef",
    "DeleteFacetRequestRequestTypeDef",
    "DeleteObjectRequestRequestTypeDef",
    "DeleteSchemaRequestRequestTypeDef",
    "DeleteSchemaResponseTypeDef",
    "DeleteTypedLinkFacetRequestRequestTypeDef",
    "DetachFromIndexRequestRequestTypeDef",
    "DetachFromIndexResponseTypeDef",
    "DetachObjectRequestRequestTypeDef",
    "DetachObjectResponseTypeDef",
    "DetachPolicyRequestRequestTypeDef",
    "DetachTypedLinkRequestRequestTypeDef",
    "DirectoryTypeDef",
    "DisableDirectoryRequestRequestTypeDef",
    "DisableDirectoryResponseTypeDef",
    "EnableDirectoryRequestRequestTypeDef",
    "EnableDirectoryResponseTypeDef",
    "FacetAttributeDefinitionTypeDef",
    "FacetAttributeReferenceTypeDef",
    "FacetAttributeTypeDef",
    "FacetAttributeUpdateTypeDef",
    "FacetTypeDef",
    "GetAppliedSchemaVersionRequestRequestTypeDef",
    "GetAppliedSchemaVersionResponseTypeDef",
    "GetDirectoryRequestRequestTypeDef",
    "GetDirectoryResponseTypeDef",
    "GetFacetRequestRequestTypeDef",
    "GetFacetResponseTypeDef",
    "GetLinkAttributesRequestRequestTypeDef",
    "GetLinkAttributesResponseTypeDef",
    "GetObjectAttributesRequestRequestTypeDef",
    "GetObjectAttributesResponseTypeDef",
    "GetObjectInformationRequestRequestTypeDef",
    "GetObjectInformationResponseTypeDef",
    "GetSchemaAsJsonRequestRequestTypeDef",
    "GetSchemaAsJsonResponseTypeDef",
    "GetTypedLinkFacetInformationRequestRequestTypeDef",
    "GetTypedLinkFacetInformationResponseTypeDef",
    "IndexAttachmentTypeDef",
    "LinkAttributeActionTypeDef",
    "LinkAttributeUpdateTypeDef",
    "ListAppliedSchemaArnsRequestRequestTypeDef",
    "ListAppliedSchemaArnsResponseTypeDef",
    "ListAttachedIndicesRequestRequestTypeDef",
    "ListAttachedIndicesResponseTypeDef",
    "ListDevelopmentSchemaArnsRequestRequestTypeDef",
    "ListDevelopmentSchemaArnsResponseTypeDef",
    "ListDirectoriesRequestRequestTypeDef",
    "ListDirectoriesResponseTypeDef",
    "ListFacetAttributesRequestRequestTypeDef",
    "ListFacetAttributesResponseTypeDef",
    "ListFacetNamesRequestRequestTypeDef",
    "ListFacetNamesResponseTypeDef",
    "ListIncomingTypedLinksRequestRequestTypeDef",
    "ListIncomingTypedLinksResponseTypeDef",
    "ListIndexRequestRequestTypeDef",
    "ListIndexResponseTypeDef",
    "ListManagedSchemaArnsRequestRequestTypeDef",
    "ListManagedSchemaArnsResponseTypeDef",
    "ListObjectAttributesRequestRequestTypeDef",
    "ListObjectAttributesResponseTypeDef",
    "ListObjectChildrenRequestRequestTypeDef",
    "ListObjectChildrenResponseTypeDef",
    "ListObjectParentPathsRequestRequestTypeDef",
    "ListObjectParentPathsResponseTypeDef",
    "ListObjectParentsRequestRequestTypeDef",
    "ListObjectParentsResponseTypeDef",
    "ListObjectPoliciesRequestRequestTypeDef",
    "ListObjectPoliciesResponseTypeDef",
    "ListOutgoingTypedLinksRequestRequestTypeDef",
    "ListOutgoingTypedLinksResponseTypeDef",
    "ListPolicyAttachmentsRequestRequestTypeDef",
    "ListPolicyAttachmentsResponseTypeDef",
    "ListPublishedSchemaArnsRequestRequestTypeDef",
    "ListPublishedSchemaArnsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTypedLinkFacetAttributesRequestRequestTypeDef",
    "ListTypedLinkFacetAttributesResponseTypeDef",
    "ListTypedLinkFacetNamesRequestRequestTypeDef",
    "ListTypedLinkFacetNamesResponseTypeDef",
    "LookupPolicyRequestRequestTypeDef",
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
    "PublishSchemaRequestRequestTypeDef",
    "PublishSchemaResponseTypeDef",
    "PutSchemaFromJsonRequestRequestTypeDef",
    "PutSchemaFromJsonResponseTypeDef",
    "RemoveFacetFromObjectRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RuleTypeDef",
    "SchemaFacetTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TypedAttributeValueRangeTypeDef",
    "TypedAttributeValueTypeDef",
    "TypedLinkAttributeDefinitionTypeDef",
    "TypedLinkAttributeRangeTypeDef",
    "TypedLinkFacetAttributeUpdateTypeDef",
    "TypedLinkFacetTypeDef",
    "TypedLinkSchemaAndFacetNameTypeDef",
    "TypedLinkSpecifierTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFacetRequestRequestTypeDef",
    "UpdateLinkAttributesRequestRequestTypeDef",
    "UpdateObjectAttributesRequestRequestTypeDef",
    "UpdateObjectAttributesResponseTypeDef",
    "UpdateSchemaRequestRequestTypeDef",
    "UpdateSchemaResponseTypeDef",
    "UpdateTypedLinkFacetRequestRequestTypeDef",
    "UpgradeAppliedSchemaRequestRequestTypeDef",
    "UpgradeAppliedSchemaResponseTypeDef",
    "UpgradePublishedSchemaRequestRequestTypeDef",
    "UpgradePublishedSchemaResponseTypeDef",
)

_RequiredAddFacetToObjectRequestRequestTypeDef = TypedDict(
    "_RequiredAddFacetToObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacet": "SchemaFacetTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalAddFacetToObjectRequestRequestTypeDef = TypedDict(
    "_OptionalAddFacetToObjectRequestRequestTypeDef",
    {
        "ObjectAttributeList": List["AttributeKeyAndValueTypeDef"],
    },
    total=False,
)

class AddFacetToObjectRequestRequestTypeDef(
    _RequiredAddFacetToObjectRequestRequestTypeDef, _OptionalAddFacetToObjectRequestRequestTypeDef
):
    pass

ApplySchemaRequestRequestTypeDef = TypedDict(
    "ApplySchemaRequestRequestTypeDef",
    {
        "PublishedSchemaArn": str,
        "DirectoryArn": str,
    },
)

ApplySchemaResponseTypeDef = TypedDict(
    "ApplySchemaResponseTypeDef",
    {
        "AppliedSchemaArn": str,
        "DirectoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachObjectRequestRequestTypeDef = TypedDict(
    "AttachObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ParentReference": "ObjectReferenceTypeDef",
        "ChildReference": "ObjectReferenceTypeDef",
        "LinkName": str,
    },
)

AttachObjectResponseTypeDef = TypedDict(
    "AttachObjectResponseTypeDef",
    {
        "AttachedObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachPolicyRequestRequestTypeDef = TypedDict(
    "AttachPolicyRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": "ObjectReferenceTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

AttachToIndexRequestRequestTypeDef = TypedDict(
    "AttachToIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": "ObjectReferenceTypeDef",
        "TargetReference": "ObjectReferenceTypeDef",
    },
)

AttachToIndexResponseTypeDef = TypedDict(
    "AttachToIndexResponseTypeDef",
    {
        "AttachedObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachTypedLinkRequestRequestTypeDef = TypedDict(
    "AttachTypedLinkRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SourceObjectReference": "ObjectReferenceTypeDef",
        "TargetObjectReference": "ObjectReferenceTypeDef",
        "TypedLinkFacet": "TypedLinkSchemaAndFacetNameTypeDef",
        "Attributes": List["AttributeNameAndValueTypeDef"],
    },
)

AttachTypedLinkResponseTypeDef = TypedDict(
    "AttachTypedLinkResponseTypeDef",
    {
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttributeKeyAndValueTypeDef = TypedDict(
    "AttributeKeyAndValueTypeDef",
    {
        "Key": "AttributeKeyTypeDef",
        "Value": "TypedAttributeValueTypeDef",
    },
)

AttributeKeyTypeDef = TypedDict(
    "AttributeKeyTypeDef",
    {
        "SchemaArn": str,
        "FacetName": str,
        "Name": str,
    },
)

AttributeNameAndValueTypeDef = TypedDict(
    "AttributeNameAndValueTypeDef",
    {
        "AttributeName": str,
        "Value": "TypedAttributeValueTypeDef",
    },
)

BatchAddFacetToObjectTypeDef = TypedDict(
    "BatchAddFacetToObjectTypeDef",
    {
        "SchemaFacet": "SchemaFacetTypeDef",
        "ObjectAttributeList": List["AttributeKeyAndValueTypeDef"],
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchAttachObjectResponseTypeDef = TypedDict(
    "BatchAttachObjectResponseTypeDef",
    {
        "attachedObjectIdentifier": str,
    },
    total=False,
)

BatchAttachObjectTypeDef = TypedDict(
    "BatchAttachObjectTypeDef",
    {
        "ParentReference": "ObjectReferenceTypeDef",
        "ChildReference": "ObjectReferenceTypeDef",
        "LinkName": str,
    },
)

BatchAttachPolicyTypeDef = TypedDict(
    "BatchAttachPolicyTypeDef",
    {
        "PolicyReference": "ObjectReferenceTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchAttachToIndexResponseTypeDef = TypedDict(
    "BatchAttachToIndexResponseTypeDef",
    {
        "AttachedObjectIdentifier": str,
    },
    total=False,
)

BatchAttachToIndexTypeDef = TypedDict(
    "BatchAttachToIndexTypeDef",
    {
        "IndexReference": "ObjectReferenceTypeDef",
        "TargetReference": "ObjectReferenceTypeDef",
    },
)

BatchAttachTypedLinkResponseTypeDef = TypedDict(
    "BatchAttachTypedLinkResponseTypeDef",
    {
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
    },
    total=False,
)

BatchAttachTypedLinkTypeDef = TypedDict(
    "BatchAttachTypedLinkTypeDef",
    {
        "SourceObjectReference": "ObjectReferenceTypeDef",
        "TargetObjectReference": "ObjectReferenceTypeDef",
        "TypedLinkFacet": "TypedLinkSchemaAndFacetNameTypeDef",
        "Attributes": List["AttributeNameAndValueTypeDef"],
    },
)

BatchCreateIndexResponseTypeDef = TypedDict(
    "BatchCreateIndexResponseTypeDef",
    {
        "ObjectIdentifier": str,
    },
    total=False,
)

_RequiredBatchCreateIndexTypeDef = TypedDict(
    "_RequiredBatchCreateIndexTypeDef",
    {
        "OrderedIndexedAttributeList": List["AttributeKeyTypeDef"],
        "IsUnique": bool,
    },
)
_OptionalBatchCreateIndexTypeDef = TypedDict(
    "_OptionalBatchCreateIndexTypeDef",
    {
        "ParentReference": "ObjectReferenceTypeDef",
        "LinkName": str,
        "BatchReferenceName": str,
    },
    total=False,
)

class BatchCreateIndexTypeDef(_RequiredBatchCreateIndexTypeDef, _OptionalBatchCreateIndexTypeDef):
    pass

BatchCreateObjectResponseTypeDef = TypedDict(
    "BatchCreateObjectResponseTypeDef",
    {
        "ObjectIdentifier": str,
    },
    total=False,
)

_RequiredBatchCreateObjectTypeDef = TypedDict(
    "_RequiredBatchCreateObjectTypeDef",
    {
        "SchemaFacet": List["SchemaFacetTypeDef"],
        "ObjectAttributeList": List["AttributeKeyAndValueTypeDef"],
    },
)
_OptionalBatchCreateObjectTypeDef = TypedDict(
    "_OptionalBatchCreateObjectTypeDef",
    {
        "ParentReference": "ObjectReferenceTypeDef",
        "LinkName": str,
        "BatchReferenceName": str,
    },
    total=False,
)

class BatchCreateObjectTypeDef(
    _RequiredBatchCreateObjectTypeDef, _OptionalBatchCreateObjectTypeDef
):
    pass

BatchDeleteObjectTypeDef = TypedDict(
    "BatchDeleteObjectTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchDetachFromIndexResponseTypeDef = TypedDict(
    "BatchDetachFromIndexResponseTypeDef",
    {
        "DetachedObjectIdentifier": str,
    },
    total=False,
)

BatchDetachFromIndexTypeDef = TypedDict(
    "BatchDetachFromIndexTypeDef",
    {
        "IndexReference": "ObjectReferenceTypeDef",
        "TargetReference": "ObjectReferenceTypeDef",
    },
)

BatchDetachObjectResponseTypeDef = TypedDict(
    "BatchDetachObjectResponseTypeDef",
    {
        "detachedObjectIdentifier": str,
    },
    total=False,
)

_RequiredBatchDetachObjectTypeDef = TypedDict(
    "_RequiredBatchDetachObjectTypeDef",
    {
        "ParentReference": "ObjectReferenceTypeDef",
        "LinkName": str,
    },
)
_OptionalBatchDetachObjectTypeDef = TypedDict(
    "_OptionalBatchDetachObjectTypeDef",
    {
        "BatchReferenceName": str,
    },
    total=False,
)

class BatchDetachObjectTypeDef(
    _RequiredBatchDetachObjectTypeDef, _OptionalBatchDetachObjectTypeDef
):
    pass

BatchDetachPolicyTypeDef = TypedDict(
    "BatchDetachPolicyTypeDef",
    {
        "PolicyReference": "ObjectReferenceTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchDetachTypedLinkTypeDef = TypedDict(
    "BatchDetachTypedLinkTypeDef",
    {
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
    },
)

BatchGetLinkAttributesResponseTypeDef = TypedDict(
    "BatchGetLinkAttributesResponseTypeDef",
    {
        "Attributes": List["AttributeKeyAndValueTypeDef"],
    },
    total=False,
)

BatchGetLinkAttributesTypeDef = TypedDict(
    "BatchGetLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
        "AttributeNames": List[str],
    },
)

BatchGetObjectAttributesResponseTypeDef = TypedDict(
    "BatchGetObjectAttributesResponseTypeDef",
    {
        "Attributes": List["AttributeKeyAndValueTypeDef"],
    },
    total=False,
)

BatchGetObjectAttributesTypeDef = TypedDict(
    "BatchGetObjectAttributesTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
        "SchemaFacet": "SchemaFacetTypeDef",
        "AttributeNames": List[str],
    },
)

BatchGetObjectInformationResponseTypeDef = TypedDict(
    "BatchGetObjectInformationResponseTypeDef",
    {
        "SchemaFacets": List["SchemaFacetTypeDef"],
        "ObjectIdentifier": str,
    },
    total=False,
)

BatchGetObjectInformationTypeDef = TypedDict(
    "BatchGetObjectInformationTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchListAttachedIndicesResponseTypeDef = TypedDict(
    "BatchListAttachedIndicesResponseTypeDef",
    {
        "IndexAttachments": List["IndexAttachmentTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListAttachedIndicesTypeDef = TypedDict(
    "_RequiredBatchListAttachedIndicesTypeDef",
    {
        "TargetReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListAttachedIndicesTypeDef = TypedDict(
    "_OptionalBatchListAttachedIndicesTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class BatchListAttachedIndicesTypeDef(
    _RequiredBatchListAttachedIndicesTypeDef, _OptionalBatchListAttachedIndicesTypeDef
):
    pass

BatchListIncomingTypedLinksResponseTypeDef = TypedDict(
    "BatchListIncomingTypedLinksResponseTypeDef",
    {
        "LinkSpecifiers": List["TypedLinkSpecifierTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListIncomingTypedLinksTypeDef = TypedDict(
    "_RequiredBatchListIncomingTypedLinksTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListIncomingTypedLinksTypeDef = TypedDict(
    "_OptionalBatchListIncomingTypedLinksTypeDef",
    {
        "FilterAttributeRanges": List["TypedLinkAttributeRangeTypeDef"],
        "FilterTypedLink": "TypedLinkSchemaAndFacetNameTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class BatchListIncomingTypedLinksTypeDef(
    _RequiredBatchListIncomingTypedLinksTypeDef, _OptionalBatchListIncomingTypedLinksTypeDef
):
    pass

BatchListIndexResponseTypeDef = TypedDict(
    "BatchListIndexResponseTypeDef",
    {
        "IndexAttachments": List["IndexAttachmentTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListIndexTypeDef = TypedDict(
    "_RequiredBatchListIndexTypeDef",
    {
        "IndexReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListIndexTypeDef = TypedDict(
    "_OptionalBatchListIndexTypeDef",
    {
        "RangesOnIndexedValues": List["ObjectAttributeRangeTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class BatchListIndexTypeDef(_RequiredBatchListIndexTypeDef, _OptionalBatchListIndexTypeDef):
    pass

BatchListObjectAttributesResponseTypeDef = TypedDict(
    "BatchListObjectAttributesResponseTypeDef",
    {
        "Attributes": List["AttributeKeyAndValueTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListObjectAttributesTypeDef = TypedDict(
    "_RequiredBatchListObjectAttributesTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListObjectAttributesTypeDef = TypedDict(
    "_OptionalBatchListObjectAttributesTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "FacetFilter": "SchemaFacetTypeDef",
    },
    total=False,
)

class BatchListObjectAttributesTypeDef(
    _RequiredBatchListObjectAttributesTypeDef, _OptionalBatchListObjectAttributesTypeDef
):
    pass

BatchListObjectChildrenResponseTypeDef = TypedDict(
    "BatchListObjectChildrenResponseTypeDef",
    {
        "Children": Dict[str, str],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListObjectChildrenTypeDef = TypedDict(
    "_RequiredBatchListObjectChildrenTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListObjectChildrenTypeDef = TypedDict(
    "_OptionalBatchListObjectChildrenTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class BatchListObjectChildrenTypeDef(
    _RequiredBatchListObjectChildrenTypeDef, _OptionalBatchListObjectChildrenTypeDef
):
    pass

BatchListObjectParentPathsResponseTypeDef = TypedDict(
    "BatchListObjectParentPathsResponseTypeDef",
    {
        "PathToObjectIdentifiersList": List["PathToObjectIdentifiersTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListObjectParentPathsTypeDef = TypedDict(
    "_RequiredBatchListObjectParentPathsTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListObjectParentPathsTypeDef = TypedDict(
    "_OptionalBatchListObjectParentPathsTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class BatchListObjectParentPathsTypeDef(
    _RequiredBatchListObjectParentPathsTypeDef, _OptionalBatchListObjectParentPathsTypeDef
):
    pass

BatchListObjectParentsResponseTypeDef = TypedDict(
    "BatchListObjectParentsResponseTypeDef",
    {
        "ParentLinks": List["ObjectIdentifierAndLinkNameTupleTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListObjectParentsTypeDef = TypedDict(
    "_RequiredBatchListObjectParentsTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListObjectParentsTypeDef = TypedDict(
    "_OptionalBatchListObjectParentsTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class BatchListObjectParentsTypeDef(
    _RequiredBatchListObjectParentsTypeDef, _OptionalBatchListObjectParentsTypeDef
):
    pass

BatchListObjectPoliciesResponseTypeDef = TypedDict(
    "BatchListObjectPoliciesResponseTypeDef",
    {
        "AttachedPolicyIds": List[str],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListObjectPoliciesTypeDef = TypedDict(
    "_RequiredBatchListObjectPoliciesTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListObjectPoliciesTypeDef = TypedDict(
    "_OptionalBatchListObjectPoliciesTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class BatchListObjectPoliciesTypeDef(
    _RequiredBatchListObjectPoliciesTypeDef, _OptionalBatchListObjectPoliciesTypeDef
):
    pass

BatchListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "BatchListOutgoingTypedLinksResponseTypeDef",
    {
        "TypedLinkSpecifiers": List["TypedLinkSpecifierTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListOutgoingTypedLinksTypeDef = TypedDict(
    "_RequiredBatchListOutgoingTypedLinksTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListOutgoingTypedLinksTypeDef = TypedDict(
    "_OptionalBatchListOutgoingTypedLinksTypeDef",
    {
        "FilterAttributeRanges": List["TypedLinkAttributeRangeTypeDef"],
        "FilterTypedLink": "TypedLinkSchemaAndFacetNameTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class BatchListOutgoingTypedLinksTypeDef(
    _RequiredBatchListOutgoingTypedLinksTypeDef, _OptionalBatchListOutgoingTypedLinksTypeDef
):
    pass

BatchListPolicyAttachmentsResponseTypeDef = TypedDict(
    "BatchListPolicyAttachmentsResponseTypeDef",
    {
        "ObjectIdentifiers": List[str],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListPolicyAttachmentsTypeDef = TypedDict(
    "_RequiredBatchListPolicyAttachmentsTypeDef",
    {
        "PolicyReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListPolicyAttachmentsTypeDef = TypedDict(
    "_OptionalBatchListPolicyAttachmentsTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class BatchListPolicyAttachmentsTypeDef(
    _RequiredBatchListPolicyAttachmentsTypeDef, _OptionalBatchListPolicyAttachmentsTypeDef
):
    pass

BatchLookupPolicyResponseTypeDef = TypedDict(
    "BatchLookupPolicyResponseTypeDef",
    {
        "PolicyToPathList": List["PolicyToPathTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchLookupPolicyTypeDef = TypedDict(
    "_RequiredBatchLookupPolicyTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchLookupPolicyTypeDef = TypedDict(
    "_OptionalBatchLookupPolicyTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class BatchLookupPolicyTypeDef(
    _RequiredBatchLookupPolicyTypeDef, _OptionalBatchLookupPolicyTypeDef
):
    pass

BatchReadExceptionTypeDef = TypedDict(
    "BatchReadExceptionTypeDef",
    {
        "Type": BatchReadExceptionTypeType,
        "Message": str,
    },
    total=False,
)

BatchReadOperationResponseTypeDef = TypedDict(
    "BatchReadOperationResponseTypeDef",
    {
        "SuccessfulResponse": "BatchReadSuccessfulResponseTypeDef",
        "ExceptionResponse": "BatchReadExceptionTypeDef",
    },
    total=False,
)

BatchReadOperationTypeDef = TypedDict(
    "BatchReadOperationTypeDef",
    {
        "ListObjectAttributes": "BatchListObjectAttributesTypeDef",
        "ListObjectChildren": "BatchListObjectChildrenTypeDef",
        "ListAttachedIndices": "BatchListAttachedIndicesTypeDef",
        "ListObjectParentPaths": "BatchListObjectParentPathsTypeDef",
        "GetObjectInformation": "BatchGetObjectInformationTypeDef",
        "GetObjectAttributes": "BatchGetObjectAttributesTypeDef",
        "ListObjectParents": "BatchListObjectParentsTypeDef",
        "ListObjectPolicies": "BatchListObjectPoliciesTypeDef",
        "ListPolicyAttachments": "BatchListPolicyAttachmentsTypeDef",
        "LookupPolicy": "BatchLookupPolicyTypeDef",
        "ListIndex": "BatchListIndexTypeDef",
        "ListOutgoingTypedLinks": "BatchListOutgoingTypedLinksTypeDef",
        "ListIncomingTypedLinks": "BatchListIncomingTypedLinksTypeDef",
        "GetLinkAttributes": "BatchGetLinkAttributesTypeDef",
    },
    total=False,
)

_RequiredBatchReadRequestRequestTypeDef = TypedDict(
    "_RequiredBatchReadRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "Operations": List["BatchReadOperationTypeDef"],
    },
)
_OptionalBatchReadRequestRequestTypeDef = TypedDict(
    "_OptionalBatchReadRequestRequestTypeDef",
    {
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)

class BatchReadRequestRequestTypeDef(
    _RequiredBatchReadRequestRequestTypeDef, _OptionalBatchReadRequestRequestTypeDef
):
    pass

BatchReadResponseTypeDef = TypedDict(
    "BatchReadResponseTypeDef",
    {
        "Responses": List["BatchReadOperationResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchReadSuccessfulResponseTypeDef = TypedDict(
    "BatchReadSuccessfulResponseTypeDef",
    {
        "ListObjectAttributes": "BatchListObjectAttributesResponseTypeDef",
        "ListObjectChildren": "BatchListObjectChildrenResponseTypeDef",
        "GetObjectInformation": "BatchGetObjectInformationResponseTypeDef",
        "GetObjectAttributes": "BatchGetObjectAttributesResponseTypeDef",
        "ListAttachedIndices": "BatchListAttachedIndicesResponseTypeDef",
        "ListObjectParentPaths": "BatchListObjectParentPathsResponseTypeDef",
        "ListObjectPolicies": "BatchListObjectPoliciesResponseTypeDef",
        "ListPolicyAttachments": "BatchListPolicyAttachmentsResponseTypeDef",
        "LookupPolicy": "BatchLookupPolicyResponseTypeDef",
        "ListIndex": "BatchListIndexResponseTypeDef",
        "ListOutgoingTypedLinks": "BatchListOutgoingTypedLinksResponseTypeDef",
        "ListIncomingTypedLinks": "BatchListIncomingTypedLinksResponseTypeDef",
        "GetLinkAttributes": "BatchGetLinkAttributesResponseTypeDef",
        "ListObjectParents": "BatchListObjectParentsResponseTypeDef",
    },
    total=False,
)

BatchRemoveFacetFromObjectTypeDef = TypedDict(
    "BatchRemoveFacetFromObjectTypeDef",
    {
        "SchemaFacet": "SchemaFacetTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchUpdateLinkAttributesTypeDef = TypedDict(
    "BatchUpdateLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
        "AttributeUpdates": List["LinkAttributeUpdateTypeDef"],
    },
)

BatchUpdateObjectAttributesResponseTypeDef = TypedDict(
    "BatchUpdateObjectAttributesResponseTypeDef",
    {
        "ObjectIdentifier": str,
    },
    total=False,
)

BatchUpdateObjectAttributesTypeDef = TypedDict(
    "BatchUpdateObjectAttributesTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
        "AttributeUpdates": List["ObjectAttributeUpdateTypeDef"],
    },
)

BatchWriteOperationResponseTypeDef = TypedDict(
    "BatchWriteOperationResponseTypeDef",
    {
        "CreateObject": "BatchCreateObjectResponseTypeDef",
        "AttachObject": "BatchAttachObjectResponseTypeDef",
        "DetachObject": "BatchDetachObjectResponseTypeDef",
        "UpdateObjectAttributes": "BatchUpdateObjectAttributesResponseTypeDef",
        "DeleteObject": Dict[str, Any],
        "AddFacetToObject": Dict[str, Any],
        "RemoveFacetFromObject": Dict[str, Any],
        "AttachPolicy": Dict[str, Any],
        "DetachPolicy": Dict[str, Any],
        "CreateIndex": "BatchCreateIndexResponseTypeDef",
        "AttachToIndex": "BatchAttachToIndexResponseTypeDef",
        "DetachFromIndex": "BatchDetachFromIndexResponseTypeDef",
        "AttachTypedLink": "BatchAttachTypedLinkResponseTypeDef",
        "DetachTypedLink": Dict[str, Any],
        "UpdateLinkAttributes": Dict[str, Any],
    },
    total=False,
)

BatchWriteOperationTypeDef = TypedDict(
    "BatchWriteOperationTypeDef",
    {
        "CreateObject": "BatchCreateObjectTypeDef",
        "AttachObject": "BatchAttachObjectTypeDef",
        "DetachObject": "BatchDetachObjectTypeDef",
        "UpdateObjectAttributes": "BatchUpdateObjectAttributesTypeDef",
        "DeleteObject": "BatchDeleteObjectTypeDef",
        "AddFacetToObject": "BatchAddFacetToObjectTypeDef",
        "RemoveFacetFromObject": "BatchRemoveFacetFromObjectTypeDef",
        "AttachPolicy": "BatchAttachPolicyTypeDef",
        "DetachPolicy": "BatchDetachPolicyTypeDef",
        "CreateIndex": "BatchCreateIndexTypeDef",
        "AttachToIndex": "BatchAttachToIndexTypeDef",
        "DetachFromIndex": "BatchDetachFromIndexTypeDef",
        "AttachTypedLink": "BatchAttachTypedLinkTypeDef",
        "DetachTypedLink": "BatchDetachTypedLinkTypeDef",
        "UpdateLinkAttributes": "BatchUpdateLinkAttributesTypeDef",
    },
    total=False,
)

BatchWriteRequestRequestTypeDef = TypedDict(
    "BatchWriteRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "Operations": List["BatchWriteOperationTypeDef"],
    },
)

BatchWriteResponseTypeDef = TypedDict(
    "BatchWriteResponseTypeDef",
    {
        "Responses": List["BatchWriteOperationResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDirectoryRequestRequestTypeDef = TypedDict(
    "CreateDirectoryRequestRequestTypeDef",
    {
        "Name": str,
        "SchemaArn": str,
    },
)

CreateDirectoryResponseTypeDef = TypedDict(
    "CreateDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "Name": str,
        "ObjectIdentifier": str,
        "AppliedSchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFacetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
_OptionalCreateFacetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFacetRequestRequestTypeDef",
    {
        "Attributes": List["FacetAttributeTypeDef"],
        "ObjectType": ObjectTypeType,
        "FacetStyle": FacetStyleType,
    },
    total=False,
)

class CreateFacetRequestRequestTypeDef(
    _RequiredCreateFacetRequestRequestTypeDef, _OptionalCreateFacetRequestRequestTypeDef
):
    pass

_RequiredCreateIndexRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "OrderedIndexedAttributeList": List["AttributeKeyTypeDef"],
        "IsUnique": bool,
    },
)
_OptionalCreateIndexRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIndexRequestRequestTypeDef",
    {
        "ParentReference": "ObjectReferenceTypeDef",
        "LinkName": str,
    },
    total=False,
)

class CreateIndexRequestRequestTypeDef(
    _RequiredCreateIndexRequestRequestTypeDef, _OptionalCreateIndexRequestRequestTypeDef
):
    pass

CreateIndexResponseTypeDef = TypedDict(
    "CreateIndexResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateObjectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacets": List["SchemaFacetTypeDef"],
    },
)
_OptionalCreateObjectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateObjectRequestRequestTypeDef",
    {
        "ObjectAttributeList": List["AttributeKeyAndValueTypeDef"],
        "ParentReference": "ObjectReferenceTypeDef",
        "LinkName": str,
    },
    total=False,
)

class CreateObjectRequestRequestTypeDef(
    _RequiredCreateObjectRequestRequestTypeDef, _OptionalCreateObjectRequestRequestTypeDef
):
    pass

CreateObjectResponseTypeDef = TypedDict(
    "CreateObjectResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSchemaRequestRequestTypeDef = TypedDict(
    "CreateSchemaRequestRequestTypeDef",
    {
        "Name": str,
    },
)

CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTypedLinkFacetRequestRequestTypeDef = TypedDict(
    "CreateTypedLinkFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Facet": "TypedLinkFacetTypeDef",
    },
)

DeleteDirectoryRequestRequestTypeDef = TypedDict(
    "DeleteDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)

DeleteDirectoryResponseTypeDef = TypedDict(
    "DeleteDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFacetRequestRequestTypeDef = TypedDict(
    "DeleteFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

DeleteObjectRequestRequestTypeDef = TypedDict(
    "DeleteObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

DeleteSchemaRequestRequestTypeDef = TypedDict(
    "DeleteSchemaRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)

DeleteSchemaResponseTypeDef = TypedDict(
    "DeleteSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTypedLinkFacetRequestRequestTypeDef = TypedDict(
    "DeleteTypedLinkFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

DetachFromIndexRequestRequestTypeDef = TypedDict(
    "DetachFromIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": "ObjectReferenceTypeDef",
        "TargetReference": "ObjectReferenceTypeDef",
    },
)

DetachFromIndexResponseTypeDef = TypedDict(
    "DetachFromIndexResponseTypeDef",
    {
        "DetachedObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachObjectRequestRequestTypeDef = TypedDict(
    "DetachObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ParentReference": "ObjectReferenceTypeDef",
        "LinkName": str,
    },
)

DetachObjectResponseTypeDef = TypedDict(
    "DetachObjectResponseTypeDef",
    {
        "DetachedObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachPolicyRequestRequestTypeDef = TypedDict(
    "DetachPolicyRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": "ObjectReferenceTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

DetachTypedLinkRequestRequestTypeDef = TypedDict(
    "DetachTypedLinkRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
    },
)

DirectoryTypeDef = TypedDict(
    "DirectoryTypeDef",
    {
        "Name": str,
        "DirectoryArn": str,
        "State": DirectoryStateType,
        "CreationDateTime": datetime,
    },
    total=False,
)

DisableDirectoryRequestRequestTypeDef = TypedDict(
    "DisableDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)

DisableDirectoryResponseTypeDef = TypedDict(
    "DisableDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableDirectoryRequestRequestTypeDef = TypedDict(
    "EnableDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)

EnableDirectoryResponseTypeDef = TypedDict(
    "EnableDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFacetAttributeDefinitionTypeDef = TypedDict(
    "_RequiredFacetAttributeDefinitionTypeDef",
    {
        "Type": FacetAttributeTypeType,
    },
)
_OptionalFacetAttributeDefinitionTypeDef = TypedDict(
    "_OptionalFacetAttributeDefinitionTypeDef",
    {
        "DefaultValue": "TypedAttributeValueTypeDef",
        "IsImmutable": bool,
        "Rules": Dict[str, "RuleTypeDef"],
    },
    total=False,
)

class FacetAttributeDefinitionTypeDef(
    _RequiredFacetAttributeDefinitionTypeDef, _OptionalFacetAttributeDefinitionTypeDef
):
    pass

FacetAttributeReferenceTypeDef = TypedDict(
    "FacetAttributeReferenceTypeDef",
    {
        "TargetFacetName": str,
        "TargetAttributeName": str,
    },
)

_RequiredFacetAttributeTypeDef = TypedDict(
    "_RequiredFacetAttributeTypeDef",
    {
        "Name": str,
    },
)
_OptionalFacetAttributeTypeDef = TypedDict(
    "_OptionalFacetAttributeTypeDef",
    {
        "AttributeDefinition": "FacetAttributeDefinitionTypeDef",
        "AttributeReference": "FacetAttributeReferenceTypeDef",
        "RequiredBehavior": RequiredAttributeBehaviorType,
    },
    total=False,
)

class FacetAttributeTypeDef(_RequiredFacetAttributeTypeDef, _OptionalFacetAttributeTypeDef):
    pass

FacetAttributeUpdateTypeDef = TypedDict(
    "FacetAttributeUpdateTypeDef",
    {
        "Attribute": "FacetAttributeTypeDef",
        "Action": UpdateActionTypeType,
    },
    total=False,
)

FacetTypeDef = TypedDict(
    "FacetTypeDef",
    {
        "Name": str,
        "ObjectType": ObjectTypeType,
        "FacetStyle": FacetStyleType,
    },
    total=False,
)

GetAppliedSchemaVersionRequestRequestTypeDef = TypedDict(
    "GetAppliedSchemaVersionRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)

GetAppliedSchemaVersionResponseTypeDef = TypedDict(
    "GetAppliedSchemaVersionResponseTypeDef",
    {
        "AppliedSchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDirectoryRequestRequestTypeDef = TypedDict(
    "GetDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)

GetDirectoryResponseTypeDef = TypedDict(
    "GetDirectoryResponseTypeDef",
    {
        "Directory": "DirectoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFacetRequestRequestTypeDef = TypedDict(
    "GetFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

GetFacetResponseTypeDef = TypedDict(
    "GetFacetResponseTypeDef",
    {
        "Facet": "FacetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLinkAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredGetLinkAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
        "AttributeNames": List[str],
    },
)
_OptionalGetLinkAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalGetLinkAttributesRequestRequestTypeDef",
    {
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)

class GetLinkAttributesRequestRequestTypeDef(
    _RequiredGetLinkAttributesRequestRequestTypeDef, _OptionalGetLinkAttributesRequestRequestTypeDef
):
    pass

GetLinkAttributesResponseTypeDef = TypedDict(
    "GetLinkAttributesResponseTypeDef",
    {
        "Attributes": List["AttributeKeyAndValueTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredGetObjectAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
        "SchemaFacet": "SchemaFacetTypeDef",
        "AttributeNames": List[str],
    },
)
_OptionalGetObjectAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalGetObjectAttributesRequestRequestTypeDef",
    {
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)

class GetObjectAttributesRequestRequestTypeDef(
    _RequiredGetObjectAttributesRequestRequestTypeDef,
    _OptionalGetObjectAttributesRequestRequestTypeDef,
):
    pass

GetObjectAttributesResponseTypeDef = TypedDict(
    "GetObjectAttributesResponseTypeDef",
    {
        "Attributes": List["AttributeKeyAndValueTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectInformationRequestRequestTypeDef = TypedDict(
    "_RequiredGetObjectInformationRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalGetObjectInformationRequestRequestTypeDef = TypedDict(
    "_OptionalGetObjectInformationRequestRequestTypeDef",
    {
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)

class GetObjectInformationRequestRequestTypeDef(
    _RequiredGetObjectInformationRequestRequestTypeDef,
    _OptionalGetObjectInformationRequestRequestTypeDef,
):
    pass

GetObjectInformationResponseTypeDef = TypedDict(
    "GetObjectInformationResponseTypeDef",
    {
        "SchemaFacets": List["SchemaFacetTypeDef"],
        "ObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaAsJsonRequestRequestTypeDef = TypedDict(
    "GetSchemaAsJsonRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)

GetSchemaAsJsonResponseTypeDef = TypedDict(
    "GetSchemaAsJsonResponseTypeDef",
    {
        "Name": str,
        "Document": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTypedLinkFacetInformationRequestRequestTypeDef = TypedDict(
    "GetTypedLinkFacetInformationRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

GetTypedLinkFacetInformationResponseTypeDef = TypedDict(
    "GetTypedLinkFacetInformationResponseTypeDef",
    {
        "IdentityAttributeOrder": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IndexAttachmentTypeDef = TypedDict(
    "IndexAttachmentTypeDef",
    {
        "IndexedAttributes": List["AttributeKeyAndValueTypeDef"],
        "ObjectIdentifier": str,
    },
    total=False,
)

LinkAttributeActionTypeDef = TypedDict(
    "LinkAttributeActionTypeDef",
    {
        "AttributeActionType": UpdateActionTypeType,
        "AttributeUpdateValue": "TypedAttributeValueTypeDef",
    },
    total=False,
)

LinkAttributeUpdateTypeDef = TypedDict(
    "LinkAttributeUpdateTypeDef",
    {
        "AttributeKey": "AttributeKeyTypeDef",
        "AttributeAction": "LinkAttributeActionTypeDef",
    },
    total=False,
)

_RequiredListAppliedSchemaArnsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppliedSchemaArnsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)
_OptionalListAppliedSchemaArnsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppliedSchemaArnsRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListAppliedSchemaArnsRequestRequestTypeDef(
    _RequiredListAppliedSchemaArnsRequestRequestTypeDef,
    _OptionalListAppliedSchemaArnsRequestRequestTypeDef,
):
    pass

ListAppliedSchemaArnsResponseTypeDef = TypedDict(
    "ListAppliedSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAttachedIndicesRequestRequestTypeDef = TypedDict(
    "_RequiredListAttachedIndicesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TargetReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListAttachedIndicesRequestRequestTypeDef = TypedDict(
    "_OptionalListAttachedIndicesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)

class ListAttachedIndicesRequestRequestTypeDef(
    _RequiredListAttachedIndicesRequestRequestTypeDef,
    _OptionalListAttachedIndicesRequestRequestTypeDef,
):
    pass

ListAttachedIndicesResponseTypeDef = TypedDict(
    "ListAttachedIndicesResponseTypeDef",
    {
        "IndexAttachments": List["IndexAttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevelopmentSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDevelopmentSchemaArnsResponseTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDirectoriesRequestRequestTypeDef = TypedDict(
    "ListDirectoriesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "state": DirectoryStateType,
    },
    total=False,
)

ListDirectoriesResponseTypeDef = TypedDict(
    "ListDirectoriesResponseTypeDef",
    {
        "Directories": List["DirectoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFacetAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredListFacetAttributesRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
_OptionalListFacetAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalListFacetAttributesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListFacetAttributesRequestRequestTypeDef(
    _RequiredListFacetAttributesRequestRequestTypeDef,
    _OptionalListFacetAttributesRequestRequestTypeDef,
):
    pass

ListFacetAttributesResponseTypeDef = TypedDict(
    "ListFacetAttributesResponseTypeDef",
    {
        "Attributes": List["FacetAttributeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFacetNamesRequestRequestTypeDef = TypedDict(
    "_RequiredListFacetNamesRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)
_OptionalListFacetNamesRequestRequestTypeDef = TypedDict(
    "_OptionalListFacetNamesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListFacetNamesRequestRequestTypeDef(
    _RequiredListFacetNamesRequestRequestTypeDef, _OptionalListFacetNamesRequestRequestTypeDef
):
    pass

ListFacetNamesResponseTypeDef = TypedDict(
    "ListFacetNamesResponseTypeDef",
    {
        "FacetNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIncomingTypedLinksRequestRequestTypeDef = TypedDict(
    "_RequiredListIncomingTypedLinksRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListIncomingTypedLinksRequestRequestTypeDef = TypedDict(
    "_OptionalListIncomingTypedLinksRequestRequestTypeDef",
    {
        "FilterAttributeRanges": List["TypedLinkAttributeRangeTypeDef"],
        "FilterTypedLink": "TypedLinkSchemaAndFacetNameTypeDef",
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)

class ListIncomingTypedLinksRequestRequestTypeDef(
    _RequiredListIncomingTypedLinksRequestRequestTypeDef,
    _OptionalListIncomingTypedLinksRequestRequestTypeDef,
):
    pass

ListIncomingTypedLinksResponseTypeDef = TypedDict(
    "ListIncomingTypedLinksResponseTypeDef",
    {
        "LinkSpecifiers": List["TypedLinkSpecifierTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIndexRequestRequestTypeDef = TypedDict(
    "_RequiredListIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListIndexRequestRequestTypeDef = TypedDict(
    "_OptionalListIndexRequestRequestTypeDef",
    {
        "RangesOnIndexedValues": List["ObjectAttributeRangeTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)

class ListIndexRequestRequestTypeDef(
    _RequiredListIndexRequestRequestTypeDef, _OptionalListIndexRequestRequestTypeDef
):
    pass

ListIndexResponseTypeDef = TypedDict(
    "ListIndexResponseTypeDef",
    {
        "IndexAttachments": List["IndexAttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListManagedSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListManagedSchemaArnsRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListManagedSchemaArnsResponseTypeDef = TypedDict(
    "ListManagedSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListObjectAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredListObjectAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListObjectAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalListObjectAttributesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
        "FacetFilter": "SchemaFacetTypeDef",
    },
    total=False,
)

class ListObjectAttributesRequestRequestTypeDef(
    _RequiredListObjectAttributesRequestRequestTypeDef,
    _OptionalListObjectAttributesRequestRequestTypeDef,
):
    pass

ListObjectAttributesResponseTypeDef = TypedDict(
    "ListObjectAttributesResponseTypeDef",
    {
        "Attributes": List["AttributeKeyAndValueTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListObjectChildrenRequestRequestTypeDef = TypedDict(
    "_RequiredListObjectChildrenRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListObjectChildrenRequestRequestTypeDef = TypedDict(
    "_OptionalListObjectChildrenRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)

class ListObjectChildrenRequestRequestTypeDef(
    _RequiredListObjectChildrenRequestRequestTypeDef,
    _OptionalListObjectChildrenRequestRequestTypeDef,
):
    pass

ListObjectChildrenResponseTypeDef = TypedDict(
    "ListObjectChildrenResponseTypeDef",
    {
        "Children": Dict[str, str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListObjectParentPathsRequestRequestTypeDef = TypedDict(
    "_RequiredListObjectParentPathsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListObjectParentPathsRequestRequestTypeDef = TypedDict(
    "_OptionalListObjectParentPathsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListObjectParentPathsRequestRequestTypeDef(
    _RequiredListObjectParentPathsRequestRequestTypeDef,
    _OptionalListObjectParentPathsRequestRequestTypeDef,
):
    pass

ListObjectParentPathsResponseTypeDef = TypedDict(
    "ListObjectParentPathsResponseTypeDef",
    {
        "PathToObjectIdentifiersList": List["PathToObjectIdentifiersTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListObjectParentsRequestRequestTypeDef = TypedDict(
    "_RequiredListObjectParentsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListObjectParentsRequestRequestTypeDef = TypedDict(
    "_OptionalListObjectParentsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
        "IncludeAllLinksToEachParent": bool,
    },
    total=False,
)

class ListObjectParentsRequestRequestTypeDef(
    _RequiredListObjectParentsRequestRequestTypeDef, _OptionalListObjectParentsRequestRequestTypeDef
):
    pass

ListObjectParentsResponseTypeDef = TypedDict(
    "ListObjectParentsResponseTypeDef",
    {
        "Parents": Dict[str, str],
        "NextToken": str,
        "ParentLinks": List["ObjectIdentifierAndLinkNameTupleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListObjectPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListObjectPoliciesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListObjectPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListObjectPoliciesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)

class ListObjectPoliciesRequestRequestTypeDef(
    _RequiredListObjectPoliciesRequestRequestTypeDef,
    _OptionalListObjectPoliciesRequestRequestTypeDef,
):
    pass

ListObjectPoliciesResponseTypeDef = TypedDict(
    "ListObjectPoliciesResponseTypeDef",
    {
        "AttachedPolicyIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListOutgoingTypedLinksRequestRequestTypeDef = TypedDict(
    "_RequiredListOutgoingTypedLinksRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListOutgoingTypedLinksRequestRequestTypeDef = TypedDict(
    "_OptionalListOutgoingTypedLinksRequestRequestTypeDef",
    {
        "FilterAttributeRanges": List["TypedLinkAttributeRangeTypeDef"],
        "FilterTypedLink": "TypedLinkSchemaAndFacetNameTypeDef",
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)

class ListOutgoingTypedLinksRequestRequestTypeDef(
    _RequiredListOutgoingTypedLinksRequestRequestTypeDef,
    _OptionalListOutgoingTypedLinksRequestRequestTypeDef,
):
    pass

ListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "ListOutgoingTypedLinksResponseTypeDef",
    {
        "TypedLinkSpecifiers": List["TypedLinkSpecifierTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPolicyAttachmentsRequestRequestTypeDef = TypedDict(
    "_RequiredListPolicyAttachmentsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListPolicyAttachmentsRequestRequestTypeDef = TypedDict(
    "_OptionalListPolicyAttachmentsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)

class ListPolicyAttachmentsRequestRequestTypeDef(
    _RequiredListPolicyAttachmentsRequestRequestTypeDef,
    _OptionalListPolicyAttachmentsRequestRequestTypeDef,
):
    pass

ListPolicyAttachmentsResponseTypeDef = TypedDict(
    "ListPolicyAttachmentsResponseTypeDef",
    {
        "ObjectIdentifiers": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPublishedSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListPublishedSchemaArnsRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPublishedSchemaArnsResponseTypeDef = TypedDict(
    "ListPublishedSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTypedLinkFacetAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredListTypedLinkFacetAttributesRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
_OptionalListTypedLinkFacetAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalListTypedLinkFacetAttributesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTypedLinkFacetAttributesRequestRequestTypeDef(
    _RequiredListTypedLinkFacetAttributesRequestRequestTypeDef,
    _OptionalListTypedLinkFacetAttributesRequestRequestTypeDef,
):
    pass

ListTypedLinkFacetAttributesResponseTypeDef = TypedDict(
    "ListTypedLinkFacetAttributesResponseTypeDef",
    {
        "Attributes": List["TypedLinkAttributeDefinitionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTypedLinkFacetNamesRequestRequestTypeDef = TypedDict(
    "_RequiredListTypedLinkFacetNamesRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)
_OptionalListTypedLinkFacetNamesRequestRequestTypeDef = TypedDict(
    "_OptionalListTypedLinkFacetNamesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTypedLinkFacetNamesRequestRequestTypeDef(
    _RequiredListTypedLinkFacetNamesRequestRequestTypeDef,
    _OptionalListTypedLinkFacetNamesRequestRequestTypeDef,
):
    pass

ListTypedLinkFacetNamesResponseTypeDef = TypedDict(
    "ListTypedLinkFacetNamesResponseTypeDef",
    {
        "FacetNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLookupPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredLookupPolicyRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalLookupPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalLookupPolicyRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class LookupPolicyRequestRequestTypeDef(
    _RequiredLookupPolicyRequestRequestTypeDef, _OptionalLookupPolicyRequestRequestTypeDef
):
    pass

LookupPolicyResponseTypeDef = TypedDict(
    "LookupPolicyResponseTypeDef",
    {
        "PolicyToPathList": List["PolicyToPathTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ObjectAttributeActionTypeDef = TypedDict(
    "ObjectAttributeActionTypeDef",
    {
        "ObjectAttributeActionType": UpdateActionTypeType,
        "ObjectAttributeUpdateValue": "TypedAttributeValueTypeDef",
    },
    total=False,
)

ObjectAttributeRangeTypeDef = TypedDict(
    "ObjectAttributeRangeTypeDef",
    {
        "AttributeKey": "AttributeKeyTypeDef",
        "Range": "TypedAttributeValueRangeTypeDef",
    },
    total=False,
)

ObjectAttributeUpdateTypeDef = TypedDict(
    "ObjectAttributeUpdateTypeDef",
    {
        "ObjectAttributeKey": "AttributeKeyTypeDef",
        "ObjectAttributeAction": "ObjectAttributeActionTypeDef",
    },
    total=False,
)

ObjectIdentifierAndLinkNameTupleTypeDef = TypedDict(
    "ObjectIdentifierAndLinkNameTupleTypeDef",
    {
        "ObjectIdentifier": str,
        "LinkName": str,
    },
    total=False,
)

ObjectReferenceTypeDef = TypedDict(
    "ObjectReferenceTypeDef",
    {
        "Selector": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PathToObjectIdentifiersTypeDef = TypedDict(
    "PathToObjectIdentifiersTypeDef",
    {
        "Path": str,
        "ObjectIdentifiers": List[str],
    },
    total=False,
)

PolicyAttachmentTypeDef = TypedDict(
    "PolicyAttachmentTypeDef",
    {
        "PolicyId": str,
        "ObjectIdentifier": str,
        "PolicyType": str,
    },
    total=False,
)

PolicyToPathTypeDef = TypedDict(
    "PolicyToPathTypeDef",
    {
        "Path": str,
        "Policies": List["PolicyAttachmentTypeDef"],
    },
    total=False,
)

_RequiredPublishSchemaRequestRequestTypeDef = TypedDict(
    "_RequiredPublishSchemaRequestRequestTypeDef",
    {
        "DevelopmentSchemaArn": str,
        "Version": str,
    },
)
_OptionalPublishSchemaRequestRequestTypeDef = TypedDict(
    "_OptionalPublishSchemaRequestRequestTypeDef",
    {
        "MinorVersion": str,
        "Name": str,
    },
    total=False,
)

class PublishSchemaRequestRequestTypeDef(
    _RequiredPublishSchemaRequestRequestTypeDef, _OptionalPublishSchemaRequestRequestTypeDef
):
    pass

PublishSchemaResponseTypeDef = TypedDict(
    "PublishSchemaResponseTypeDef",
    {
        "PublishedSchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutSchemaFromJsonRequestRequestTypeDef = TypedDict(
    "PutSchemaFromJsonRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Document": str,
    },
)

PutSchemaFromJsonResponseTypeDef = TypedDict(
    "PutSchemaFromJsonResponseTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFacetFromObjectRequestRequestTypeDef = TypedDict(
    "RemoveFacetFromObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacet": "SchemaFacetTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Type": RuleTypeType,
        "Parameters": Dict[str, str],
    },
    total=False,
)

SchemaFacetTypeDef = TypedDict(
    "SchemaFacetTypeDef",
    {
        "SchemaArn": str,
        "FacetName": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredTypedAttributeValueRangeTypeDef = TypedDict(
    "_RequiredTypedAttributeValueRangeTypeDef",
    {
        "StartMode": RangeModeType,
        "EndMode": RangeModeType,
    },
)
_OptionalTypedAttributeValueRangeTypeDef = TypedDict(
    "_OptionalTypedAttributeValueRangeTypeDef",
    {
        "StartValue": "TypedAttributeValueTypeDef",
        "EndValue": "TypedAttributeValueTypeDef",
    },
    total=False,
)

class TypedAttributeValueRangeTypeDef(
    _RequiredTypedAttributeValueRangeTypeDef, _OptionalTypedAttributeValueRangeTypeDef
):
    pass

TypedAttributeValueTypeDef = TypedDict(
    "TypedAttributeValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": Union[bytes, IO[bytes], StreamingBody],
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": Union[datetime, str],
    },
    total=False,
)

_RequiredTypedLinkAttributeDefinitionTypeDef = TypedDict(
    "_RequiredTypedLinkAttributeDefinitionTypeDef",
    {
        "Name": str,
        "Type": FacetAttributeTypeType,
        "RequiredBehavior": RequiredAttributeBehaviorType,
    },
)
_OptionalTypedLinkAttributeDefinitionTypeDef = TypedDict(
    "_OptionalTypedLinkAttributeDefinitionTypeDef",
    {
        "DefaultValue": "TypedAttributeValueTypeDef",
        "IsImmutable": bool,
        "Rules": Dict[str, "RuleTypeDef"],
    },
    total=False,
)

class TypedLinkAttributeDefinitionTypeDef(
    _RequiredTypedLinkAttributeDefinitionTypeDef, _OptionalTypedLinkAttributeDefinitionTypeDef
):
    pass

_RequiredTypedLinkAttributeRangeTypeDef = TypedDict(
    "_RequiredTypedLinkAttributeRangeTypeDef",
    {
        "Range": "TypedAttributeValueRangeTypeDef",
    },
)
_OptionalTypedLinkAttributeRangeTypeDef = TypedDict(
    "_OptionalTypedLinkAttributeRangeTypeDef",
    {
        "AttributeName": str,
    },
    total=False,
)

class TypedLinkAttributeRangeTypeDef(
    _RequiredTypedLinkAttributeRangeTypeDef, _OptionalTypedLinkAttributeRangeTypeDef
):
    pass

TypedLinkFacetAttributeUpdateTypeDef = TypedDict(
    "TypedLinkFacetAttributeUpdateTypeDef",
    {
        "Attribute": "TypedLinkAttributeDefinitionTypeDef",
        "Action": UpdateActionTypeType,
    },
)

TypedLinkFacetTypeDef = TypedDict(
    "TypedLinkFacetTypeDef",
    {
        "Name": str,
        "Attributes": List["TypedLinkAttributeDefinitionTypeDef"],
        "IdentityAttributeOrder": List[str],
    },
)

TypedLinkSchemaAndFacetNameTypeDef = TypedDict(
    "TypedLinkSchemaAndFacetNameTypeDef",
    {
        "SchemaArn": str,
        "TypedLinkName": str,
    },
)

TypedLinkSpecifierTypeDef = TypedDict(
    "TypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": "TypedLinkSchemaAndFacetNameTypeDef",
        "SourceObjectReference": "ObjectReferenceTypeDef",
        "TargetObjectReference": "ObjectReferenceTypeDef",
        "IdentityAttributeValues": List["AttributeNameAndValueTypeDef"],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateFacetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
_OptionalUpdateFacetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFacetRequestRequestTypeDef",
    {
        "AttributeUpdates": List["FacetAttributeUpdateTypeDef"],
        "ObjectType": ObjectTypeType,
    },
    total=False,
)

class UpdateFacetRequestRequestTypeDef(
    _RequiredUpdateFacetRequestRequestTypeDef, _OptionalUpdateFacetRequestRequestTypeDef
):
    pass

UpdateLinkAttributesRequestRequestTypeDef = TypedDict(
    "UpdateLinkAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
        "AttributeUpdates": List["LinkAttributeUpdateTypeDef"],
    },
)

UpdateObjectAttributesRequestRequestTypeDef = TypedDict(
    "UpdateObjectAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
        "AttributeUpdates": List["ObjectAttributeUpdateTypeDef"],
    },
)

UpdateObjectAttributesResponseTypeDef = TypedDict(
    "UpdateObjectAttributesResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSchemaRequestRequestTypeDef = TypedDict(
    "UpdateSchemaRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

UpdateSchemaResponseTypeDef = TypedDict(
    "UpdateSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTypedLinkFacetRequestRequestTypeDef = TypedDict(
    "UpdateTypedLinkFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "AttributeUpdates": List["TypedLinkFacetAttributeUpdateTypeDef"],
        "IdentityAttributeOrder": List[str],
    },
)

_RequiredUpgradeAppliedSchemaRequestRequestTypeDef = TypedDict(
    "_RequiredUpgradeAppliedSchemaRequestRequestTypeDef",
    {
        "PublishedSchemaArn": str,
        "DirectoryArn": str,
    },
)
_OptionalUpgradeAppliedSchemaRequestRequestTypeDef = TypedDict(
    "_OptionalUpgradeAppliedSchemaRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class UpgradeAppliedSchemaRequestRequestTypeDef(
    _RequiredUpgradeAppliedSchemaRequestRequestTypeDef,
    _OptionalUpgradeAppliedSchemaRequestRequestTypeDef,
):
    pass

UpgradeAppliedSchemaResponseTypeDef = TypedDict(
    "UpgradeAppliedSchemaResponseTypeDef",
    {
        "UpgradedSchemaArn": str,
        "DirectoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpgradePublishedSchemaRequestRequestTypeDef = TypedDict(
    "_RequiredUpgradePublishedSchemaRequestRequestTypeDef",
    {
        "DevelopmentSchemaArn": str,
        "PublishedSchemaArn": str,
        "MinorVersion": str,
    },
)
_OptionalUpgradePublishedSchemaRequestRequestTypeDef = TypedDict(
    "_OptionalUpgradePublishedSchemaRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class UpgradePublishedSchemaRequestRequestTypeDef(
    _RequiredUpgradePublishedSchemaRequestRequestTypeDef,
    _OptionalUpgradePublishedSchemaRequestRequestTypeDef,
):
    pass

UpgradePublishedSchemaResponseTypeDef = TypedDict(
    "UpgradePublishedSchemaResponseTypeDef",
    {
        "UpgradedSchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
