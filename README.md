## Flask Application Design

### HTML Files

- **index.html**: This will be the main HTML file for the website. It will contain the necessary Bootstrap elements to display the request headers, method, and body.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Request Viewer</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQh58iYOTvBX41IVsSLXmkN7F0C6h4x+Omy4cwh7y3XWDszP7h4s1CfeT" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    <h1>Request Viewer</h1>
    <div id="request-headers"></div>
    <div id="request-method"></div>
    <div id="request-body"></div>
  </div>

  <script>
    // Function to display request headers
    function displayHeaders(headers) {
      const headersElement = document.getElementById('request-headers');

      let headersHtml = '<ul>';
      for (const header in headers) {
        headersHtml += `<li>${header}: ${headers[header]}</li>`;
      }
      headersHtml += '</ul>';

      headersElement.innerHTML = headersHtml;
    }

    // Function to display request method
    function displayMethod(method) {
      const methodElement = document.getElementById('request-method');

      methodElement.innerHTML = `Method: ${method}`;
    }

    // Function to display request body
    function displayBody(body) {
      const bodyElement = document.getElementById('request-body');

      bodyElement.innerHTML = `Body: ${body}`;
    }

    // Fetch request data from Flask endpoint
    fetch('/request-data')
      .then(response => response.json())
      .then(data => {
        displayHeaders(data.headers);
        displayMethod(data.method);
        displayBody(data.body);
      })
      .catch(error => {
        console.error('Error fetching request data:', error);
      });
  </script>
</body>
</html>
```

### Routes

- **`/request-data`**: This route will handle the request headers, method, and body and return them as a JSON response.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/request-data', methods=['GET', 'POST'])
def request_data():
  headers = request.headers
  method = request.method
  body = request.get_data()

  return jsonify({
    'headers': headers,
    'method': method,
    'body': body.decode('utf-8')
  })

if __name__ == '__main__':
  app.run(debug=True)
```