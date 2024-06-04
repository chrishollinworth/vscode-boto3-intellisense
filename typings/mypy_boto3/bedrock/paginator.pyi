"""
Type annotations for bedrock service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_bedrock import BedrockClient
    from mypy_boto3_bedrock.paginator import (
        ListCustomModelsPaginator,
        ListEvaluationJobsPaginator,
        ListGuardrailsPaginator,
        ListModelCustomizationJobsPaginator,
        ListProvisionedModelThroughputsPaginator,
    )

    client: BedrockClient = boto3.client("bedrock")

    list_custom_models_paginator: ListCustomModelsPaginator = client.get_paginator("list_custom_models")
    list_evaluation_jobs_paginator: ListEvaluationJobsPaginator = client.get_paginator("list_evaluation_jobs")
    list_guardrails_paginator: ListGuardrailsPaginator = client.get_paginator("list_guardrails")
    list_model_customization_jobs_paginator: ListModelCustomizationJobsPaginator = client.get_paginator("list_model_customization_jobs")
    list_provisioned_model_throughputs_paginator: ListProvisionedModelThroughputsPaginator = client.get_paginator("list_provisioned_model_throughputs")
    ```
"""

import sys
from datetime import datetime
from typing import Iterator, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    EvaluationJobStatusType,
    FineTuningJobStatusType,
    ProvisionedModelStatusType,
    SortOrderType,
)
from .type_defs import (
    ListCustomModelsResponseTypeDef,
    ListEvaluationJobsResponseTypeDef,
    ListGuardrailsResponseTypeDef,
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
    "ListEvaluationJobsPaginator",
    "ListGuardrailsPaginator",
    "ListModelCustomizationJobsPaginator",
    "ListProvisionedModelThroughputsPaginator",
)

class ListCustomModelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock.html#Bedrock.Paginator.ListCustomModels)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock.html#Bedrock.Paginator.ListCustomModels.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listcustommodelspaginator)
        """

class ListEvaluationJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock.html#Bedrock.Paginator.ListEvaluationJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listevaluationjobspaginator)
    """

    def paginate(
        self,
        *,
        creationTimeAfter: Union[datetime, str] = None,
        creationTimeBefore: Union[datetime, str] = None,
        statusEquals: EvaluationJobStatusType = None,
        nameContains: str = None,
        sortBy: Literal["CreationTime"] = None,
        sortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEvaluationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock.html#Bedrock.Paginator.ListEvaluationJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listevaluationjobspaginator)
        """

class ListGuardrailsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock.html#Bedrock.Paginator.ListGuardrails)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listguardrailspaginator)
    """

    def paginate(
        self, *, guardrailIdentifier: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGuardrailsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock.html#Bedrock.Paginator.ListGuardrails.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listguardrailspaginator)
        """

class ListModelCustomizationJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock.html#Bedrock.Paginator.ListModelCustomizationJobs)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock.html#Bedrock.Paginator.ListModelCustomizationJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listmodelcustomizationjobspaginator)
        """

class ListProvisionedModelThroughputsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock.html#Bedrock.Paginator.ListProvisionedModelThroughputs)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock.html#Bedrock.Paginator.ListProvisionedModelThroughputs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listprovisionedmodelthroughputspaginator)
        """
