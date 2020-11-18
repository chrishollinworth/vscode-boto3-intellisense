"""
Main interface for clouddirectory service type definitions.

Usage::

    ```python
    from mypy_boto3_clouddirectory.type_defs import AttributeKeyAndValueTypeDef

    data: AttributeKeyAndValueTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
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
    "BatchReadSuccessfulResponseTypeDef",
    "BatchRemoveFacetFromObjectTypeDef",
    "BatchUpdateLinkAttributesTypeDef",
    "BatchUpdateObjectAttributesResponseTypeDef",
    "BatchUpdateObjectAttributesTypeDef",
    "BatchWriteOperationResponseTypeDef",
    "DirectoryTypeDef",
    "FacetAttributeDefinitionTypeDef",
    "FacetAttributeReferenceTypeDef",
    "FacetAttributeTypeDef",
    "FacetTypeDef",
    "IndexAttachmentTypeDef",
    "LinkAttributeActionTypeDef",
    "LinkAttributeUpdateTypeDef",
    "ObjectAttributeActionTypeDef",
    "ObjectAttributeRangeTypeDef",
    "ObjectAttributeUpdateTypeDef",
    "ObjectIdentifierAndLinkNameTupleTypeDef",
    "ObjectReferenceTypeDef",
    "PathToObjectIdentifiersTypeDef",
    "PolicyAttachmentTypeDef",
    "PolicyToPathTypeDef",
    "RuleTypeDef",
    "SchemaFacetTypeDef",
    "TagTypeDef",
    "TypedAttributeValueRangeTypeDef",
    "TypedAttributeValueTypeDef",
    "TypedLinkAttributeDefinitionTypeDef",
    "TypedLinkAttributeRangeTypeDef",
    "TypedLinkSchemaAndFacetNameTypeDef",
    "TypedLinkSpecifierTypeDef",
    "ApplySchemaResponseTypeDef",
    "AttachObjectResponseTypeDef",
    "AttachToIndexResponseTypeDef",
    "AttachTypedLinkResponseTypeDef",
    "BatchReadOperationTypeDef",
    "BatchReadResponseTypeDef",
    "BatchWriteOperationTypeDef",
    "BatchWriteResponseTypeDef",
    "CreateDirectoryResponseTypeDef",
    "CreateIndexResponseTypeDef",
    "CreateObjectResponseTypeDef",
    "CreateSchemaResponseTypeDef",
    "DeleteDirectoryResponseTypeDef",
    "DeleteSchemaResponseTypeDef",
    "DetachFromIndexResponseTypeDef",
    "DetachObjectResponseTypeDef",
    "DisableDirectoryResponseTypeDef",
    "EnableDirectoryResponseTypeDef",
    "FacetAttributeUpdateTypeDef",
    "GetAppliedSchemaVersionResponseTypeDef",
    "GetDirectoryResponseTypeDef",
    "GetFacetResponseTypeDef",
    "GetLinkAttributesResponseTypeDef",
    "GetObjectAttributesResponseTypeDef",
    "GetObjectInformationResponseTypeDef",
    "GetSchemaAsJsonResponseTypeDef",
    "GetTypedLinkFacetInformationResponseTypeDef",
    "ListAppliedSchemaArnsResponseTypeDef",
    "ListAttachedIndicesResponseTypeDef",
    "ListDevelopmentSchemaArnsResponseTypeDef",
    "ListDirectoriesResponseTypeDef",
    "ListFacetAttributesResponseTypeDef",
    "ListFacetNamesResponseTypeDef",
    "ListIncomingTypedLinksResponseTypeDef",
    "ListIndexResponseTypeDef",
    "ListManagedSchemaArnsResponseTypeDef",
    "ListObjectAttributesResponseTypeDef",
    "ListObjectChildrenResponseTypeDef",
    "ListObjectParentPathsResponseTypeDef",
    "ListObjectParentsResponseTypeDef",
    "ListObjectPoliciesResponseTypeDef",
    "ListOutgoingTypedLinksResponseTypeDef",
    "ListPolicyAttachmentsResponseTypeDef",
    "ListPublishedSchemaArnsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTypedLinkFacetAttributesResponseTypeDef",
    "ListTypedLinkFacetNamesResponseTypeDef",
    "LookupPolicyResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PublishSchemaResponseTypeDef",
    "PutSchemaFromJsonResponseTypeDef",
    "TypedLinkFacetAttributeUpdateTypeDef",
    "TypedLinkFacetTypeDef",
    "UpdateObjectAttributesResponseTypeDef",
    "UpdateSchemaResponseTypeDef",
    "UpgradeAppliedSchemaResponseTypeDef",
    "UpgradePublishedSchemaResponseTypeDef",
)

AttributeKeyAndValueTypeDef = TypedDict(
    "AttributeKeyAndValueTypeDef",
    {"Key": "AttributeKeyTypeDef", "Value": "TypedAttributeValueTypeDef"},
)

AttributeKeyTypeDef = TypedDict(
    "AttributeKeyTypeDef", {"SchemaArn": str, "FacetName": str, "Name": str}
)

AttributeNameAndValueTypeDef = TypedDict(
    "AttributeNameAndValueTypeDef", {"AttributeName": str, "Value": "TypedAttributeValueTypeDef"}
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
    "BatchAttachObjectResponseTypeDef", {"attachedObjectIdentifier": str}, total=False
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
    {"PolicyReference": "ObjectReferenceTypeDef", "ObjectReference": "ObjectReferenceTypeDef"},
)

BatchAttachToIndexResponseTypeDef = TypedDict(
    "BatchAttachToIndexResponseTypeDef", {"AttachedObjectIdentifier": str}, total=False
)

BatchAttachToIndexTypeDef = TypedDict(
    "BatchAttachToIndexTypeDef",
    {"IndexReference": "ObjectReferenceTypeDef", "TargetReference": "ObjectReferenceTypeDef"},
)

BatchAttachTypedLinkResponseTypeDef = TypedDict(
    "BatchAttachTypedLinkResponseTypeDef",
    {"TypedLinkSpecifier": "TypedLinkSpecifierTypeDef"},
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
    "BatchCreateIndexResponseTypeDef", {"ObjectIdentifier": str}, total=False
)

_RequiredBatchCreateIndexTypeDef = TypedDict(
    "_RequiredBatchCreateIndexTypeDef",
    {"OrderedIndexedAttributeList": List["AttributeKeyTypeDef"], "IsUnique": bool},
)
_OptionalBatchCreateIndexTypeDef = TypedDict(
    "_OptionalBatchCreateIndexTypeDef",
    {"ParentReference": "ObjectReferenceTypeDef", "LinkName": str, "BatchReferenceName": str},
    total=False,
)


class BatchCreateIndexTypeDef(_RequiredBatchCreateIndexTypeDef, _OptionalBatchCreateIndexTypeDef):
    pass


BatchCreateObjectResponseTypeDef = TypedDict(
    "BatchCreateObjectResponseTypeDef", {"ObjectIdentifier": str}, total=False
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
    {"ParentReference": "ObjectReferenceTypeDef", "LinkName": str, "BatchReferenceName": str},
    total=False,
)


class BatchCreateObjectTypeDef(
    _RequiredBatchCreateObjectTypeDef, _OptionalBatchCreateObjectTypeDef
):
    pass


BatchDeleteObjectTypeDef = TypedDict(
    "BatchDeleteObjectTypeDef", {"ObjectReference": "ObjectReferenceTypeDef"}
)

BatchDetachFromIndexResponseTypeDef = TypedDict(
    "BatchDetachFromIndexResponseTypeDef", {"DetachedObjectIdentifier": str}, total=False
)

BatchDetachFromIndexTypeDef = TypedDict(
    "BatchDetachFromIndexTypeDef",
    {"IndexReference": "ObjectReferenceTypeDef", "TargetReference": "ObjectReferenceTypeDef"},
)

BatchDetachObjectResponseTypeDef = TypedDict(
    "BatchDetachObjectResponseTypeDef", {"detachedObjectIdentifier": str}, total=False
)

_RequiredBatchDetachObjectTypeDef = TypedDict(
    "_RequiredBatchDetachObjectTypeDef",
    {"ParentReference": "ObjectReferenceTypeDef", "LinkName": str},
)
_OptionalBatchDetachObjectTypeDef = TypedDict(
    "_OptionalBatchDetachObjectTypeDef", {"BatchReferenceName": str}, total=False
)


class BatchDetachObjectTypeDef(
    _RequiredBatchDetachObjectTypeDef, _OptionalBatchDetachObjectTypeDef
):
    pass


BatchDetachPolicyTypeDef = TypedDict(
    "BatchDetachPolicyTypeDef",
    {"PolicyReference": "ObjectReferenceTypeDef", "ObjectReference": "ObjectReferenceTypeDef"},
)

BatchDetachTypedLinkTypeDef = TypedDict(
    "BatchDetachTypedLinkTypeDef", {"TypedLinkSpecifier": "TypedLinkSpecifierTypeDef"}
)

BatchGetLinkAttributesResponseTypeDef = TypedDict(
    "BatchGetLinkAttributesResponseTypeDef",
    {"Attributes": List["AttributeKeyAndValueTypeDef"]},
    total=False,
)

BatchGetLinkAttributesTypeDef = TypedDict(
    "BatchGetLinkAttributesTypeDef",
    {"TypedLinkSpecifier": "TypedLinkSpecifierTypeDef", "AttributeNames": List[str]},
)

BatchGetObjectAttributesResponseTypeDef = TypedDict(
    "BatchGetObjectAttributesResponseTypeDef",
    {"Attributes": List["AttributeKeyAndValueTypeDef"]},
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
    {"SchemaFacets": List["SchemaFacetTypeDef"], "ObjectIdentifier": str},
    total=False,
)

BatchGetObjectInformationTypeDef = TypedDict(
    "BatchGetObjectInformationTypeDef", {"ObjectReference": "ObjectReferenceTypeDef"}
)

BatchListAttachedIndicesResponseTypeDef = TypedDict(
    "BatchListAttachedIndicesResponseTypeDef",
    {"IndexAttachments": List["IndexAttachmentTypeDef"], "NextToken": str},
    total=False,
)

_RequiredBatchListAttachedIndicesTypeDef = TypedDict(
    "_RequiredBatchListAttachedIndicesTypeDef", {"TargetReference": "ObjectReferenceTypeDef"}
)
_OptionalBatchListAttachedIndicesTypeDef = TypedDict(
    "_OptionalBatchListAttachedIndicesTypeDef", {"NextToken": str, "MaxResults": int}, total=False
)


class BatchListAttachedIndicesTypeDef(
    _RequiredBatchListAttachedIndicesTypeDef, _OptionalBatchListAttachedIndicesTypeDef
):
    pass


BatchListIncomingTypedLinksResponseTypeDef = TypedDict(
    "BatchListIncomingTypedLinksResponseTypeDef",
    {"LinkSpecifiers": List["TypedLinkSpecifierTypeDef"], "NextToken": str},
    total=False,
)

_RequiredBatchListIncomingTypedLinksTypeDef = TypedDict(
    "_RequiredBatchListIncomingTypedLinksTypeDef", {"ObjectReference": "ObjectReferenceTypeDef"}
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
    {"IndexAttachments": List["IndexAttachmentTypeDef"], "NextToken": str},
    total=False,
)

_RequiredBatchListIndexTypeDef = TypedDict(
    "_RequiredBatchListIndexTypeDef", {"IndexReference": "ObjectReferenceTypeDef"}
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
    {"Attributes": List["AttributeKeyAndValueTypeDef"], "NextToken": str},
    total=False,
)

_RequiredBatchListObjectAttributesTypeDef = TypedDict(
    "_RequiredBatchListObjectAttributesTypeDef", {"ObjectReference": "ObjectReferenceTypeDef"}
)
_OptionalBatchListObjectAttributesTypeDef = TypedDict(
    "_OptionalBatchListObjectAttributesTypeDef",
    {"NextToken": str, "MaxResults": int, "FacetFilter": "SchemaFacetTypeDef"},
    total=False,
)


class BatchListObjectAttributesTypeDef(
    _RequiredBatchListObjectAttributesTypeDef, _OptionalBatchListObjectAttributesTypeDef
):
    pass


BatchListObjectChildrenResponseTypeDef = TypedDict(
    "BatchListObjectChildrenResponseTypeDef",
    {"Children": Dict[str, str], "NextToken": str},
    total=False,
)

_RequiredBatchListObjectChildrenTypeDef = TypedDict(
    "_RequiredBatchListObjectChildrenTypeDef", {"ObjectReference": "ObjectReferenceTypeDef"}
)
_OptionalBatchListObjectChildrenTypeDef = TypedDict(
    "_OptionalBatchListObjectChildrenTypeDef", {"NextToken": str, "MaxResults": int}, total=False
)


class BatchListObjectChildrenTypeDef(
    _RequiredBatchListObjectChildrenTypeDef, _OptionalBatchListObjectChildrenTypeDef
):
    pass


BatchListObjectParentPathsResponseTypeDef = TypedDict(
    "BatchListObjectParentPathsResponseTypeDef",
    {"PathToObjectIdentifiersList": List["PathToObjectIdentifiersTypeDef"], "NextToken": str},
    total=False,
)

_RequiredBatchListObjectParentPathsTypeDef = TypedDict(
    "_RequiredBatchListObjectParentPathsTypeDef", {"ObjectReference": "ObjectReferenceTypeDef"}
)
_OptionalBatchListObjectParentPathsTypeDef = TypedDict(
    "_OptionalBatchListObjectParentPathsTypeDef", {"NextToken": str, "MaxResults": int}, total=False
)


class BatchListObjectParentPathsTypeDef(
    _RequiredBatchListObjectParentPathsTypeDef, _OptionalBatchListObjectParentPathsTypeDef
):
    pass


BatchListObjectParentsResponseTypeDef = TypedDict(
    "BatchListObjectParentsResponseTypeDef",
    {"ParentLinks": List["ObjectIdentifierAndLinkNameTupleTypeDef"], "NextToken": str},
    total=False,
)

_RequiredBatchListObjectParentsTypeDef = TypedDict(
    "_RequiredBatchListObjectParentsTypeDef", {"ObjectReference": "ObjectReferenceTypeDef"}
)
_OptionalBatchListObjectParentsTypeDef = TypedDict(
    "_OptionalBatchListObjectParentsTypeDef", {"NextToken": str, "MaxResults": int}, total=False
)


class BatchListObjectParentsTypeDef(
    _RequiredBatchListObjectParentsTypeDef, _OptionalBatchListObjectParentsTypeDef
):
    pass


BatchListObjectPoliciesResponseTypeDef = TypedDict(
    "BatchListObjectPoliciesResponseTypeDef",
    {"AttachedPolicyIds": List[str], "NextToken": str},
    total=False,
)

_RequiredBatchListObjectPoliciesTypeDef = TypedDict(
    "_RequiredBatchListObjectPoliciesTypeDef", {"ObjectReference": "ObjectReferenceTypeDef"}
)
_OptionalBatchListObjectPoliciesTypeDef = TypedDict(
    "_OptionalBatchListObjectPoliciesTypeDef", {"NextToken": str, "MaxResults": int}, total=False
)


class BatchListObjectPoliciesTypeDef(
    _RequiredBatchListObjectPoliciesTypeDef, _OptionalBatchListObjectPoliciesTypeDef
):
    pass


BatchListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "BatchListOutgoingTypedLinksResponseTypeDef",
    {"TypedLinkSpecifiers": List["TypedLinkSpecifierTypeDef"], "NextToken": str},
    total=False,
)

_RequiredBatchListOutgoingTypedLinksTypeDef = TypedDict(
    "_RequiredBatchListOutgoingTypedLinksTypeDef", {"ObjectReference": "ObjectReferenceTypeDef"}
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
    {"ObjectIdentifiers": List[str], "NextToken": str},
    total=False,
)

_RequiredBatchListPolicyAttachmentsTypeDef = TypedDict(
    "_RequiredBatchListPolicyAttachmentsTypeDef", {"PolicyReference": "ObjectReferenceTypeDef"}
)
_OptionalBatchListPolicyAttachmentsTypeDef = TypedDict(
    "_OptionalBatchListPolicyAttachmentsTypeDef", {"NextToken": str, "MaxResults": int}, total=False
)


class BatchListPolicyAttachmentsTypeDef(
    _RequiredBatchListPolicyAttachmentsTypeDef, _OptionalBatchListPolicyAttachmentsTypeDef
):
    pass


BatchLookupPolicyResponseTypeDef = TypedDict(
    "BatchLookupPolicyResponseTypeDef",
    {"PolicyToPathList": List["PolicyToPathTypeDef"], "NextToken": str},
    total=False,
)

_RequiredBatchLookupPolicyTypeDef = TypedDict(
    "_RequiredBatchLookupPolicyTypeDef", {"ObjectReference": "ObjectReferenceTypeDef"}
)
_OptionalBatchLookupPolicyTypeDef = TypedDict(
    "_OptionalBatchLookupPolicyTypeDef", {"NextToken": str, "MaxResults": int}, total=False
)


class BatchLookupPolicyTypeDef(
    _RequiredBatchLookupPolicyTypeDef, _OptionalBatchLookupPolicyTypeDef
):
    pass


BatchReadExceptionTypeDef = TypedDict(
    "BatchReadExceptionTypeDef",
    {
        "Type": Literal[
            "ValidationException",
            "InvalidArnException",
            "ResourceNotFoundException",
            "InvalidNextTokenException",
            "AccessDeniedException",
            "NotNodeException",
            "FacetValidationException",
            "CannotListParentOfRootException",
            "NotIndexException",
            "NotPolicyException",
            "DirectoryNotEnabledException",
            "LimitExceededException",
            "InternalServiceException",
        ],
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
    {"SchemaFacet": "SchemaFacetTypeDef", "ObjectReference": "ObjectReferenceTypeDef"},
)

BatchUpdateLinkAttributesTypeDef = TypedDict(
    "BatchUpdateLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
        "AttributeUpdates": List["LinkAttributeUpdateTypeDef"],
    },
)

BatchUpdateObjectAttributesResponseTypeDef = TypedDict(
    "BatchUpdateObjectAttributesResponseTypeDef", {"ObjectIdentifier": str}, total=False
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

DirectoryTypeDef = TypedDict(
    "DirectoryTypeDef",
    {
        "Name": str,
        "DirectoryArn": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "CreationDateTime": datetime,
    },
    total=False,
)

_RequiredFacetAttributeDefinitionTypeDef = TypedDict(
    "_RequiredFacetAttributeDefinitionTypeDef",
    {"Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"]},
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
    "FacetAttributeReferenceTypeDef", {"TargetFacetName": str, "TargetAttributeName": str}
)

_RequiredFacetAttributeTypeDef = TypedDict("_RequiredFacetAttributeTypeDef", {"Name": str})
_OptionalFacetAttributeTypeDef = TypedDict(
    "_OptionalFacetAttributeTypeDef",
    {
        "AttributeDefinition": "FacetAttributeDefinitionTypeDef",
        "AttributeReference": "FacetAttributeReferenceTypeDef",
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
    total=False,
)


class FacetAttributeTypeDef(_RequiredFacetAttributeTypeDef, _OptionalFacetAttributeTypeDef):
    pass


FacetTypeDef = TypedDict(
    "FacetTypeDef",
    {
        "Name": str,
        "ObjectType": Literal["NODE", "LEAF_NODE", "POLICY", "INDEX"],
        "FacetStyle": Literal["STATIC", "DYNAMIC"],
    },
    total=False,
)

IndexAttachmentTypeDef = TypedDict(
    "IndexAttachmentTypeDef",
    {"IndexedAttributes": List["AttributeKeyAndValueTypeDef"], "ObjectIdentifier": str},
    total=False,
)

LinkAttributeActionTypeDef = TypedDict(
    "LinkAttributeActionTypeDef",
    {
        "AttributeActionType": Literal["CREATE_OR_UPDATE", "DELETE"],
        "AttributeUpdateValue": "TypedAttributeValueTypeDef",
    },
    total=False,
)

LinkAttributeUpdateTypeDef = TypedDict(
    "LinkAttributeUpdateTypeDef",
    {"AttributeKey": "AttributeKeyTypeDef", "AttributeAction": "LinkAttributeActionTypeDef"},
    total=False,
)

ObjectAttributeActionTypeDef = TypedDict(
    "ObjectAttributeActionTypeDef",
    {
        "ObjectAttributeActionType": Literal["CREATE_OR_UPDATE", "DELETE"],
        "ObjectAttributeUpdateValue": "TypedAttributeValueTypeDef",
    },
    total=False,
)

ObjectAttributeRangeTypeDef = TypedDict(
    "ObjectAttributeRangeTypeDef",
    {"AttributeKey": "AttributeKeyTypeDef", "Range": "TypedAttributeValueRangeTypeDef"},
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
    {"ObjectIdentifier": str, "LinkName": str},
    total=False,
)

ObjectReferenceTypeDef = TypedDict("ObjectReferenceTypeDef", {"Selector": str}, total=False)

PathToObjectIdentifiersTypeDef = TypedDict(
    "PathToObjectIdentifiersTypeDef", {"Path": str, "ObjectIdentifiers": List[str]}, total=False
)

PolicyAttachmentTypeDef = TypedDict(
    "PolicyAttachmentTypeDef",
    {"PolicyId": str, "ObjectIdentifier": str, "PolicyType": str},
    total=False,
)

PolicyToPathTypeDef = TypedDict(
    "PolicyToPathTypeDef", {"Path": str, "Policies": List["PolicyAttachmentTypeDef"]}, total=False
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Type": Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"],
        "Parameters": Dict[str, str],
    },
    total=False,
)

SchemaFacetTypeDef = TypedDict(
    "SchemaFacetTypeDef", {"SchemaArn": str, "FacetName": str}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

_RequiredTypedAttributeValueRangeTypeDef = TypedDict(
    "_RequiredTypedAttributeValueRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
    },
)
_OptionalTypedAttributeValueRangeTypeDef = TypedDict(
    "_OptionalTypedAttributeValueRangeTypeDef",
    {"StartValue": "TypedAttributeValueTypeDef", "EndValue": "TypedAttributeValueTypeDef"},
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
        "BinaryValue": Union[bytes, IO[bytes]],
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

_RequiredTypedLinkAttributeDefinitionTypeDef = TypedDict(
    "_RequiredTypedLinkAttributeDefinitionTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"],
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
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
    "_RequiredTypedLinkAttributeRangeTypeDef", {"Range": "TypedAttributeValueRangeTypeDef"}
)
_OptionalTypedLinkAttributeRangeTypeDef = TypedDict(
    "_OptionalTypedLinkAttributeRangeTypeDef", {"AttributeName": str}, total=False
)


class TypedLinkAttributeRangeTypeDef(
    _RequiredTypedLinkAttributeRangeTypeDef, _OptionalTypedLinkAttributeRangeTypeDef
):
    pass


TypedLinkSchemaAndFacetNameTypeDef = TypedDict(
    "TypedLinkSchemaAndFacetNameTypeDef", {"SchemaArn": str, "TypedLinkName": str}
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

ApplySchemaResponseTypeDef = TypedDict(
    "ApplySchemaResponseTypeDef", {"AppliedSchemaArn": str, "DirectoryArn": str}, total=False
)

AttachObjectResponseTypeDef = TypedDict(
    "AttachObjectResponseTypeDef", {"AttachedObjectIdentifier": str}, total=False
)

AttachToIndexResponseTypeDef = TypedDict(
    "AttachToIndexResponseTypeDef", {"AttachedObjectIdentifier": str}, total=False
)

AttachTypedLinkResponseTypeDef = TypedDict(
    "AttachTypedLinkResponseTypeDef",
    {"TypedLinkSpecifier": "TypedLinkSpecifierTypeDef"},
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

BatchReadResponseTypeDef = TypedDict(
    "BatchReadResponseTypeDef",
    {"Responses": List["BatchReadOperationResponseTypeDef"]},
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

BatchWriteResponseTypeDef = TypedDict(
    "BatchWriteResponseTypeDef",
    {"Responses": List["BatchWriteOperationResponseTypeDef"]},
    total=False,
)

CreateDirectoryResponseTypeDef = TypedDict(
    "CreateDirectoryResponseTypeDef",
    {"DirectoryArn": str, "Name": str, "ObjectIdentifier": str, "AppliedSchemaArn": str},
)

CreateIndexResponseTypeDef = TypedDict(
    "CreateIndexResponseTypeDef", {"ObjectIdentifier": str}, total=False
)

CreateObjectResponseTypeDef = TypedDict(
    "CreateObjectResponseTypeDef", {"ObjectIdentifier": str}, total=False
)

CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef", {"SchemaArn": str}, total=False
)

DeleteDirectoryResponseTypeDef = TypedDict("DeleteDirectoryResponseTypeDef", {"DirectoryArn": str})

DeleteSchemaResponseTypeDef = TypedDict(
    "DeleteSchemaResponseTypeDef", {"SchemaArn": str}, total=False
)

DetachFromIndexResponseTypeDef = TypedDict(
    "DetachFromIndexResponseTypeDef", {"DetachedObjectIdentifier": str}, total=False
)

DetachObjectResponseTypeDef = TypedDict(
    "DetachObjectResponseTypeDef", {"DetachedObjectIdentifier": str}, total=False
)

DisableDirectoryResponseTypeDef = TypedDict(
    "DisableDirectoryResponseTypeDef", {"DirectoryArn": str}
)

EnableDirectoryResponseTypeDef = TypedDict("EnableDirectoryResponseTypeDef", {"DirectoryArn": str})

FacetAttributeUpdateTypeDef = TypedDict(
    "FacetAttributeUpdateTypeDef",
    {"Attribute": "FacetAttributeTypeDef", "Action": Literal["CREATE_OR_UPDATE", "DELETE"]},
    total=False,
)

GetAppliedSchemaVersionResponseTypeDef = TypedDict(
    "GetAppliedSchemaVersionResponseTypeDef", {"AppliedSchemaArn": str}, total=False
)

GetDirectoryResponseTypeDef = TypedDict(
    "GetDirectoryResponseTypeDef", {"Directory": "DirectoryTypeDef"}
)

GetFacetResponseTypeDef = TypedDict(
    "GetFacetResponseTypeDef", {"Facet": "FacetTypeDef"}, total=False
)

GetLinkAttributesResponseTypeDef = TypedDict(
    "GetLinkAttributesResponseTypeDef",
    {"Attributes": List["AttributeKeyAndValueTypeDef"]},
    total=False,
)

GetObjectAttributesResponseTypeDef = TypedDict(
    "GetObjectAttributesResponseTypeDef",
    {"Attributes": List["AttributeKeyAndValueTypeDef"]},
    total=False,
)

GetObjectInformationResponseTypeDef = TypedDict(
    "GetObjectInformationResponseTypeDef",
    {"SchemaFacets": List["SchemaFacetTypeDef"], "ObjectIdentifier": str},
    total=False,
)

GetSchemaAsJsonResponseTypeDef = TypedDict(
    "GetSchemaAsJsonResponseTypeDef", {"Name": str, "Document": str}, total=False
)

GetTypedLinkFacetInformationResponseTypeDef = TypedDict(
    "GetTypedLinkFacetInformationResponseTypeDef",
    {"IdentityAttributeOrder": List[str]},
    total=False,
)

ListAppliedSchemaArnsResponseTypeDef = TypedDict(
    "ListAppliedSchemaArnsResponseTypeDef", {"SchemaArns": List[str], "NextToken": str}, total=False
)

ListAttachedIndicesResponseTypeDef = TypedDict(
    "ListAttachedIndicesResponseTypeDef",
    {"IndexAttachments": List["IndexAttachmentTypeDef"], "NextToken": str},
    total=False,
)

ListDevelopmentSchemaArnsResponseTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsResponseTypeDef",
    {"SchemaArns": List[str], "NextToken": str},
    total=False,
)

_RequiredListDirectoriesResponseTypeDef = TypedDict(
    "_RequiredListDirectoriesResponseTypeDef", {"Directories": List["DirectoryTypeDef"]}
)
_OptionalListDirectoriesResponseTypeDef = TypedDict(
    "_OptionalListDirectoriesResponseTypeDef", {"NextToken": str}, total=False
)


class ListDirectoriesResponseTypeDef(
    _RequiredListDirectoriesResponseTypeDef, _OptionalListDirectoriesResponseTypeDef
):
    pass


ListFacetAttributesResponseTypeDef = TypedDict(
    "ListFacetAttributesResponseTypeDef",
    {"Attributes": List["FacetAttributeTypeDef"], "NextToken": str},
    total=False,
)

ListFacetNamesResponseTypeDef = TypedDict(
    "ListFacetNamesResponseTypeDef", {"FacetNames": List[str], "NextToken": str}, total=False
)

ListIncomingTypedLinksResponseTypeDef = TypedDict(
    "ListIncomingTypedLinksResponseTypeDef",
    {"LinkSpecifiers": List["TypedLinkSpecifierTypeDef"], "NextToken": str},
    total=False,
)

ListIndexResponseTypeDef = TypedDict(
    "ListIndexResponseTypeDef",
    {"IndexAttachments": List["IndexAttachmentTypeDef"], "NextToken": str},
    total=False,
)

ListManagedSchemaArnsResponseTypeDef = TypedDict(
    "ListManagedSchemaArnsResponseTypeDef", {"SchemaArns": List[str], "NextToken": str}, total=False
)

ListObjectAttributesResponseTypeDef = TypedDict(
    "ListObjectAttributesResponseTypeDef",
    {"Attributes": List["AttributeKeyAndValueTypeDef"], "NextToken": str},
    total=False,
)

ListObjectChildrenResponseTypeDef = TypedDict(
    "ListObjectChildrenResponseTypeDef", {"Children": Dict[str, str], "NextToken": str}, total=False
)

ListObjectParentPathsResponseTypeDef = TypedDict(
    "ListObjectParentPathsResponseTypeDef",
    {"PathToObjectIdentifiersList": List["PathToObjectIdentifiersTypeDef"], "NextToken": str},
    total=False,
)

ListObjectParentsResponseTypeDef = TypedDict(
    "ListObjectParentsResponseTypeDef",
    {
        "Parents": Dict[str, str],
        "NextToken": str,
        "ParentLinks": List["ObjectIdentifierAndLinkNameTupleTypeDef"],
    },
    total=False,
)

ListObjectPoliciesResponseTypeDef = TypedDict(
    "ListObjectPoliciesResponseTypeDef",
    {"AttachedPolicyIds": List[str], "NextToken": str},
    total=False,
)

ListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "ListOutgoingTypedLinksResponseTypeDef",
    {"TypedLinkSpecifiers": List["TypedLinkSpecifierTypeDef"], "NextToken": str},
    total=False,
)

ListPolicyAttachmentsResponseTypeDef = TypedDict(
    "ListPolicyAttachmentsResponseTypeDef",
    {"ObjectIdentifiers": List[str], "NextToken": str},
    total=False,
)

ListPublishedSchemaArnsResponseTypeDef = TypedDict(
    "ListPublishedSchemaArnsResponseTypeDef",
    {"SchemaArns": List[str], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {"Tags": List["TagTypeDef"], "NextToken": str},
    total=False,
)

ListTypedLinkFacetAttributesResponseTypeDef = TypedDict(
    "ListTypedLinkFacetAttributesResponseTypeDef",
    {"Attributes": List["TypedLinkAttributeDefinitionTypeDef"], "NextToken": str},
    total=False,
)

ListTypedLinkFacetNamesResponseTypeDef = TypedDict(
    "ListTypedLinkFacetNamesResponseTypeDef",
    {"FacetNames": List[str], "NextToken": str},
    total=False,
)

LookupPolicyResponseTypeDef = TypedDict(
    "LookupPolicyResponseTypeDef",
    {"PolicyToPathList": List["PolicyToPathTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PublishSchemaResponseTypeDef = TypedDict(
    "PublishSchemaResponseTypeDef", {"PublishedSchemaArn": str}, total=False
)

PutSchemaFromJsonResponseTypeDef = TypedDict(
    "PutSchemaFromJsonResponseTypeDef", {"Arn": str}, total=False
)

TypedLinkFacetAttributeUpdateTypeDef = TypedDict(
    "TypedLinkFacetAttributeUpdateTypeDef",
    {
        "Attribute": "TypedLinkAttributeDefinitionTypeDef",
        "Action": Literal["CREATE_OR_UPDATE", "DELETE"],
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

UpdateObjectAttributesResponseTypeDef = TypedDict(
    "UpdateObjectAttributesResponseTypeDef", {"ObjectIdentifier": str}, total=False
)

UpdateSchemaResponseTypeDef = TypedDict(
    "UpdateSchemaResponseTypeDef", {"SchemaArn": str}, total=False
)

UpgradeAppliedSchemaResponseTypeDef = TypedDict(
    "UpgradeAppliedSchemaResponseTypeDef",
    {"UpgradedSchemaArn": str, "DirectoryArn": str},
    total=False,
)

UpgradePublishedSchemaResponseTypeDef = TypedDict(
    "UpgradePublishedSchemaResponseTypeDef", {"UpgradedSchemaArn": str}, total=False
)
