from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Function to handle API call to shorten URL
def shorten_url(long_url):
    # Using free API, no need to register TinyURL account
    api_url = f"https://tinyurl.com/api-create.php?url={long_url}"
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            return response.text  # Return shortened URL
        else:
            return "Error: Unable to connect to shortening server."
    except Exception as e:
        return f"Connection error: {str(e)}"

# Home page of web application
@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None
    original_url = None
    error_message = None

    # When user clicks 'Shorten' button (sends POST data)
    if request.method == "POST":
        original_url = request.form.get("url_input").strip()

        if original_url:
            # Call the shorten URL function above
            result = shorten_url(original_url)
            if "Error" in result:
                error_message = result
            else:
                short_url = result
        else:
            error_message = "Please do not leave the URL empty!"

    # Return interface with results (if any)
    return render_template("index.html", short_url=short_url, original_url=original_url, error=error_message)

if __name__ == "__main__":
    # Run web application in Debug mode for easy debugging
    app.run(debug=True)
