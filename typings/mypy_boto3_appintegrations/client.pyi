"""
Type annotations for appintegrations service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_appintegrations.client import AppIntegrationsServiceClient

    session = Session()
    client: AppIntegrationsServiceClient = session.client("appintegrations")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListApplicationAssociationsPaginator,
    ListApplicationsPaginator,
    ListDataIntegrationAssociationsPaginator,
    ListDataIntegrationsPaginator,
    ListEventIntegrationAssociationsPaginator,
    ListEventIntegrationsPaginator,
)
from .type_defs import (
    CreateApplicationRequestTypeDef,
    CreateApplicationResponseTypeDef,
    CreateDataIntegrationAssociationRequestTypeDef,
    CreateDataIntegrationAssociationResponseTypeDef,
    CreateDataIntegrationRequestTypeDef,
    CreateDataIntegrationResponseTypeDef,
    CreateEventIntegrationRequestTypeDef,
    CreateEventIntegrationResponseTypeDef,
    DeleteApplicationRequestTypeDef,
    DeleteDataIntegrationRequestTypeDef,
    DeleteEventIntegrationRequestTypeDef,
    GetApplicationRequestTypeDef,
    GetApplicationResponseTypeDef,
    GetDataIntegrationRequestTypeDef,
    GetDataIntegrationResponseTypeDef,
    GetEventIntegrationRequestTypeDef,
    GetEventIntegrationResponseTypeDef,
    ListApplicationAssociationsRequestTypeDef,
    ListApplicationAssociationsResponseTypeDef,
    ListApplicationsRequestTypeDef,
    ListApplicationsResponseTypeDef,
    ListDataIntegrationAssociationsRequestTypeDef,
    ListDataIntegrationAssociationsResponseTypeDef,
    ListDataIntegrationsRequestTypeDef,
    ListDataIntegrationsResponseTypeDef,
    ListEventIntegrationAssociationsRequestTypeDef,
    ListEventIntegrationAssociationsResponseTypeDef,
    ListEventIntegrationsRequestTypeDef,
    ListEventIntegrationsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateApplicationRequestTypeDef,
    UpdateDataIntegrationAssociationRequestTypeDef,
    UpdateDataIntegrationRequestTypeDef,
    UpdateEventIntegrationRequestTypeDef,
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

__all__ = ("AppIntegrationsServiceClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DuplicateResourceException: Type[BotocoreClientError]
    InternalServiceError: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]

class AppIntegrationsServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppIntegrationsServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#generate_presigned_url)
        """

    def create_application(
        self, **kwargs: Unpack[CreateApplicationRequestTypeDef]
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates and persists an Application resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/create_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#create_application)
        """

    def create_data_integration(
        self, **kwargs: Unpack[CreateDataIntegrationRequestTypeDef]
    ) -> CreateDataIntegrationResponseTypeDef:
        """
        Creates and persists a DataIntegration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/create_data_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#create_data_integration)
        """

    def create_data_integration_association(
        self, **kwargs: Unpack[CreateDataIntegrationAssociationRequestTypeDef]
    ) -> CreateDataIntegrationAssociationResponseTypeDef:
        """
        Creates and persists a DataIntegrationAssociation resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/create_data_integration_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#create_data_integration_association)
        """

    def create_event_integration(
        self, **kwargs: Unpack[CreateEventIntegrationRequestTypeDef]
    ) -> CreateEventIntegrationResponseTypeDef:
        """
        Creates an EventIntegration, given a specified name, description, and a
        reference to an Amazon EventBridge bus in your account and a partner event
        source that pushes events to that bus.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/create_event_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#create_event_integration)
        """

    def delete_application(
        self, **kwargs: Unpack[DeleteApplicationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the Application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/delete_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#delete_application)
        """

    def delete_data_integration(
        self, **kwargs: Unpack[DeleteDataIntegrationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the DataIntegration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/delete_data_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#delete_data_integration)
        """

    def delete_event_integration(
        self, **kwargs: Unpack[DeleteEventIntegrationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified existing event integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/delete_event_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#delete_event_integration)
        """

    def get_application(
        self, **kwargs: Unpack[GetApplicationRequestTypeDef]
    ) -> GetApplicationResponseTypeDef:
        """
        Get an Application resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/get_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#get_application)
        """

    def get_data_integration(
        self, **kwargs: Unpack[GetDataIntegrationRequestTypeDef]
    ) -> GetDataIntegrationResponseTypeDef:
        """
        Returns information about the DataIntegration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/get_data_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#get_data_integration)
        """

    def get_event_integration(
        self, **kwargs: Unpack[GetEventIntegrationRequestTypeDef]
    ) -> GetEventIntegrationResponseTypeDef:
        """
        Returns information about the event integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/get_event_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#get_event_integration)
        """

    def list_application_associations(
        self, **kwargs: Unpack[ListApplicationAssociationsRequestTypeDef]
    ) -> ListApplicationAssociationsResponseTypeDef:
        """
        Returns a paginated list of application associations for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/list_application_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#list_application_associations)
        """

    def list_applications(
        self, **kwargs: Unpack[ListApplicationsRequestTypeDef]
    ) -> ListApplicationsResponseTypeDef:
        """
        Lists applications in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/list_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#list_applications)
        """

    def list_data_integration_associations(
        self, **kwargs: Unpack[ListDataIntegrationAssociationsRequestTypeDef]
    ) -> ListDataIntegrationAssociationsResponseTypeDef:
        """
        Returns a paginated list of DataIntegration associations in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/list_data_integration_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#list_data_integration_associations)
        """

    def list_data_integrations(
        self, **kwargs: Unpack[ListDataIntegrationsRequestTypeDef]
    ) -> ListDataIntegrationsResponseTypeDef:
        """
        Returns a paginated list of DataIntegrations in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/list_data_integrations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#list_data_integrations)
        """

    def list_event_integration_associations(
        self, **kwargs: Unpack[ListEventIntegrationAssociationsRequestTypeDef]
    ) -> ListEventIntegrationAssociationsResponseTypeDef:
        """
        Returns a paginated list of event integration associations in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/list_event_integration_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#list_event_integration_associations)
        """

    def list_event_integrations(
        self, **kwargs: Unpack[ListEventIntegrationsRequestTypeDef]
    ) -> ListEventIntegrationsResponseTypeDef:
        """
        Returns a paginated list of event integrations in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/list_event_integrations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#list_event_integrations)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#untag_resource)
        """

    def update_application(
        self, **kwargs: Unpack[UpdateApplicationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates and persists an Application resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/update_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#update_application)
        """

    def update_data_integration(
        self, **kwargs: Unpack[UpdateDataIntegrationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the description of a DataIntegration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/update_data_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#update_data_integration)
        """

    def update_data_integration_association(
        self, **kwargs: Unpack[UpdateDataIntegrationAssociationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates and persists a DataIntegrationAssociation resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/update_data_integration_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#update_data_integration_association)
        """

    def update_event_integration(
        self, **kwargs: Unpack[UpdateEventIntegrationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the description of an event integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/update_event_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#update_event_integration)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_application_associations"]
    ) -> ListApplicationAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_integration_associations"]
    ) -> ListDataIntegrationAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_integrations"]
    ) -> ListDataIntegrationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_event_integration_associations"]
    ) -> ListEventIntegrationAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_event_integrations"]
    ) -> ListEventIntegrationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client/#get_paginator)
        """
