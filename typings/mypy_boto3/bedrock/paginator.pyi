"""
Type annotations for bedrock service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_bedrock import BedrockClient
    from mypy_boto3_bedrock.paginator import (
        ListCustomModelsPaginator,
        ListModelCustomizationJobsPaginator,
        ListProvisionedModelThroughputsPaginator,
    )

    client: BedrockClient = boto3.client("bedrock")

    list_custom_models_paginator: ListCustomModelsPaginator = client.get_paginator("list_custom_models")
    list_model_customization_jobs_paginator: ListModelCustomizationJobsPaginator = client.get_paginator("list_model_customization_jobs")
    list_provisioned_model_throughputs_paginator: ListProvisionedModelThroughputsPaginator = client.get_paginator("list_provisioned_model_throughputs")
    ```
"""
import sys
from datetime import datetime
from typing import Iterator, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import FineTuningJobStatusType, ProvisionedModelStatusType, SortOrderType
from .type_defs import (
    ListCustomModelsResponseTypeDef,
    ListModelCustomizationJobsResponseTypeDef,
    ListProvisionedModelThroughputsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListCustomModelsPaginator",
    "ListModelCustomizationJobsPaginator",
    "ListProvisionedModelThroughputsPaginator",
)

class ListCustomModelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/bedrock.html#Bedrock.Paginator.ListCustomModels)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listcustommodelspaginator)
    """

    def paginate(
        self,
        *,
        creationTimeBefore: Union[datetime, str] = None,
        creationTimeAfter: Union[datetime, str] = None,
        nameContains: str = None,
        baseModelArnEquals: str = None,
        foundationModelArnEquals: str = None,
        sortBy: Literal["CreationTime"] = None,
        sortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCustomModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/bedrock.html#Bedrock.Paginator.ListCustomModels.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listcustommodelspaginator)
        """

class ListModelCustomizationJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/bedrock.html#Bedrock.Paginator.ListModelCustomizationJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listmodelcustomizationjobspaginator)
    """

    def paginate(
        self,
        *,
        creationTimeAfter: Union[datetime, str] = None,
        creationTimeBefore: Union[datetime, str] = None,
        statusEquals: FineTuningJobStatusType = None,
        nameContains: str = None,
        sortBy: Literal["CreationTime"] = None,
        sortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListModelCustomizationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/bedrock.html#Bedrock.Paginator.ListModelCustomizationJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listmodelcustomizationjobspaginator)
        """

class ListProvisionedModelThroughputsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/bedrock.html#Bedrock.Paginator.ListProvisionedModelThroughputs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listprovisionedmodelthroughputspaginator)
    """

    def paginate(
        self,
        *,
        creationTimeAfter: Union[datetime, str] = None,
        creationTimeBefore: Union[datetime, str] = None,
        statusEquals: ProvisionedModelStatusType = None,
        modelArnEquals: str = None,
        nameContains: str = None,
        sortBy: Literal["CreationTime"] = None,
        sortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProvisionedModelThroughputsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/bedrock.html#Bedrock.Paginator.ListProvisionedModelThroughputs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listprovisionedmodelthroughputspaginator)
        """
