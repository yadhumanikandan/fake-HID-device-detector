import requests

# Define the data you want to insert
data = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'age': 30
}

# Make a POST request to the Flask application to insert the data
response = requests.post('http://127.0.0.1:5000/insert', json=data)

# Check the response status
if response.status_code == 200:
    print("Data inserted successfully!")
else:
    print("Error:", response.text)
