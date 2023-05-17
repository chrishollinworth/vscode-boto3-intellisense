import boto3

def get_all_available_services():

    session = boto3.session.Session()
    aws_services = session.get_available_services()

    aws_services_line_breaks = ["{}\n".format(i).replace("-", "_") for i in aws_services]
    with open(r'services2.txt', 'w') as fp:
        fp.writelines(aws_services_line_breaks)

if __name__ == "__main__":
    get_all_available_services()