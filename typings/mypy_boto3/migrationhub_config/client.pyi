"""
Type annotations for migrationhub-config service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhub_config/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_migrationhub_config.client import MigrationHubConfigClient

    session = Session()
    client: MigrationHubConfigClient = session.client("migrationhub-config")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CreateHomeRegionControlRequestTypeDef,
    CreateHomeRegionControlResultTypeDef,
    DeleteHomeRegionControlRequestTypeDef,
    DescribeHomeRegionControlsRequestTypeDef,
    DescribeHomeRegionControlsResultTypeDef,
    GetHomeRegionResultTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("MigrationHubConfigClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DryRunOperation: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class MigrationHubConfigClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config.html#MigrationHubConfig.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhub_config/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MigrationHubConfigClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config.html#MigrationHubConfig.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhub_config/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhub_config/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhub_config/client/#generate_presigned_url)
        """

    def create_home_region_control(
        self, **kwargs: Unpack[CreateHomeRegionControlRequestTypeDef]
    ) -> CreateHomeRegionControlResultTypeDef:
        """
        This API sets up the home region for the calling account only.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config/client/create_home_region_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhub_config/client/#create_home_region_control)
        """

    def delete_home_region_control(
        self, **kwargs: Unpack[DeleteHomeRegionControlRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This operation deletes the home region configuration for the calling account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config/client/delete_home_region_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhub_config/client/#delete_home_region_control)
        """

    def describe_home_region_controls(
        self, **kwargs: Unpack[DescribeHomeRegionControlsRequestTypeDef]
    ) -> DescribeHomeRegionControlsResultTypeDef:
        """
        This API permits filtering on the <code>ControlId</code> and
        <code>HomeRegion</code> fields.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config/client/describe_home_region_controls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhub_config/client/#describe_home_region_controls)
        """

    def get_home_region(self) -> GetHomeRegionResultTypeDef:
        """
        Returns the calling account's home region, if configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config/client/get_home_region.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhub_config/client/#get_home_region)
        """
