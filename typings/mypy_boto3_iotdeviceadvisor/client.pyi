"""
Main interface for iotdeviceadvisor service client

Usage::

    ```python
    import boto3
    from mypy_boto3_iotdeviceadvisor import IoTDeviceAdvisorClient

    client: IoTDeviceAdvisorClient = boto3.client("iotdeviceadvisor")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_iotdeviceadvisor.type_defs import (
    CreateSuiteDefinitionResponseTypeDef,
    GetSuiteDefinitionResponseTypeDef,
    GetSuiteRunReportResponseTypeDef,
    GetSuiteRunResponseTypeDef,
    ListSuiteDefinitionsResponseTypeDef,
    ListSuiteRunsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTestCasesResponseTypeDef,
    StartSuiteRunResponseTypeDef,
    SuiteDefinitionConfigurationTypeDef,
    SuiteRunConfigurationTypeDef,
    UpdateSuiteDefinitionResponseTypeDef,
)

__all__ = ("IoTDeviceAdvisorClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class IoTDeviceAdvisorClient:
    """
    [IoTDeviceAdvisor.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.can_paginate)
        """

    def create_suite_definition(
        self,
        suiteDefinitionConfiguration: "SuiteDefinitionConfigurationTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> CreateSuiteDefinitionResponseTypeDef:
        """
        [Client.create_suite_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.create_suite_definition)
        """

    def delete_suite_definition(self, suiteDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_suite_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.delete_suite_definition)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.generate_presigned_url)
        """

    def get_suite_definition(
        self, suiteDefinitionId: str, suiteDefinitionVersion: str = None
    ) -> GetSuiteDefinitionResponseTypeDef:
        """
        [Client.get_suite_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.get_suite_definition)
        """

    def get_suite_run(self, suiteDefinitionId: str, suiteRunId: str) -> GetSuiteRunResponseTypeDef:
        """
        [Client.get_suite_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.get_suite_run)
        """

    def get_suite_run_report(
        self, suiteDefinitionId: str, suiteRunId: str
    ) -> GetSuiteRunReportResponseTypeDef:
        """
        [Client.get_suite_run_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.get_suite_run_report)
        """

    def list_suite_definitions(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListSuiteDefinitionsResponseTypeDef:
        """
        [Client.list_suite_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.list_suite_definitions)
        """

    def list_suite_runs(
        self,
        suiteDefinitionId: str = None,
        suiteDefinitionVersion: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListSuiteRunsResponseTypeDef:
        """
        [Client.list_suite_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.list_suite_runs)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.list_tags_for_resource)
        """

    def list_test_cases(
        self, intendedForQualification: bool = None, maxResults: int = None, nextToken: str = None
    ) -> ListTestCasesResponseTypeDef:
        """
        [Client.list_test_cases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.list_test_cases)
        """

    def start_suite_run(
        self,
        suiteDefinitionId: str,
        suiteDefinitionVersion: str = None,
        suiteRunConfiguration: "SuiteRunConfigurationTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> StartSuiteRunResponseTypeDef:
        """
        [Client.start_suite_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.start_suite_run)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.untag_resource)
        """

    def update_suite_definition(
        self,
        suiteDefinitionId: str,
        suiteDefinitionConfiguration: "SuiteDefinitionConfigurationTypeDef" = None,
    ) -> UpdateSuiteDefinitionResponseTypeDef:
        """
        [Client.update_suite_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.update_suite_definition)
        """
