"""
Type annotations for ssm-quicksetup service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ssm_quicksetup.client import SystemsManagerQuickSetupClient

    session = Session()
    client: SystemsManagerQuickSetupClient = session.client("ssm-quicksetup")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListConfigurationManagersPaginator, ListConfigurationsPaginator
from .type_defs import (
    CreateConfigurationManagerInputTypeDef,
    CreateConfigurationManagerOutputTypeDef,
    DeleteConfigurationManagerInputTypeDef,
    EmptyResponseMetadataTypeDef,
    GetConfigurationInputTypeDef,
    GetConfigurationManagerInputTypeDef,
    GetConfigurationManagerOutputTypeDef,
    GetConfigurationOutputTypeDef,
    GetServiceSettingsOutputTypeDef,
    ListConfigurationManagersInputTypeDef,
    ListConfigurationManagersOutputTypeDef,
    ListConfigurationsInputTypeDef,
    ListConfigurationsOutputTypeDef,
    ListQuickSetupTypesOutputTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateConfigurationDefinitionInputTypeDef,
    UpdateConfigurationManagerInputTypeDef,
    UpdateServiceSettingsInputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("SystemsManagerQuickSetupClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class SystemsManagerQuickSetupClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup.html#SystemsManagerQuickSetup.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SystemsManagerQuickSetupClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup.html#SystemsManagerQuickSetup.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#generate_presigned_url)
        """

    def create_configuration_manager(
        self, **kwargs: Unpack[CreateConfigurationManagerInputTypeDef]
    ) -> CreateConfigurationManagerOutputTypeDef:
        """
        Creates a Quick Setup configuration manager resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/create_configuration_manager.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#create_configuration_manager)
        """

    def delete_configuration_manager(
        self, **kwargs: Unpack[DeleteConfigurationManagerInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a configuration manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/delete_configuration_manager.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#delete_configuration_manager)
        """

    def get_configuration(
        self, **kwargs: Unpack[GetConfigurationInputTypeDef]
    ) -> GetConfigurationOutputTypeDef:
        """
        Returns details about the specified configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/get_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#get_configuration)
        """

    def get_configuration_manager(
        self, **kwargs: Unpack[GetConfigurationManagerInputTypeDef]
    ) -> GetConfigurationManagerOutputTypeDef:
        """
        Returns a configuration manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/get_configuration_manager.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#get_configuration_manager)
        """

    def get_service_settings(self) -> GetServiceSettingsOutputTypeDef:
        """
        Returns settings configured for Quick Setup in the requesting Amazon Web
        Services account and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/get_service_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#get_service_settings)
        """

    def list_configuration_managers(
        self, **kwargs: Unpack[ListConfigurationManagersInputTypeDef]
    ) -> ListConfigurationManagersOutputTypeDef:
        """
        Returns Quick Setup configuration managers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/list_configuration_managers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#list_configuration_managers)
        """

    def list_configurations(
        self, **kwargs: Unpack[ListConfigurationsInputTypeDef]
    ) -> ListConfigurationsOutputTypeDef:
        """
        Returns configurations deployed by Quick Setup in the requesting Amazon Web
        Services account and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/list_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#list_configurations)
        """

    def list_quick_setup_types(self) -> ListQuickSetupTypesOutputTypeDef:
        """
        Returns the available Quick Setup types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/list_quick_setup_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#list_quick_setup_types)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns tags assigned to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#list_tags_for_resource)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Assigns key-value pairs of metadata to Amazon Web Services resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#untag_resource)
        """

    def update_configuration_definition(
        self, **kwargs: Unpack[UpdateConfigurationDefinitionInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a Quick Setup configuration definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/update_configuration_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#update_configuration_definition)
        """

    def update_configuration_manager(
        self, **kwargs: Unpack[UpdateConfigurationManagerInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a Quick Setup configuration manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/update_configuration_manager.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#update_configuration_manager)
        """

    def update_service_settings(
        self, **kwargs: Unpack[UpdateServiceSettingsInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates settings configured for Quick Setup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/update_service_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#update_service_settings)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_configuration_managers"]
    ) -> ListConfigurationManagersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_configurations"]
    ) -> ListConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/client/#get_paginator)
        """
