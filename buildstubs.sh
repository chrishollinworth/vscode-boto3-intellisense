docker build -t boto3-build-stubs .
docker run -td boto3-build-stubs
id=$(docker container ls  | grep 'boto3-build-stubs' | awk '{print $1}');
docker cp $id:/typings .
docker cp $id:/services2.txt services2.txt