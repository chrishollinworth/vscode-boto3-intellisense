"""
Main interface for comprehend service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_comprehend import (
        Client,
        ComprehendClient,
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

from .client import ComprehendClient
from .paginator import (
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

Client = ComprehendClient

__all__ = (
    "Client",
    "ComprehendClient",
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
