"""
Type annotations for appintegrations service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/literals.html)

Usage::

    ```python
    from mypy_boto3_appintegrations.literals import ListApplicationAssociationsPaginatorName

    data: ListApplicationAssociationsPaginatorName = "list_application_associations"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListApplicationAssociationsPaginatorName",
    "ListApplicationsPaginatorName",
    "ListDataIntegrationAssociationsPaginatorName",
    "ListDataIntegrationsPaginatorName",
    "ListEventIntegrationAssociationsPaginatorName",
    "ListEventIntegrationsPaginatorName",
)

ListApplicationAssociationsPaginatorName = Literal["list_application_associations"]
ListApplicationsPaginatorName = Literal["list_applications"]
ListDataIntegrationAssociationsPaginatorName = Literal["list_data_integration_associations"]
ListDataIntegrationsPaginatorName = Literal["list_data_integrations"]
ListEventIntegrationAssociationsPaginatorName = Literal["list_event_integration_associations"]
ListEventIntegrationsPaginatorName = Literal["list_event_integrations"]
