# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for migrationhub-config service client

Usage::

    ```python
    import boto3
    from mypy_boto3_migrationhub_config import MigrationHubConfigClient

    client: MigrationHubConfigClient = boto3.client("migrationhub-config")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from mypy_boto3_migrationhub_config.type_defs import (
    CreateHomeRegionControlResultTypeDef,
    DescribeHomeRegionControlsResultTypeDef,
    GetHomeRegionResultTypeDef,
    TargetTypeDef,
)

__all__ = ("MigrationHubConfigClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DryRunOperation: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class MigrationHubConfigClient:
    """
    [MigrationHubConfig.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/migrationhub-config.html#MigrationHubConfig.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/migrationhub-config.html#MigrationHubConfig.Client.can_paginate)
        """

    def create_home_region_control(
        self, HomeRegion: str, Target: "TargetTypeDef", DryRun: bool = None
    ) -> CreateHomeRegionControlResultTypeDef:
        """
        [Client.create_home_region_control documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/migrationhub-config.html#MigrationHubConfig.Client.create_home_region_control)
        """

    def describe_home_region_controls(
        self,
        ControlId: str = None,
        HomeRegion: str = None,
        Target: "TargetTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeHomeRegionControlsResultTypeDef:
        """
        [Client.describe_home_region_controls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/migrationhub-config.html#MigrationHubConfig.Client.describe_home_region_controls)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/migrationhub-config.html#MigrationHubConfig.Client.generate_presigned_url)
        """

    def get_home_region(self) -> GetHomeRegionResultTypeDef:
        """
        [Client.get_home_region documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/migrationhub-config.html#MigrationHubConfig.Client.get_home_region)
        """
