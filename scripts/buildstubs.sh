pip3 install -U virtualenv

python3 -m venv buildstubs_env
source buildstubs_env/bin/activate
pip3 install boto3-stubs[all]

buildstubs_env/bin/python -m mypy_boto3

# workaround for https://github.com/vemel/mypy_boto3_builder/issues/39
mkdir -p ./../typings/boto3
cp buildstubs_env/lib/python*/site-packages/mypy_boto3/boto3_init_gen.py ./../typings/boto3/__init__.pyi

cat services.txt | while IFS=$' \t\n\r' read -r line || [[ -n "$line" ]]; do 
    
    # install generated stubs for implicit type inference on boto3.client/boto3.resource
	mkdir -p ./../typings/mypy_boto3/$line
	for f in __init__ client paginator service_resource waiter type_defs; do \
	cp buildstubs_env/lib/python*/site-packages/mypy_boto3/$line/$f.py ./../typings/mypy_boto3/$line/$f.pyi; done

    
    # install packaged stubs for explicit type annotation (also used by the generated stubs)
    mkdir -p ./../typings/mypy_boto3_$line
    for f2 in __init__ client paginator service_resource waiter type_defs; do \  
    cp buildstubs_env/lib/python*/site-packages/mypy_boto3_$line/$f2.py ./../typings/mypy_boto3_$line/$f2.pyi; 
    done
done
