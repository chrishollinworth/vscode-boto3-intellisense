"""
Type annotations for servicecatalog-appregistry service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_servicecatalog_appregistry.client import AppRegistryClient

    session = Session()
    client: AppRegistryClient = session.client("servicecatalog-appregistry")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListApplicationsPaginator,
    ListAssociatedAttributeGroupsPaginator,
    ListAssociatedResourcesPaginator,
    ListAttributeGroupsForApplicationPaginator,
    ListAttributeGroupsPaginator,
)
from .type_defs import (
    AssociateAttributeGroupRequestTypeDef,
    AssociateAttributeGroupResponseTypeDef,
    AssociateResourceRequestTypeDef,
    AssociateResourceResponseTypeDef,
    CreateApplicationRequestTypeDef,
    CreateApplicationResponseTypeDef,
    CreateAttributeGroupRequestTypeDef,
    CreateAttributeGroupResponseTypeDef,
    DeleteApplicationRequestTypeDef,
    DeleteApplicationResponseTypeDef,
    DeleteAttributeGroupRequestTypeDef,
    DeleteAttributeGroupResponseTypeDef,
    DisassociateAttributeGroupRequestTypeDef,
    DisassociateAttributeGroupResponseTypeDef,
    DisassociateResourceRequestTypeDef,
    DisassociateResourceResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetApplicationRequestTypeDef,
    GetApplicationResponseTypeDef,
    GetAssociatedResourceRequestTypeDef,
    GetAssociatedResourceResponseTypeDef,
    GetAttributeGroupRequestTypeDef,
    GetAttributeGroupResponseTypeDef,
    GetConfigurationResponseTypeDef,
    ListApplicationsRequestTypeDef,
    ListApplicationsResponseTypeDef,
    ListAssociatedAttributeGroupsRequestTypeDef,
    ListAssociatedAttributeGroupsResponseTypeDef,
    ListAssociatedResourcesRequestTypeDef,
    ListAssociatedResourcesResponseTypeDef,
    ListAttributeGroupsForApplicationRequestTypeDef,
    ListAttributeGroupsForApplicationResponseTypeDef,
    ListAttributeGroupsRequestTypeDef,
    ListAttributeGroupsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutConfigurationRequestTypeDef,
    SyncResourceRequestTypeDef,
    SyncResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateApplicationRequestTypeDef,
    UpdateApplicationResponseTypeDef,
    UpdateAttributeGroupRequestTypeDef,
    UpdateAttributeGroupResponseTypeDef,
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

__all__ = ("AppRegistryClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AppRegistryClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppRegistryClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#generate_presigned_url)
        """

    def associate_attribute_group(
        self, **kwargs: Unpack[AssociateAttributeGroupRequestTypeDef]
    ) -> AssociateAttributeGroupResponseTypeDef:
        """
        Associates an attribute group with an application to augment the application's
        metadata with the group's attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/associate_attribute_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#associate_attribute_group)
        """

    def associate_resource(
        self, **kwargs: Unpack[AssociateResourceRequestTypeDef]
    ) -> AssociateResourceResponseTypeDef:
        """
        Associates a resource with an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/associate_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#associate_resource)
        """

    def create_application(
        self, **kwargs: Unpack[CreateApplicationRequestTypeDef]
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates a new application that is the top-level node in a hierarchy of related
        cloud resource abstractions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/create_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#create_application)
        """

    def create_attribute_group(
        self, **kwargs: Unpack[CreateAttributeGroupRequestTypeDef]
    ) -> CreateAttributeGroupResponseTypeDef:
        """
        Creates a new attribute group as a container for user-defined attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/create_attribute_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#create_attribute_group)
        """

    def delete_application(
        self, **kwargs: Unpack[DeleteApplicationRequestTypeDef]
    ) -> DeleteApplicationResponseTypeDef:
        """
        Deletes an application that is specified either by its application ID, name, or
        ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/delete_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#delete_application)
        """

    def delete_attribute_group(
        self, **kwargs: Unpack[DeleteAttributeGroupRequestTypeDef]
    ) -> DeleteAttributeGroupResponseTypeDef:
        """
        Deletes an attribute group, specified either by its attribute group ID, name,
        or ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/delete_attribute_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#delete_attribute_group)
        """

    def disassociate_attribute_group(
        self, **kwargs: Unpack[DisassociateAttributeGroupRequestTypeDef]
    ) -> DisassociateAttributeGroupResponseTypeDef:
        """
        Disassociates an attribute group from an application to remove the extra
        attributes contained in the attribute group from the application's metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/disassociate_attribute_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#disassociate_attribute_group)
        """

    def disassociate_resource(
        self, **kwargs: Unpack[DisassociateResourceRequestTypeDef]
    ) -> DisassociateResourceResponseTypeDef:
        """
        Disassociates a resource from application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/disassociate_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#disassociate_resource)
        """

    def get_application(
        self, **kwargs: Unpack[GetApplicationRequestTypeDef]
    ) -> GetApplicationResponseTypeDef:
        """
        Retrieves metadata information about one of your applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/get_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#get_application)
        """

    def get_associated_resource(
        self, **kwargs: Unpack[GetAssociatedResourceRequestTypeDef]
    ) -> GetAssociatedResourceResponseTypeDef:
        """
        Gets the resource associated with the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/get_associated_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#get_associated_resource)
        """

    def get_attribute_group(
        self, **kwargs: Unpack[GetAttributeGroupRequestTypeDef]
    ) -> GetAttributeGroupResponseTypeDef:
        """
        Retrieves an attribute group by its ARN, ID, or name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/get_attribute_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#get_attribute_group)
        """

    def get_configuration(self) -> GetConfigurationResponseTypeDef:
        """
        Retrieves a <code>TagKey</code> configuration from an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/get_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#get_configuration)
        """

    def list_applications(
        self, **kwargs: Unpack[ListApplicationsRequestTypeDef]
    ) -> ListApplicationsResponseTypeDef:
        """
        Retrieves a list of all of your applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/list_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#list_applications)
        """

    def list_associated_attribute_groups(
        self, **kwargs: Unpack[ListAssociatedAttributeGroupsRequestTypeDef]
    ) -> ListAssociatedAttributeGroupsResponseTypeDef:
        """
        Lists all attribute groups that are associated with specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/list_associated_attribute_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#list_associated_attribute_groups)
        """

    def list_associated_resources(
        self, **kwargs: Unpack[ListAssociatedResourcesRequestTypeDef]
    ) -> ListAssociatedResourcesResponseTypeDef:
        """
        Lists all of the resources that are associated with the specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/list_associated_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#list_associated_resources)
        """

    def list_attribute_groups(
        self, **kwargs: Unpack[ListAttributeGroupsRequestTypeDef]
    ) -> ListAttributeGroupsResponseTypeDef:
        """
        Lists all attribute groups which you have access to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/list_attribute_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#list_attribute_groups)
        """

    def list_attribute_groups_for_application(
        self, **kwargs: Unpack[ListAttributeGroupsForApplicationRequestTypeDef]
    ) -> ListAttributeGroupsForApplicationResponseTypeDef:
        """
        Lists the details of all attribute groups associated with a specific
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/list_attribute_groups_for_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#list_attribute_groups_for_application)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all of the tags on the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#list_tags_for_resource)
        """

    def put_configuration(
        self, **kwargs: Unpack[PutConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates a <code>TagKey</code> configuration to an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/put_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#put_configuration)
        """

    def sync_resource(
        self, **kwargs: Unpack[SyncResourceRequestTypeDef]
    ) -> SyncResourceResponseTypeDef:
        """
        Syncs the resource with current AppRegistry records.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/sync_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#sync_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#untag_resource)
        """

    def update_application(
        self, **kwargs: Unpack[UpdateApplicationRequestTypeDef]
    ) -> UpdateApplicationResponseTypeDef:
        """
        Updates an existing application with new attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/update_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#update_application)
        """

    def update_attribute_group(
        self, **kwargs: Unpack[UpdateAttributeGroupRequestTypeDef]
    ) -> UpdateAttributeGroupResponseTypeDef:
        """
        Updates an existing attribute group with new details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/update_attribute_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#update_attribute_group)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_associated_attribute_groups"]
    ) -> ListAssociatedAttributeGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_associated_resources"]
    ) -> ListAssociatedResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_attribute_groups_for_application"]
    ) -> ListAttributeGroupsForApplicationPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_attribute_groups"]
    ) -> ListAttributeGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client/#get_paginator)
        """
