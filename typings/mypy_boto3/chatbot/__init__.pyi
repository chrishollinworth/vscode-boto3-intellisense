"""
Main interface for chatbot service.

Usage::

    ```python
    import boto3
    from mypy_boto3_chatbot import (
        ChatbotClient,
        Client,
    )

    session = boto3.Session()

    client: ChatbotClient = boto3.client("chatbot")
    session_client: ChatbotClient = session.client("chatbot")
    ```
"""

from .client import ChatbotClient

Client = ChatbotClient

__all__ = ("ChatbotClient", "Client")
