# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for clouddirectory service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_clouddirectory import CloudDirectoryClient
    from mypy_boto3_clouddirectory.paginator import (
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

    client: CloudDirectoryClient = boto3.client("clouddirectory")

    list_applied_schema_arns_paginator: ListAppliedSchemaArnsPaginator = client.get_paginator("list_applied_schema_arns")
    list_attached_indices_paginator: ListAttachedIndicesPaginator = client.get_paginator("list_attached_indices")
    list_development_schema_arns_paginator: ListDevelopmentSchemaArnsPaginator = client.get_paginator("list_development_schema_arns")
    list_directories_paginator: ListDirectoriesPaginator = client.get_paginator("list_directories")
    list_facet_attributes_paginator: ListFacetAttributesPaginator = client.get_paginator("list_facet_attributes")
    list_facet_names_paginator: ListFacetNamesPaginator = client.get_paginator("list_facet_names")
    list_incoming_typed_links_paginator: ListIncomingTypedLinksPaginator = client.get_paginator("list_incoming_typed_links")
    list_index_paginator: ListIndexPaginator = client.get_paginator("list_index")
    list_managed_schema_arns_paginator: ListManagedSchemaArnsPaginator = client.get_paginator("list_managed_schema_arns")
    list_object_attributes_paginator: ListObjectAttributesPaginator = client.get_paginator("list_object_attributes")
    list_object_parent_paths_paginator: ListObjectParentPathsPaginator = client.get_paginator("list_object_parent_paths")
    list_object_policies_paginator: ListObjectPoliciesPaginator = client.get_paginator("list_object_policies")
    list_outgoing_typed_links_paginator: ListOutgoingTypedLinksPaginator = client.get_paginator("list_outgoing_typed_links")
    list_policy_attachments_paginator: ListPolicyAttachmentsPaginator = client.get_paginator("list_policy_attachments")
    list_published_schema_arns_paginator: ListPublishedSchemaArnsPaginator = client.get_paginator("list_published_schema_arns")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_typed_link_facet_attributes_paginator: ListTypedLinkFacetAttributesPaginator = client.get_paginator("list_typed_link_facet_attributes")
    list_typed_link_facet_names_paginator: ListTypedLinkFacetNamesPaginator = client.get_paginator("list_typed_link_facet_names")
    lookup_policy_paginator: LookupPolicyPaginator = client.get_paginator("lookup_policy")
    ```
"""
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_clouddirectory.type_defs import (
    ListAppliedSchemaArnsResponseTypeDef,
    ListAttachedIndicesResponseTypeDef,
    ListDevelopmentSchemaArnsResponseTypeDef,
    ListDirectoriesResponseTypeDef,
    ListFacetAttributesResponseTypeDef,
    ListFacetNamesResponseTypeDef,
    ListIncomingTypedLinksResponseTypeDef,
    ListIndexResponseTypeDef,
    ListManagedSchemaArnsResponseTypeDef,
    ListObjectAttributesResponseTypeDef,
    ListObjectParentPathsResponseTypeDef,
    ListObjectPoliciesResponseTypeDef,
    ListOutgoingTypedLinksResponseTypeDef,
    ListPolicyAttachmentsResponseTypeDef,
    ListPublishedSchemaArnsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTypedLinkFacetAttributesResponseTypeDef,
    ListTypedLinkFacetNamesResponseTypeDef,
    LookupPolicyResponseTypeDef,
    ObjectAttributeRangeTypeDef,
    ObjectReferenceTypeDef,
    PaginatorConfigTypeDef,
    SchemaFacetTypeDef,
    TypedLinkAttributeRangeTypeDef,
    TypedLinkSchemaAndFacetNameTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAppliedSchemaArnsPaginator",
    "ListAttachedIndicesPaginator",
    "ListDevelopmentSchemaArnsPaginator",
    "ListDirectoriesPaginator",
    "ListFacetAttributesPaginator",
    "ListFacetNamesPaginator",
    "ListIncomingTypedLinksPaginator",
    "ListIndexPaginator",
    "ListManagedSchemaArnsPaginator",
    "ListObjectAttributesPaginator",
    "ListObjectParentPathsPaginator",
    "ListObjectPoliciesPaginator",
    "ListOutgoingTypedLinksPaginator",
    "ListPolicyAttachmentsPaginator",
    "ListPublishedSchemaArnsPaginator",
    "ListTagsForResourcePaginator",
    "ListTypedLinkFacetAttributesPaginator",
    "ListTypedLinkFacetNamesPaginator",
    "LookupPolicyPaginator",
)


class ListAppliedSchemaArnsPaginator(Boto3Paginator):
    """
    [Paginator.ListAppliedSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAppliedSchemaArns)
    """

    def paginate(
        self,
        DirectoryArn: str,
        SchemaArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAppliedSchemaArnsResponseTypeDef]:
        """
        [ListAppliedSchemaArns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAppliedSchemaArns.paginate)
        """


class ListAttachedIndicesPaginator(Boto3Paginator):
    """
    [Paginator.ListAttachedIndices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAttachedIndices)
    """

    def paginate(
        self,
        DirectoryArn: str,
        TargetReference: "ObjectReferenceTypeDef",
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAttachedIndicesResponseTypeDef]:
        """
        [ListAttachedIndices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAttachedIndices.paginate)
        """


class ListDevelopmentSchemaArnsPaginator(Boto3Paginator):
    """
    [Paginator.ListDevelopmentSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDevelopmentSchemaArns)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDevelopmentSchemaArnsResponseTypeDef]:
        """
        [ListDevelopmentSchemaArns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDevelopmentSchemaArns.paginate)
        """


class ListDirectoriesPaginator(Boto3Paginator):
    """
    [Paginator.ListDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDirectories)
    """

    def paginate(
        self,
        state: Literal["ENABLED", "DISABLED", "DELETED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDirectoriesResponseTypeDef]:
        """
        [ListDirectories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDirectories.paginate)
        """


class ListFacetAttributesPaginator(Boto3Paginator):
    """
    [Paginator.ListFacetAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetAttributes)
    """

    def paginate(
        self, SchemaArn: str, Name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFacetAttributesResponseTypeDef]:
        """
        [ListFacetAttributes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetAttributes.paginate)
        """


class ListFacetNamesPaginator(Boto3Paginator):
    """
    [Paginator.ListFacetNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetNames)
    """

    def paginate(
        self, SchemaArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFacetNamesResponseTypeDef]:
        """
        [ListFacetNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetNames.paginate)
        """


class ListIncomingTypedLinksPaginator(Boto3Paginator):
    """
    [Paginator.ListIncomingTypedLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIncomingTypedLinks)
    """

    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        FilterAttributeRanges: List["TypedLinkAttributeRangeTypeDef"] = None,
        FilterTypedLink: "TypedLinkSchemaAndFacetNameTypeDef" = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListIncomingTypedLinksResponseTypeDef]:
        """
        [ListIncomingTypedLinks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIncomingTypedLinks.paginate)
        """


class ListIndexPaginator(Boto3Paginator):
    """
    [Paginator.ListIndex documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIndex)
    """

    def paginate(
        self,
        DirectoryArn: str,
        IndexReference: "ObjectReferenceTypeDef",
        RangesOnIndexedValues: List["ObjectAttributeRangeTypeDef"] = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListIndexResponseTypeDef]:
        """
        [ListIndex.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIndex.paginate)
        """


class ListManagedSchemaArnsPaginator(Boto3Paginator):
    """
    [Paginator.ListManagedSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListManagedSchemaArns)
    """

    def paginate(
        self, SchemaArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListManagedSchemaArnsResponseTypeDef]:
        """
        [ListManagedSchemaArns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListManagedSchemaArns.paginate)
        """


class ListObjectAttributesPaginator(Boto3Paginator):
    """
    [Paginator.ListObjectAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectAttributes)
    """

    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        FacetFilter: "SchemaFacetTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListObjectAttributesResponseTypeDef]:
        """
        [ListObjectAttributes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectAttributes.paginate)
        """


class ListObjectParentPathsPaginator(Boto3Paginator):
    """
    [Paginator.ListObjectParentPaths documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectParentPaths)
    """

    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListObjectParentPathsResponseTypeDef]:
        """
        [ListObjectParentPaths.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectParentPaths.paginate)
        """


class ListObjectPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListObjectPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectPolicies)
    """

    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListObjectPoliciesResponseTypeDef]:
        """
        [ListObjectPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectPolicies.paginate)
        """


class ListOutgoingTypedLinksPaginator(Boto3Paginator):
    """
    [Paginator.ListOutgoingTypedLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListOutgoingTypedLinks)
    """

    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        FilterAttributeRanges: List["TypedLinkAttributeRangeTypeDef"] = None,
        FilterTypedLink: "TypedLinkSchemaAndFacetNameTypeDef" = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListOutgoingTypedLinksResponseTypeDef]:
        """
        [ListOutgoingTypedLinks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListOutgoingTypedLinks.paginate)
        """


class ListPolicyAttachmentsPaginator(Boto3Paginator):
    """
    [Paginator.ListPolicyAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPolicyAttachments)
    """

    def paginate(
        self,
        DirectoryArn: str,
        PolicyReference: "ObjectReferenceTypeDef",
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPolicyAttachmentsResponseTypeDef]:
        """
        [ListPolicyAttachments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPolicyAttachments.paginate)
        """


class ListPublishedSchemaArnsPaginator(Boto3Paginator):
    """
    [Paginator.ListPublishedSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPublishedSchemaArns)
    """

    def paginate(
        self, SchemaArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPublishedSchemaArnsResponseTypeDef]:
        """
        [ListPublishedSchemaArns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPublishedSchemaArns.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTagsForResource)
    """

    def paginate(
        self, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTagsForResource.paginate)
        """


class ListTypedLinkFacetAttributesPaginator(Boto3Paginator):
    """
    [Paginator.ListTypedLinkFacetAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetAttributes)
    """

    def paginate(
        self, SchemaArn: str, Name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTypedLinkFacetAttributesResponseTypeDef]:
        """
        [ListTypedLinkFacetAttributes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetAttributes.paginate)
        """


class ListTypedLinkFacetNamesPaginator(Boto3Paginator):
    """
    [Paginator.ListTypedLinkFacetNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetNames)
    """

    def paginate(
        self, SchemaArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTypedLinkFacetNamesResponseTypeDef]:
        """
        [ListTypedLinkFacetNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetNames.paginate)
        """


class LookupPolicyPaginator(Boto3Paginator):
    """
    [Paginator.LookupPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.LookupPolicy)
    """

    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[LookupPolicyResponseTypeDef]:
        """
        [LookupPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/clouddirectory.html#CloudDirectory.Paginator.LookupPolicy.paginate)
        """
