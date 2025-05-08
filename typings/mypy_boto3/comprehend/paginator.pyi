"""
Type annotations for comprehend service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_comprehend.client import ComprehendClient
    from mypy_boto3_comprehend.paginator import (
        ListDocumentClassificationJobsPaginator,
        ListDocumentClassifiersPaginator,
        ListDominantLanguageDetectionJobsPaginator,
        ListEndpointsPaginator,
        ListEntitiesDetectionJobsPaginator,
        ListEntityRecognizersPaginator,
        ListKeyPhrasesDetectionJobsPaginator,
        ListPiiEntitiesDetectionJobsPaginator,
        ListSentimentDetectionJobsPaginator,
        ListTopicsDetectionJobsPaginator,
    )

    session = Session()
    client: ComprehendClient = session.client("comprehend")

    list_document_classification_jobs_paginator: ListDocumentClassificationJobsPaginator = client.get_paginator("list_document_classification_jobs")
    list_document_classifiers_paginator: ListDocumentClassifiersPaginator = client.get_paginator("list_document_classifiers")
    list_dominant_language_detection_jobs_paginator: ListDominantLanguageDetectionJobsPaginator = client.get_paginator("list_dominant_language_detection_jobs")
    list_endpoints_paginator: ListEndpointsPaginator = client.get_paginator("list_endpoints")
    list_entities_detection_jobs_paginator: ListEntitiesDetectionJobsPaginator = client.get_paginator("list_entities_detection_jobs")
    list_entity_recognizers_paginator: ListEntityRecognizersPaginator = client.get_paginator("list_entity_recognizers")
    list_key_phrases_detection_jobs_paginator: ListKeyPhrasesDetectionJobsPaginator = client.get_paginator("list_key_phrases_detection_jobs")
    list_pii_entities_detection_jobs_paginator: ListPiiEntitiesDetectionJobsPaginator = client.get_paginator("list_pii_entities_detection_jobs")
    list_sentiment_detection_jobs_paginator: ListSentimentDetectionJobsPaginator = client.get_paginator("list_sentiment_detection_jobs")
    list_topics_detection_jobs_paginator: ListTopicsDetectionJobsPaginator = client.get_paginator("list_topics_detection_jobs")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDocumentClassificationJobsRequestPaginateTypeDef,
    ListDocumentClassificationJobsResponseTypeDef,
    ListDocumentClassifiersRequestPaginateTypeDef,
    ListDocumentClassifiersResponseTypeDef,
    ListDominantLanguageDetectionJobsRequestPaginateTypeDef,
    ListDominantLanguageDetectionJobsResponseTypeDef,
    ListEndpointsRequestPaginateTypeDef,
    ListEndpointsResponseTypeDef,
    ListEntitiesDetectionJobsRequestPaginateTypeDef,
    ListEntitiesDetectionJobsResponseTypeDef,
    ListEntityRecognizersRequestPaginateTypeDef,
    ListEntityRecognizersResponseTypeDef,
    ListKeyPhrasesDetectionJobsRequestPaginateTypeDef,
    ListKeyPhrasesDetectionJobsResponseTypeDef,
    ListPiiEntitiesDetectionJobsRequestPaginateTypeDef,
    ListPiiEntitiesDetectionJobsResponseTypeDef,
    ListSentimentDetectionJobsRequestPaginateTypeDef,
    ListSentimentDetectionJobsResponseTypeDef,
    ListTopicsDetectionJobsRequestPaginateTypeDef,
    ListTopicsDetectionJobsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListDocumentClassificationJobsPaginator",
    "ListDocumentClassifiersPaginator",
    "ListDominantLanguageDetectionJobsPaginator",
    "ListEndpointsPaginator",
    "ListEntitiesDetectionJobsPaginator",
    "ListEntityRecognizersPaginator",
    "ListKeyPhrasesDetectionJobsPaginator",
    "ListPiiEntitiesDetectionJobsPaginator",
    "ListSentimentDetectionJobsPaginator",
    "ListTopicsDetectionJobsPaginator",
)

if TYPE_CHECKING:
    _ListDocumentClassificationJobsPaginatorBase = Paginator[
        ListDocumentClassificationJobsResponseTypeDef
    ]
else:
    _ListDocumentClassificationJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDocumentClassificationJobsPaginator(_ListDocumentClassificationJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListDocumentClassificationJobs.html#Comprehend.Paginator.ListDocumentClassificationJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listdocumentclassificationjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDocumentClassificationJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListDocumentClassificationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListDocumentClassificationJobs.html#Comprehend.Paginator.ListDocumentClassificationJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listdocumentclassificationjobspaginator)
        """

if TYPE_CHECKING:
    _ListDocumentClassifiersPaginatorBase = Paginator[ListDocumentClassifiersResponseTypeDef]
else:
    _ListDocumentClassifiersPaginatorBase = Paginator  # type: ignore[assignment]

class ListDocumentClassifiersPaginator(_ListDocumentClassifiersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListDocumentClassifiers.html#Comprehend.Paginator.ListDocumentClassifiers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listdocumentclassifierspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDocumentClassifiersRequestPaginateTypeDef]
    ) -> PageIterator[ListDocumentClassifiersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListDocumentClassifiers.html#Comprehend.Paginator.ListDocumentClassifiers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listdocumentclassifierspaginator)
        """

if TYPE_CHECKING:
    _ListDominantLanguageDetectionJobsPaginatorBase = Paginator[
        ListDominantLanguageDetectionJobsResponseTypeDef
    ]
else:
    _ListDominantLanguageDetectionJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDominantLanguageDetectionJobsPaginator(_ListDominantLanguageDetectionJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListDominantLanguageDetectionJobs.html#Comprehend.Paginator.ListDominantLanguageDetectionJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listdominantlanguagedetectionjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDominantLanguageDetectionJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListDominantLanguageDetectionJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListDominantLanguageDetectionJobs.html#Comprehend.Paginator.ListDominantLanguageDetectionJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listdominantlanguagedetectionjobspaginator)
        """

if TYPE_CHECKING:
    _ListEndpointsPaginatorBase = Paginator[ListEndpointsResponseTypeDef]
else:
    _ListEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEndpointsPaginator(_ListEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListEndpoints.html#Comprehend.Paginator.ListEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[ListEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListEndpoints.html#Comprehend.Paginator.ListEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listendpointspaginator)
        """

if TYPE_CHECKING:
    _ListEntitiesDetectionJobsPaginatorBase = Paginator[ListEntitiesDetectionJobsResponseTypeDef]
else:
    _ListEntitiesDetectionJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEntitiesDetectionJobsPaginator(_ListEntitiesDetectionJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListEntitiesDetectionJobs.html#Comprehend.Paginator.ListEntitiesDetectionJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listentitiesdetectionjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEntitiesDetectionJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListEntitiesDetectionJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListEntitiesDetectionJobs.html#Comprehend.Paginator.ListEntitiesDetectionJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listentitiesdetectionjobspaginator)
        """

if TYPE_CHECKING:
    _ListEntityRecognizersPaginatorBase = Paginator[ListEntityRecognizersResponseTypeDef]
else:
    _ListEntityRecognizersPaginatorBase = Paginator  # type: ignore[assignment]

class ListEntityRecognizersPaginator(_ListEntityRecognizersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListEntityRecognizers.html#Comprehend.Paginator.ListEntityRecognizers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listentityrecognizerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEntityRecognizersRequestPaginateTypeDef]
    ) -> PageIterator[ListEntityRecognizersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListEntityRecognizers.html#Comprehend.Paginator.ListEntityRecognizers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listentityrecognizerspaginator)
        """

if TYPE_CHECKING:
    _ListKeyPhrasesDetectionJobsPaginatorBase = Paginator[
        ListKeyPhrasesDetectionJobsResponseTypeDef
    ]
else:
    _ListKeyPhrasesDetectionJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListKeyPhrasesDetectionJobsPaginator(_ListKeyPhrasesDetectionJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListKeyPhrasesDetectionJobs.html#Comprehend.Paginator.ListKeyPhrasesDetectionJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listkeyphrasesdetectionjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListKeyPhrasesDetectionJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListKeyPhrasesDetectionJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListKeyPhrasesDetectionJobs.html#Comprehend.Paginator.ListKeyPhrasesDetectionJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listkeyphrasesdetectionjobspaginator)
        """

if TYPE_CHECKING:
    _ListPiiEntitiesDetectionJobsPaginatorBase = Paginator[
        ListPiiEntitiesDetectionJobsResponseTypeDef
    ]
else:
    _ListPiiEntitiesDetectionJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPiiEntitiesDetectionJobsPaginator(_ListPiiEntitiesDetectionJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListPiiEntitiesDetectionJobs.html#Comprehend.Paginator.ListPiiEntitiesDetectionJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listpiientitiesdetectionjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPiiEntitiesDetectionJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListPiiEntitiesDetectionJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListPiiEntitiesDetectionJobs.html#Comprehend.Paginator.ListPiiEntitiesDetectionJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listpiientitiesdetectionjobspaginator)
        """

if TYPE_CHECKING:
    _ListSentimentDetectionJobsPaginatorBase = Paginator[ListSentimentDetectionJobsResponseTypeDef]
else:
    _ListSentimentDetectionJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSentimentDetectionJobsPaginator(_ListSentimentDetectionJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListSentimentDetectionJobs.html#Comprehend.Paginator.ListSentimentDetectionJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listsentimentdetectionjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSentimentDetectionJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListSentimentDetectionJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListSentimentDetectionJobs.html#Comprehend.Paginator.ListSentimentDetectionJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listsentimentdetectionjobspaginator)
        """

if TYPE_CHECKING:
    _ListTopicsDetectionJobsPaginatorBase = Paginator[ListTopicsDetectionJobsResponseTypeDef]
else:
    _ListTopicsDetectionJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTopicsDetectionJobsPaginator(_ListTopicsDetectionJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListTopicsDetectionJobs.html#Comprehend.Paginator.ListTopicsDetectionJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listtopicsdetectionjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTopicsDetectionJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListTopicsDetectionJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/paginator/ListTopicsDetectionJobs.html#Comprehend.Paginator.ListTopicsDetectionJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators/#listtopicsdetectionjobspaginator)
        """
