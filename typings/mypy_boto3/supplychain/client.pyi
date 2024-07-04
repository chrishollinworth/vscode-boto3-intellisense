"""
Type annotations for supplychain service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_supplychain import SupplyChainClient

    client: SupplyChainClient = boto3.client("supplychain")
    ```
"""

from datetime import datetime
from typing import Any, Dict, Type, Union

from botocore.client import BaseClient, ClientMeta

from .literals import DataIntegrationEventTypeType
from .type_defs import (
    CreateBillOfMaterialsImportJobResponseTypeDef,
    GetBillOfMaterialsImportJobResponseTypeDef,
    SendDataIntegrationEventResponseTypeDef,
)

__all__ = ("SupplyChainClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class SupplyChainClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/supplychain.html#SupplyChain.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SupplyChainClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/supplychain.html#SupplyChain.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/supplychain.html#SupplyChain.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client.html#close)
        """

    def create_bill_of_materials_import_job(
        self, *, instanceId: str, s3uri: str, clientToken: str = None
    ) -> CreateBillOfMaterialsImportJobResponseTypeDef:
        """
        CreateBillOfMaterialsImportJob creates an import job for the Product Bill Of
        Materials (BOM) entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/supplychain.html#SupplyChain.Client.create_bill_of_materials_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client.html#create_bill_of_materials_import_job)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/supplychain.html#SupplyChain.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client.html#generate_presigned_url)
        """

    def get_bill_of_materials_import_job(
        self, *, instanceId: str, jobId: str
    ) -> GetBillOfMaterialsImportJobResponseTypeDef:
        """
        Get status and details of a BillOfMaterialsImportJob.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/supplychain.html#SupplyChain.Client.get_bill_of_materials_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client.html#get_bill_of_materials_import_job)
        """

    def send_data_integration_event(
        self,
        *,
        instanceId: str,
        eventType: DataIntegrationEventTypeType,
        data: str,
        eventGroupId: str,
        eventTimestamp: Union[datetime, str] = None,
        clientToken: str = None
    ) -> SendDataIntegrationEventResponseTypeDef:
        """
        Send transactional data events with real-time data for analysis or monitoring.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/supplychain.html#SupplyChain.Client.send_data_integration_event)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client.html#send_data_integration_event)
        """
