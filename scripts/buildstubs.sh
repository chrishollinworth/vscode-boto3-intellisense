# might need to sudo rm -Rf typings/ sometimes
sudo apt install python3-pip
pip3 install -U virtualenv
alias python='python3'

python3 -m venv buildstubs_env
source buildstubs_env/bin/activate
pip3 install --upgrade boto3 botocore

rm -rf mypy_boto3_builder
git clone --depth 1 https://github.com/chrishollinworth/mypy_boto3_builder.git
cd mypy_boto3_builder

./scripts/build.sh
./scripts/install.sh

cd ./../scripts

buildstubs_env/bin/python -m mypy_boto3

# workaround for https://github.com/vemel/mypy_boto3_builder/issues/39
rm -rf ./../typings/boto3
mkdir -p ./../typings/boto3
cp buildstubs_env/lib/python*/site-packages/mypy_boto3/boto3_init_gen.py ./../typings/boto3/__init__.pyi

cd ./../scripts
cat services.txt | while IFS=$' \t\n\r' read -r line || [[ -n "$line" ]]; do 
    
    if [ "$line" != "lambda" ]; then 
        # install generated stubs for implicit type inference on boto3.client/boto3.resource
        mkdir -p ./../typings/mypy_boto3/$line
        for f in __init__ client paginator service_resource waiter type_defs; do \
        cp buildstubs_env/lib/python*/site-packages/mypy_boto3/$line/$f.py ./../typings/mypy_boto3/$line/$f.pyi; done
    else
        # install generated stubs for implicit type inference on boto3.client/boto3.resource
        mkdir -p ./../typings/mypy_boto3/lambda_
        for f in __init__ client paginator service_resource waiter type_defs; do \
        cp buildstubs_env/lib/python*/site-packages/mypy_boto3/lambda_/$f.py ./../typings/mypy_boto3/lambda_/$f.pyi; done
    fi

    # install packaged stubs for explicit type annotation (also used by the generated stubs)
    mkdir -p ./../typings/mypy_boto3_$line
    for f2 in __init__ client paginator service_resource waiter type_defs; do \  
    cp buildstubs_env/lib/python*/site-packages/mypy_boto3_$line/$f2.py ./../typings/mypy_boto3_$line/$f2.pyi; 
    done
done
