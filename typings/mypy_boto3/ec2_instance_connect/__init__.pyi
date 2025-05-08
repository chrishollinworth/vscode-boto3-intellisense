"""
Main interface for ec2-instance-connect service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ec2_instance_connect import (
        Client,
        EC2InstanceConnectClient,
    )

    session = Session()
    client: EC2InstanceConnectClient = session.client("ec2-instance-connect")
    ```
"""

from .client import EC2InstanceConnectClient

Client = EC2InstanceConnectClient

__all__ = ("Client", "EC2InstanceConnectClient")
