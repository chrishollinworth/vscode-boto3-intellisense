"""
Main interface for comprehend service.

Usage::

    ```python
    import boto3
    from mypy_boto3_comprehend import (
        Client,
        ComprehendClient,
        ListDocumentClassificationJobsPaginator,
        ListDocumentClassifiersPaginator,
        ListDominantLanguageDetectionJobsPaginator,
        ListEntitiesDetectionJobsPaginator,
        ListEntityRecognizersPaginator,
        ListKeyPhrasesDetectionJobsPaginator,
        ListSentimentDetectionJobsPaginator,
        ListTopicsDetectionJobsPaginator,
    )

    session = boto3.Session()

    client: ComprehendClient = boto3.client("comprehend")
    session_client: ComprehendClient = session.client("comprehend")

    list_document_classification_jobs_paginator: ListDocumentClassificationJobsPaginator = client.get_paginator("list_document_classification_jobs")
    list_document_classifiers_paginator: ListDocumentClassifiersPaginator = client.get_paginator("list_document_classifiers")
    list_dominant_language_detection_jobs_paginator: ListDominantLanguageDetectionJobsPaginator = client.get_paginator("list_dominant_language_detection_jobs")
    list_entities_detection_jobs_paginator: ListEntitiesDetectionJobsPaginator = client.get_paginator("list_entities_detection_jobs")
    list_entity_recognizers_paginator: ListEntityRecognizersPaginator = client.get_paginator("list_entity_recognizers")
    list_key_phrases_detection_jobs_paginator: ListKeyPhrasesDetectionJobsPaginator = client.get_paginator("list_key_phrases_detection_jobs")
    list_sentiment_detection_jobs_paginator: ListSentimentDetectionJobsPaginator = client.get_paginator("list_sentiment_detection_jobs")
    list_topics_detection_jobs_paginator: ListTopicsDetectionJobsPaginator = client.get_paginator("list_topics_detection_jobs")
    ```
"""
from mypy_boto3_comprehend.client import ComprehendClient
from mypy_boto3_comprehend.paginator import (
    ListDocumentClassificationJobsPaginator,
    ListDocumentClassifiersPaginator,
    ListDominantLanguageDetectionJobsPaginator,
    ListEntitiesDetectionJobsPaginator,
    ListEntityRecognizersPaginator,
    ListKeyPhrasesDetectionJobsPaginator,
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
    "ListEntitiesDetectionJobsPaginator",
    "ListEntityRecognizersPaginator",
    "ListKeyPhrasesDetectionJobsPaginator",
    "ListSentimentDetectionJobsPaginator",
    "ListTopicsDetectionJobsPaginator",
)
