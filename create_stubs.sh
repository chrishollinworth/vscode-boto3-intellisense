mkdir -p typings/boto3
mkdir -p typings/botocore

cp /opt/venv/lib/python3.*/site-packages/boto3-stubs/__init__.pyi typings/boto3/__init__.pyi
cp /opt/venv/lib/python3.*/site-packages/boto3-stubs/compat.pyi typings/boto3/compat.pyi
cp /opt/venv/lib/python3.*/site-packages/boto3-stubs/exceptions.pyi typings/boto3/exceptions.pyi
cp /opt/venv/lib/python3.*/site-packages/boto3-stubs/session.pyi typings/boto3/session.pyi
cp /opt/venv/lib/python3.*/site-packages/boto3-stubs/utils.pyi typings/boto3/utils.pyi
cp /opt/venv/lib/python3.*/site-packages/botocore-stubs/config.pyi typings/botocore/config.pyi

cat services2.txt | while IFS=$' \t\n\r' read -r line || [[ -n "$line" ]]; do

    if [ "$line" != "lambda" ]; then
        # install generated stubs for implicit type inference on boto3.client/boto3.resource
        mkdir -p typings/mypy_boto3/$line
        for f in __init__ client literals paginator service_resource waiter type_defs; do \
        cp /opt/venv/lib/python3.*/site-packages/mypy_boto3_$line/$f.pyi typings/mypy_boto3/$line/$f.pyi; done
    else
        # install generated stubs for implicit type inference on boto3.client/boto3.resource
        mkdir -p typings/mypy_boto3/lambda_
        for f in __init__ client literals paginator service_resource waiter type_defs; do \
        cp /opt/venv/lib/python3.*/site-packages/mypy_boto3/lambda_/$f.pyi typings/mypy_boto3/lambda_/$f.pyi; done
    fi

    # install packaged stubs for explicit type annotation (also used by the generated stubs)
    mkdir -p typings/mypy_boto3_$line
    for f2 in __init__ client literals paginator service_resource waiter type_defs; do \
    cp /opt/venv/lib/python3.*/site-packages/mypy_boto3_$line/$f2.pyi typings/mypy_boto3_$line/$f2.pyi;
    done
done