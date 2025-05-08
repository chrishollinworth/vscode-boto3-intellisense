"""
Main interface for clouddirectory service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_clouddirectory import (
        Client,
        CloudDirectoryClient,
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

    session = Session()
    client: CloudDirectoryClient = session.client("clouddirectory")

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

from .client import CloudDirectoryClient
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

Client = CloudDirectoryClient

__all__ = (
    "Client",
    "CloudDirectoryClient",
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
