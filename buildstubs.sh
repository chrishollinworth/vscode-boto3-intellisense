sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget

sudo apt install -y python3-pip
pip3 install virtualenv

sudo rm -Rf  buildstubs_env

virtualenv buildstubs_env
source buildstubs_env/bin/activate
pip3 install --upgrade boto3 botocore jinja2 pyparsing black mdformat isort

git clone https://github.com/chrishollinworth/mypy_boto3_builder.git
cd mypy_boto3_builder

./scripts/build.sh
./scripts/install.sh

cd ..

sudo rm -Rf typings

mkdir -p typings/boto3
mkdir -p typings/botocore


cp buildstubs_env/lib/python3.9/site-packages/boto3-stubs/__init__.pyi typings/boto3/__init__.pyi
cp buildstubs_env/lib/python3.9/site-packages/boto3-stubs/compat.pyi typings/boto3/compat.pyi
cp buildstubs_env/lib/python3.9/site-packages/boto3-stubs/exceptions.pyi typings/boto3/exceptions.pyi
cp buildstubs_env/lib/python3.9/site-packages/boto3-stubs/session.pyi typings/boto3/session.pyi
cp buildstubs_env/lib/python3.9/site-packages/boto3-stubs/utils.pyi typings/boto3/utils.pyi
cp buildstubs_env/lib/python3.9/site-packages/botocore-stubs/config.pyi typings/botocore/config.pyi

cat services.txt | while IFS=$' \t\n\r' read -r line || [[ -n "$line" ]]; do 
   
    if [ "$line" != "lambda" ]; then 
        # install generated stubs for implicit type inference on boto3.client/boto3.resource
        mkdir -p typings/mypy_boto3/$line
        for f in __init__ client literals paginator service_resource waiter type_defs; do \
        cp buildstubs_env/lib/python3.9/site-packages/mypy_boto3_$line/$f.pyi typings/mypy_boto3/$line/$f.pyi; done
    else
        # install generated stubs for implicit type inference on boto3.client/boto3.resource
        mkdir -p typings/mypy_boto3/lambda_
        for f in __init__ client literals paginator service_resource waiter type_defs; do \
        cp buildstubs_env/lib/python3.9/site-packages/mypy_boto3/lambda_/$f.pyi typings/mypy_boto3/lambda_/$f.pyi; done
    fi

    # install packaged stubs for explicit type annotation (also used by the generated stubs)
    mkdir -p typings/mypy_boto3_$line
    for f2 in __init__ client literals paginator service_resource waiter type_defs; do \  
    cp buildstubs_env/lib/python3.9/site-packages/mypy_boto3_$line/$f2.pyi typings/mypy_boto3_$line/$f2.pyi; 
    done
done
