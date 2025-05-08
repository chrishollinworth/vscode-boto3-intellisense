"""
Type annotations for iotdeviceadvisor service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iotdeviceadvisor.client import IoTDeviceAdvisorClient

    session = Session()
    client: IoTDeviceAdvisorClient = session.client("iotdeviceadvisor")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CreateSuiteDefinitionRequestTypeDef,
    CreateSuiteDefinitionResponseTypeDef,
    DeleteSuiteDefinitionRequestTypeDef,
    GetEndpointRequestTypeDef,
    GetEndpointResponseTypeDef,
    GetSuiteDefinitionRequestTypeDef,
    GetSuiteDefinitionResponseTypeDef,
    GetSuiteRunReportRequestTypeDef,
    GetSuiteRunReportResponseTypeDef,
    GetSuiteRunRequestTypeDef,
    GetSuiteRunResponseTypeDef,
    ListSuiteDefinitionsRequestTypeDef,
    ListSuiteDefinitionsResponseTypeDef,
    ListSuiteRunsRequestTypeDef,
    ListSuiteRunsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartSuiteRunRequestTypeDef,
    StartSuiteRunResponseTypeDef,
    StopSuiteRunRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateSuiteDefinitionRequestTypeDef,
    UpdateSuiteDefinitionResponseTypeDef,
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

__all__ = ("IoTDeviceAdvisorClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class IoTDeviceAdvisorClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTDeviceAdvisorClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#generate_presigned_url)
        """

    def create_suite_definition(
        self, **kwargs: Unpack[CreateSuiteDefinitionRequestTypeDef]
    ) -> CreateSuiteDefinitionResponseTypeDef:
        """
        Creates a Device Advisor test suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor/client/create_suite_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#create_suite_definition)
        """

    def delete_suite_definition(
        self, **kwargs: Unpack[DeleteSuiteDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a Device Advisor test suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor/client/delete_suite_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#delete_suite_definition)
        """

    def get_endpoint(
        self, **kwargs: Unpack[GetEndpointRequestTypeDef]
    ) -> GetEndpointResponseTypeDef:
        """
        Gets information about an Device Advisor endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor/client/get_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#get_endpoint)
        """

    def get_suite_definition(
        self, **kwargs: Unpack[GetSuiteDefinitionRequestTypeDef]
    ) -> GetSuiteDefinitionResponseTypeDef:
        """
        Gets information about a Device Advisor test suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor/client/get_suite_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#get_suite_definition)
        """

    def get_suite_run(
        self, **kwargs: Unpack[GetSuiteRunRequestTypeDef]
    ) -> GetSuiteRunResponseTypeDef:
        """
        Gets information about a Device Advisor test suite run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor/client/get_suite_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#get_suite_run)
        """

    def get_suite_run_report(
        self, **kwargs: Unpack[GetSuiteRunReportRequestTypeDef]
    ) -> GetSuiteRunReportResponseTypeDef:
        """
        Gets a report download link for a successful Device Advisor qualifying test
        suite run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor/client/get_suite_run_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#get_suite_run_report)
        """

    def list_suite_definitions(
        self, **kwargs: Unpack[ListSuiteDefinitionsRequestTypeDef]
    ) -> ListSuiteDefinitionsResponseTypeDef:
        """
        Lists the Device Advisor test suites you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor/client/list_suite_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#list_suite_definitions)
        """

    def list_suite_runs(
        self, **kwargs: Unpack[ListSuiteRunsRequestTypeDef]
    ) -> ListSuiteRunsResponseTypeDef:
        """
        Lists runs of the specified Device Advisor test suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor/client/list_suite_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#list_suite_runs)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags attached to an IoT Device Advisor resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#list_tags_for_resource)
        """

    def start_suite_run(
        self, **kwargs: Unpack[StartSuiteRunRequestTypeDef]
    ) -> StartSuiteRunResponseTypeDef:
        """
        Starts a Device Advisor test suite run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor/client/start_suite_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#start_suite_run)
        """

    def stop_suite_run(self, **kwargs: Unpack[StopSuiteRunRequestTypeDef]) -> Dict[str, Any]:
        """
        Stops a Device Advisor test suite run that is currently running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor/client/stop_suite_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#stop_suite_run)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds to and modifies existing tags of an IoT Device Advisor resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from an IoT Device Advisor resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#untag_resource)
        """

    def update_suite_definition(
        self, **kwargs: Unpack[UpdateSuiteDefinitionRequestTypeDef]
    ) -> UpdateSuiteDefinitionResponseTypeDef:
        """
        Updates a Device Advisor test suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor/client/update_suite_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client/#update_suite_definition)
        """
