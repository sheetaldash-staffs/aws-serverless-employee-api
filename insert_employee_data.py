import boto3
from faker import Faker

# Initialize AWS DynamoDB resource and Faker
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Ensure region is correct
table = dynamodb.Table('Employees')  # Name of the table created in DynamoDB
fake = Faker()

# Generate and insert 100 employees
for _ in range(100):
    employee_id = fake.uuid4()  # Unique employee ID
    name = fake.name()
    job_title = fake.job()
    department = fake.word()

    # Insert into DynamoDB table
    table.put_item(
        Item={
            'employeeId': employee_id,
            'name': name,
            'job_title': job_title,
            'department': department,
        }
    )
    print(f"Inserted employee {name} with ID {employee_id}")
