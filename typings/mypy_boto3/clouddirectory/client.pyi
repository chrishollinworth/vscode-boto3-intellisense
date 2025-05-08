"""
Type annotations for clouddirectory service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_clouddirectory.client import CloudDirectoryClient

    session = Session()
    client: CloudDirectoryClient = session.client("clouddirectory")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAppliedSchemaArnsPaginator,
    ListAttachedIndicesPaginator,
    ListDevelopmentSchemaArnsPaginator,
    ListDirectoriesPaginator,
    ListFacetAttributesPaginator,
    ListFacetNamesPaginator,
    ListIncomingTypedLinksPaginator,
    ListIndexPaginator,
    ListManagedSchemaArnsPaginator,
    ListObjectAttributesPaginator,
    ListObjectParentPathsPaginator,
    ListObjectPoliciesPaginator,
    ListOutgoingTypedLinksPaginator,
    ListPolicyAttachmentsPaginator,
    ListPublishedSchemaArnsPaginator,
    ListTagsForResourcePaginator,
    ListTypedLinkFacetAttributesPaginator,
    ListTypedLinkFacetNamesPaginator,
    LookupPolicyPaginator,
)
from .type_defs import (
    AddFacetToObjectRequestTypeDef,
    ApplySchemaRequestTypeDef,
    ApplySchemaResponseTypeDef,
    AttachObjectRequestTypeDef,
    AttachObjectResponseTypeDef,
    AttachPolicyRequestTypeDef,
    AttachToIndexRequestTypeDef,
    AttachToIndexResponseTypeDef,
    AttachTypedLinkRequestTypeDef,
    AttachTypedLinkResponseTypeDef,
    BatchReadRequestTypeDef,
    BatchReadResponseTypeDef,
    BatchWriteRequestTypeDef,
    BatchWriteResponseTypeDef,
    CreateDirectoryRequestTypeDef,
    CreateDirectoryResponseTypeDef,
    CreateFacetRequestTypeDef,
    CreateIndexRequestTypeDef,
    CreateIndexResponseTypeDef,
    CreateObjectRequestTypeDef,
    CreateObjectResponseTypeDef,
    CreateSchemaRequestTypeDef,
    CreateSchemaResponseTypeDef,
    CreateTypedLinkFacetRequestTypeDef,
    DeleteDirectoryRequestTypeDef,
    DeleteDirectoryResponseTypeDef,
    DeleteFacetRequestTypeDef,
    DeleteObjectRequestTypeDef,
    DeleteSchemaRequestTypeDef,
    DeleteSchemaResponseTypeDef,
    DeleteTypedLinkFacetRequestTypeDef,
    DetachFromIndexRequestTypeDef,
    DetachFromIndexResponseTypeDef,
    DetachObjectRequestTypeDef,
    DetachObjectResponseTypeDef,
    DetachPolicyRequestTypeDef,
    DetachTypedLinkRequestTypeDef,
    DisableDirectoryRequestTypeDef,
    DisableDirectoryResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    EnableDirectoryRequestTypeDef,
    EnableDirectoryResponseTypeDef,
    GetAppliedSchemaVersionRequestTypeDef,
    GetAppliedSchemaVersionResponseTypeDef,
    GetDirectoryRequestTypeDef,
    GetDirectoryResponseTypeDef,
    GetFacetRequestTypeDef,
    GetFacetResponseTypeDef,
    GetLinkAttributesRequestTypeDef,
    GetLinkAttributesResponseTypeDef,
    GetObjectAttributesRequestTypeDef,
    GetObjectAttributesResponseTypeDef,
    GetObjectInformationRequestTypeDef,
    GetObjectInformationResponseTypeDef,
    GetSchemaAsJsonRequestTypeDef,
    GetSchemaAsJsonResponseTypeDef,
    GetTypedLinkFacetInformationRequestTypeDef,
    GetTypedLinkFacetInformationResponseTypeDef,
    ListAppliedSchemaArnsRequestTypeDef,
    ListAppliedSchemaArnsResponseTypeDef,
    ListAttachedIndicesRequestTypeDef,
    ListAttachedIndicesResponseTypeDef,
    ListDevelopmentSchemaArnsRequestTypeDef,
    ListDevelopmentSchemaArnsResponseTypeDef,
    ListDirectoriesRequestTypeDef,
    ListDirectoriesResponseTypeDef,
    ListFacetAttributesRequestTypeDef,
    ListFacetAttributesResponseTypeDef,
    ListFacetNamesRequestTypeDef,
    ListFacetNamesResponseTypeDef,
    ListIncomingTypedLinksRequestTypeDef,
    ListIncomingTypedLinksResponseTypeDef,
    ListIndexRequestTypeDef,
    ListIndexResponseTypeDef,
    ListManagedSchemaArnsRequestTypeDef,
    ListManagedSchemaArnsResponseTypeDef,
    ListObjectAttributesRequestTypeDef,
    ListObjectAttributesResponseTypeDef,
    ListObjectChildrenRequestTypeDef,
    ListObjectChildrenResponseTypeDef,
    ListObjectParentPathsRequestTypeDef,
    ListObjectParentPathsResponseTypeDef,
    ListObjectParentsRequestTypeDef,
    ListObjectParentsResponseTypeDef,
    ListObjectPoliciesRequestTypeDef,
    ListObjectPoliciesResponseTypeDef,
    ListOutgoingTypedLinksRequestTypeDef,
    ListOutgoingTypedLinksResponseTypeDef,
    ListPolicyAttachmentsRequestTypeDef,
    ListPolicyAttachmentsResponseTypeDef,
    ListPublishedSchemaArnsRequestTypeDef,
    ListPublishedSchemaArnsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTypedLinkFacetAttributesRequestTypeDef,
    ListTypedLinkFacetAttributesResponseTypeDef,
    ListTypedLinkFacetNamesRequestTypeDef,
    ListTypedLinkFacetNamesResponseTypeDef,
    LookupPolicyRequestTypeDef,
    LookupPolicyResponseTypeDef,
    PublishSchemaRequestTypeDef,
    PublishSchemaResponseTypeDef,
    PutSchemaFromJsonRequestTypeDef,
    PutSchemaFromJsonResponseTypeDef,
    RemoveFacetFromObjectRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateFacetRequestTypeDef,
    UpdateLinkAttributesRequestTypeDef,
    UpdateObjectAttributesRequestTypeDef,
    UpdateObjectAttributesResponseTypeDef,
    UpdateSchemaRequestTypeDef,
    UpdateSchemaResponseTypeDef,
    UpdateTypedLinkFacetRequestTypeDef,
    UpgradeAppliedSchemaRequestTypeDef,
    UpgradeAppliedSchemaResponseTypeDef,
    UpgradePublishedSchemaRequestTypeDef,
    UpgradePublishedSchemaResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("CloudDirectoryClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    BatchWriteException: Type[BotocoreClientError]
    CannotListParentOfRootException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DirectoryAlreadyExistsException: Type[BotocoreClientError]
    DirectoryDeletedException: Type[BotocoreClientError]
    DirectoryNotDisabledException: Type[BotocoreClientError]
    DirectoryNotEnabledException: Type[BotocoreClientError]
    FacetAlreadyExistsException: Type[BotocoreClientError]
    FacetInUseException: Type[BotocoreClientError]
    FacetNotFoundException: Type[BotocoreClientError]
    FacetValidationException: Type[BotocoreClientError]
    IncompatibleSchemaException: Type[BotocoreClientError]
    IndexedAttributeMissingException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidArnException: Type[BotocoreClientError]
    InvalidAttachmentException: Type[BotocoreClientError]
    InvalidFacetUpdateException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidRuleException: Type[BotocoreClientError]
    InvalidSchemaDocException: Type[BotocoreClientError]
    InvalidTaggingRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    LinkNameAlreadyInUseException: Type[BotocoreClientError]
    NotIndexException: Type[BotocoreClientError]
    NotNodeException: Type[BotocoreClientError]
    NotPolicyException: Type[BotocoreClientError]
    ObjectAlreadyDetachedException: Type[BotocoreClientError]
    ObjectNotDetachedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    RetryableConflictException: Type[BotocoreClientError]
    SchemaAlreadyExistsException: Type[BotocoreClientError]
    SchemaAlreadyPublishedException: Type[BotocoreClientError]
    StillContainsLinksException: Type[BotocoreClientError]
    UnsupportedIndexTypeException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CloudDirectoryClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudDirectoryClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#generate_presigned_url)
        """

    def add_facet_to_object(
        self, **kwargs: Unpack[AddFacetToObjectRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds a new <a>Facet</a> to an object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/add_facet_to_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#add_facet_to_object)
        """

    def apply_schema(
        self, **kwargs: Unpack[ApplySchemaRequestTypeDef]
    ) -> ApplySchemaResponseTypeDef:
        """
        Copies the input published schema, at the specified version, into the
        <a>Directory</a> with the same name and version as that of the published
        schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/apply_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#apply_schema)
        """

    def attach_object(
        self, **kwargs: Unpack[AttachObjectRequestTypeDef]
    ) -> AttachObjectResponseTypeDef:
        """
        Attaches an existing object to another object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/attach_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#attach_object)
        """

    def attach_policy(self, **kwargs: Unpack[AttachPolicyRequestTypeDef]) -> Dict[str, Any]:
        """
        Attaches a policy object to a regular object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/attach_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#attach_policy)
        """

    def attach_to_index(
        self, **kwargs: Unpack[AttachToIndexRequestTypeDef]
    ) -> AttachToIndexResponseTypeDef:
        """
        Attaches the specified object to the specified index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/attach_to_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#attach_to_index)
        """

    def attach_typed_link(
        self, **kwargs: Unpack[AttachTypedLinkRequestTypeDef]
    ) -> AttachTypedLinkResponseTypeDef:
        """
        Attaches a typed link to a specified source and target object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/attach_typed_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#attach_typed_link)
        """

    def batch_read(self, **kwargs: Unpack[BatchReadRequestTypeDef]) -> BatchReadResponseTypeDef:
        """
        Performs all the read operations in a batch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/batch_read.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#batch_read)
        """

    def batch_write(self, **kwargs: Unpack[BatchWriteRequestTypeDef]) -> BatchWriteResponseTypeDef:
        """
        Performs all the write operations in a batch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/batch_write.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#batch_write)
        """

    def create_directory(
        self, **kwargs: Unpack[CreateDirectoryRequestTypeDef]
    ) -> CreateDirectoryResponseTypeDef:
        """
        Creates a <a>Directory</a> by copying the published schema into the directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/create_directory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#create_directory)
        """

    def create_facet(self, **kwargs: Unpack[CreateFacetRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a new <a>Facet</a> in a schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/create_facet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#create_facet)
        """

    def create_index(
        self, **kwargs: Unpack[CreateIndexRequestTypeDef]
    ) -> CreateIndexResponseTypeDef:
        """
        Creates an index object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/create_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#create_index)
        """

    def create_object(
        self, **kwargs: Unpack[CreateObjectRequestTypeDef]
    ) -> CreateObjectResponseTypeDef:
        """
        Creates an object in a <a>Directory</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/create_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#create_object)
        """

    def create_schema(
        self, **kwargs: Unpack[CreateSchemaRequestTypeDef]
    ) -> CreateSchemaResponseTypeDef:
        """
        Creates a new schema in a development state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/create_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#create_schema)
        """

    def create_typed_link_facet(
        self, **kwargs: Unpack[CreateTypedLinkFacetRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a <a>TypedLinkFacet</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/create_typed_link_facet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#create_typed_link_facet)
        """

    def delete_directory(
        self, **kwargs: Unpack[DeleteDirectoryRequestTypeDef]
    ) -> DeleteDirectoryResponseTypeDef:
        """
        Deletes a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/delete_directory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#delete_directory)
        """

    def delete_facet(self, **kwargs: Unpack[DeleteFacetRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a given <a>Facet</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/delete_facet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#delete_facet)
        """

    def delete_object(self, **kwargs: Unpack[DeleteObjectRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an object and its associated attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/delete_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#delete_object)
        """

    def delete_schema(
        self, **kwargs: Unpack[DeleteSchemaRequestTypeDef]
    ) -> DeleteSchemaResponseTypeDef:
        """
        Deletes a given schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/delete_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#delete_schema)
        """

    def delete_typed_link_facet(
        self, **kwargs: Unpack[DeleteTypedLinkFacetRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a <a>TypedLinkFacet</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/delete_typed_link_facet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#delete_typed_link_facet)
        """

    def detach_from_index(
        self, **kwargs: Unpack[DetachFromIndexRequestTypeDef]
    ) -> DetachFromIndexResponseTypeDef:
        """
        Detaches the specified object from the specified index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/detach_from_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#detach_from_index)
        """

    def detach_object(
        self, **kwargs: Unpack[DetachObjectRequestTypeDef]
    ) -> DetachObjectResponseTypeDef:
        """
        Detaches a given object from the parent object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/detach_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#detach_object)
        """

    def detach_policy(self, **kwargs: Unpack[DetachPolicyRequestTypeDef]) -> Dict[str, Any]:
        """
        Detaches a policy from an object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/detach_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#detach_policy)
        """

    def detach_typed_link(
        self, **kwargs: Unpack[DetachTypedLinkRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Detaches a typed link from a specified source and target object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/detach_typed_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#detach_typed_link)
        """

    def disable_directory(
        self, **kwargs: Unpack[DisableDirectoryRequestTypeDef]
    ) -> DisableDirectoryResponseTypeDef:
        """
        Disables the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/disable_directory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#disable_directory)
        """

    def enable_directory(
        self, **kwargs: Unpack[EnableDirectoryRequestTypeDef]
    ) -> EnableDirectoryResponseTypeDef:
        """
        Enables the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/enable_directory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#enable_directory)
        """

    def get_applied_schema_version(
        self, **kwargs: Unpack[GetAppliedSchemaVersionRequestTypeDef]
    ) -> GetAppliedSchemaVersionResponseTypeDef:
        """
        Returns current applied schema version ARN, including the minor version in use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_applied_schema_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_applied_schema_version)
        """

    def get_directory(
        self, **kwargs: Unpack[GetDirectoryRequestTypeDef]
    ) -> GetDirectoryResponseTypeDef:
        """
        Retrieves metadata about a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_directory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_directory)
        """

    def get_facet(self, **kwargs: Unpack[GetFacetRequestTypeDef]) -> GetFacetResponseTypeDef:
        """
        Gets details of the <a>Facet</a>, such as facet name, attributes, <a>Rule</a>s,
        or <code>ObjectType</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_facet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_facet)
        """

    def get_link_attributes(
        self, **kwargs: Unpack[GetLinkAttributesRequestTypeDef]
    ) -> GetLinkAttributesResponseTypeDef:
        """
        Retrieves attributes that are associated with a typed link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_link_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_link_attributes)
        """

    def get_object_attributes(
        self, **kwargs: Unpack[GetObjectAttributesRequestTypeDef]
    ) -> GetObjectAttributesResponseTypeDef:
        """
        Retrieves attributes within a facet that are associated with an object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_object_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_object_attributes)
        """

    def get_object_information(
        self, **kwargs: Unpack[GetObjectInformationRequestTypeDef]
    ) -> GetObjectInformationResponseTypeDef:
        """
        Retrieves metadata about an object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_object_information.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_object_information)
        """

    def get_schema_as_json(
        self, **kwargs: Unpack[GetSchemaAsJsonRequestTypeDef]
    ) -> GetSchemaAsJsonResponseTypeDef:
        """
        Retrieves a JSON representation of the schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_schema_as_json.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_schema_as_json)
        """

    def get_typed_link_facet_information(
        self, **kwargs: Unpack[GetTypedLinkFacetInformationRequestTypeDef]
    ) -> GetTypedLinkFacetInformationResponseTypeDef:
        """
        Returns the identity attribute order for a specific <a>TypedLinkFacet</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_typed_link_facet_information.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_typed_link_facet_information)
        """

    def list_applied_schema_arns(
        self, **kwargs: Unpack[ListAppliedSchemaArnsRequestTypeDef]
    ) -> ListAppliedSchemaArnsResponseTypeDef:
        """
        Lists schema major versions applied to a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_applied_schema_arns.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_applied_schema_arns)
        """

    def list_attached_indices(
        self, **kwargs: Unpack[ListAttachedIndicesRequestTypeDef]
    ) -> ListAttachedIndicesResponseTypeDef:
        """
        Lists indices attached to the specified object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_attached_indices.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_attached_indices)
        """

    def list_development_schema_arns(
        self, **kwargs: Unpack[ListDevelopmentSchemaArnsRequestTypeDef]
    ) -> ListDevelopmentSchemaArnsResponseTypeDef:
        """
        Retrieves each Amazon Resource Name (ARN) of schemas in the development state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_development_schema_arns.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_development_schema_arns)
        """

    def list_directories(
        self, **kwargs: Unpack[ListDirectoriesRequestTypeDef]
    ) -> ListDirectoriesResponseTypeDef:
        """
        Lists directories created within an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_directories.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_directories)
        """

    def list_facet_attributes(
        self, **kwargs: Unpack[ListFacetAttributesRequestTypeDef]
    ) -> ListFacetAttributesResponseTypeDef:
        """
        Retrieves attributes attached to the facet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_facet_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_facet_attributes)
        """

    def list_facet_names(
        self, **kwargs: Unpack[ListFacetNamesRequestTypeDef]
    ) -> ListFacetNamesResponseTypeDef:
        """
        Retrieves the names of facets that exist in a schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_facet_names.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_facet_names)
        """

    def list_incoming_typed_links(
        self, **kwargs: Unpack[ListIncomingTypedLinksRequestTypeDef]
    ) -> ListIncomingTypedLinksResponseTypeDef:
        """
        Returns a paginated list of all the incoming <a>TypedLinkSpecifier</a>
        information for an object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_incoming_typed_links.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_incoming_typed_links)
        """

    def list_index(self, **kwargs: Unpack[ListIndexRequestTypeDef]) -> ListIndexResponseTypeDef:
        """
        Lists objects attached to the specified index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_index)
        """

    def list_managed_schema_arns(
        self, **kwargs: Unpack[ListManagedSchemaArnsRequestTypeDef]
    ) -> ListManagedSchemaArnsResponseTypeDef:
        """
        Lists the major version families of each managed schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_managed_schema_arns.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_managed_schema_arns)
        """

    def list_object_attributes(
        self, **kwargs: Unpack[ListObjectAttributesRequestTypeDef]
    ) -> ListObjectAttributesResponseTypeDef:
        """
        Lists all attributes that are associated with an object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_object_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_object_attributes)
        """

    def list_object_children(
        self, **kwargs: Unpack[ListObjectChildrenRequestTypeDef]
    ) -> ListObjectChildrenResponseTypeDef:
        """
        Returns a paginated list of child objects that are associated with a given
        object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_object_children.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_object_children)
        """

    def list_object_parent_paths(
        self, **kwargs: Unpack[ListObjectParentPathsRequestTypeDef]
    ) -> ListObjectParentPathsResponseTypeDef:
        """
        Retrieves all available parent paths for any object type such as node, leaf
        node, policy node, and index node objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_object_parent_paths.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_object_parent_paths)
        """

    def list_object_parents(
        self, **kwargs: Unpack[ListObjectParentsRequestTypeDef]
    ) -> ListObjectParentsResponseTypeDef:
        """
        Lists parent objects that are associated with a given object in pagination
        fashion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_object_parents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_object_parents)
        """

    def list_object_policies(
        self, **kwargs: Unpack[ListObjectPoliciesRequestTypeDef]
    ) -> ListObjectPoliciesResponseTypeDef:
        """
        Returns policies attached to an object in pagination fashion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_object_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_object_policies)
        """

    def list_outgoing_typed_links(
        self, **kwargs: Unpack[ListOutgoingTypedLinksRequestTypeDef]
    ) -> ListOutgoingTypedLinksResponseTypeDef:
        """
        Returns a paginated list of all the outgoing <a>TypedLinkSpecifier</a>
        information for an object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_outgoing_typed_links.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_outgoing_typed_links)
        """

    def list_policy_attachments(
        self, **kwargs: Unpack[ListPolicyAttachmentsRequestTypeDef]
    ) -> ListPolicyAttachmentsResponseTypeDef:
        """
        Returns all of the <code>ObjectIdentifiers</code> to which a given policy is
        attached.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_policy_attachments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_policy_attachments)
        """

    def list_published_schema_arns(
        self, **kwargs: Unpack[ListPublishedSchemaArnsRequestTypeDef]
    ) -> ListPublishedSchemaArnsResponseTypeDef:
        """
        Lists the major version families of each published schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_published_schema_arns.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_published_schema_arns)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_tags_for_resource)
        """

    def list_typed_link_facet_attributes(
        self, **kwargs: Unpack[ListTypedLinkFacetAttributesRequestTypeDef]
    ) -> ListTypedLinkFacetAttributesResponseTypeDef:
        """
        Returns a paginated list of all attribute definitions for a particular
        <a>TypedLinkFacet</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_typed_link_facet_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_typed_link_facet_attributes)
        """

    def list_typed_link_facet_names(
        self, **kwargs: Unpack[ListTypedLinkFacetNamesRequestTypeDef]
    ) -> ListTypedLinkFacetNamesResponseTypeDef:
        """
        Returns a paginated list of <code>TypedLink</code> facet names for a particular
        schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/list_typed_link_facet_names.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#list_typed_link_facet_names)
        """

    def lookup_policy(
        self, **kwargs: Unpack[LookupPolicyRequestTypeDef]
    ) -> LookupPolicyResponseTypeDef:
        """
        Lists all policies from the root of the <a>Directory</a> to the object
        specified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/lookup_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#lookup_policy)
        """

    def publish_schema(
        self, **kwargs: Unpack[PublishSchemaRequestTypeDef]
    ) -> PublishSchemaResponseTypeDef:
        """
        Publishes a development schema with a major version and a recommended minor
        version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/publish_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#publish_schema)
        """

    def put_schema_from_json(
        self, **kwargs: Unpack[PutSchemaFromJsonRequestTypeDef]
    ) -> PutSchemaFromJsonResponseTypeDef:
        """
        Allows a schema to be updated using JSON upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/put_schema_from_json.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#put_schema_from_json)
        """

    def remove_facet_from_object(
        self, **kwargs: Unpack[RemoveFacetFromObjectRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the specified facet from the specified object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/remove_facet_from_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#remove_facet_from_object)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        An API operation for adding tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        An API operation for removing tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#untag_resource)
        """

    def update_facet(self, **kwargs: Unpack[UpdateFacetRequestTypeDef]) -> Dict[str, Any]:
        """
        Does the following:.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/update_facet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#update_facet)
        """

    def update_link_attributes(
        self, **kwargs: Unpack[UpdateLinkAttributesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a given typed link's attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/update_link_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#update_link_attributes)
        """

    def update_object_attributes(
        self, **kwargs: Unpack[UpdateObjectAttributesRequestTypeDef]
    ) -> UpdateObjectAttributesResponseTypeDef:
        """
        Updates a given object's attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/update_object_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#update_object_attributes)
        """

    def update_schema(
        self, **kwargs: Unpack[UpdateSchemaRequestTypeDef]
    ) -> UpdateSchemaResponseTypeDef:
        """
        Updates the schema name with a new name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/update_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#update_schema)
        """

    def update_typed_link_facet(
        self, **kwargs: Unpack[UpdateTypedLinkFacetRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a <a>TypedLinkFacet</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/update_typed_link_facet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#update_typed_link_facet)
        """

    def upgrade_applied_schema(
        self, **kwargs: Unpack[UpgradeAppliedSchemaRequestTypeDef]
    ) -> UpgradeAppliedSchemaResponseTypeDef:
        """
        Upgrades a single directory in-place using the <code>PublishedSchemaArn</code>
        with schema updates found in <code>MinorVersion</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/upgrade_applied_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#upgrade_applied_schema)
        """

    def upgrade_published_schema(
        self, **kwargs: Unpack[UpgradePublishedSchemaRequestTypeDef]
    ) -> UpgradePublishedSchemaResponseTypeDef:
        """
        Upgrades a published schema under a new minor version revision using the
        current contents of <code>DevelopmentSchemaArn</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/upgrade_published_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#upgrade_published_schema)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_applied_schema_arns"]
    ) -> ListAppliedSchemaArnsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_attached_indices"]
    ) -> ListAttachedIndicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_development_schema_arns"]
    ) -> ListDevelopmentSchemaArnsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_directories"]
    ) -> ListDirectoriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_facet_attributes"]
    ) -> ListFacetAttributesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_facet_names"]
    ) -> ListFacetNamesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_incoming_typed_links"]
    ) -> ListIncomingTypedLinksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_index"]
    ) -> ListIndexPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_managed_schema_arns"]
    ) -> ListManagedSchemaArnsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_object_attributes"]
    ) -> ListObjectAttributesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_object_parent_paths"]
    ) -> ListObjectParentPathsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_object_policies"]
    ) -> ListObjectPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_outgoing_typed_links"]
    ) -> ListOutgoingTypedLinksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policy_attachments"]
    ) -> ListPolicyAttachmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_published_schema_arns"]
    ) -> ListPublishedSchemaArnsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_typed_link_facet_attributes"]
    ) -> ListTypedLinkFacetAttributesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_typed_link_facet_names"]
    ) -> ListTypedLinkFacetNamesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["lookup_policy"]
    ) -> LookupPolicyPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client/#get_paginator)
        """
