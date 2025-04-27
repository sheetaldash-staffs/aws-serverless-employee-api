from flask import Flask, jsonify
import boto3

app = Flask(__name__)

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='eu-north-1')
table = dynamodb.Table('Employees')

# Get all employees
@app.route('/employees', methods=['GET'])
def get_all_employees():
    response = table.scan()  # Scan all items in the table
    employees = response['Items']
    return jsonify(employees)

# Get employee by ID
@app.route('/employee/<employee_id>', methods=['GET'])
def get_employee(employee_id):
    response = table.get_item(Key={'employeeId': employee_id})
    if 'Item' in response:
        return jsonify(response['Item'])
    else:
        return jsonify({'message': 'Employee not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
