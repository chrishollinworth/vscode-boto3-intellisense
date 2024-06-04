"""
Type annotations for resiliencehub service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_resiliencehub import ResilienceHubClient
    from mypy_boto3_resiliencehub.paginator import (
        ListAppAssessmentResourceDriftsPaginator,
    )

    client: ResilienceHubClient = boto3.client("resiliencehub")

    list_app_assessment_resource_drifts_paginator: ListAppAssessmentResourceDriftsPaginator = client.get_paginator("list_app_assessment_resource_drifts")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListAppAssessmentResourceDriftsResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListAppAssessmentResourceDriftsPaginator",)

class ListAppAssessmentResourceDriftsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/resiliencehub.html#ResilienceHub.Paginator.ListAppAssessmentResourceDrifts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/paginators.html#listappassessmentresourcedriftspaginator)
    """

    def paginate(
        self, *, assessmentArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAppAssessmentResourceDriftsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/resiliencehub.html#ResilienceHub.Paginator.ListAppAssessmentResourceDrifts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/paginators.html#listappassessmentresourcedriftspaginator)
        """
