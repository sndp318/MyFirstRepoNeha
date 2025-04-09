# app.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"
    

@app.route("/keshav")
def hello_world_fancy():
    greetings = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Introduction of Keshav</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        p {
            font-size: 16px;
            line-height: 1.6;
            color: #555;
        }
        .highlight {
            font-weight: bold;
            color: #007bff;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #888;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Introduction of Keshav</h1>
        <p>Hello, I would like to introduce my brother <span class="highlight">Keshav</span>.</p>
        <p>Keshav is a dedicated and hard-working individual. After completing his Bachelor of Science (<span class="highlight">BSc</span>), he joined <span class="highlight">Wipro</span>, one of the leading companies in the IT industry.</p>
        <p>At Wipro, Keshav has been contributing to various projects, showcasing his skills, knowledge, and passion for technology. He is continuously growing and learning in his career, always striving for excellence.</p>
        <p>We are all very proud of his accomplishments and the positive impact he is making in his field.</p>
        
        <div class="footer">
            <p>Created with love for Keshav!</p>
        </div>
    </div>

</body>
</html>

    """
    return greetings



@app.route("/testpage")
def testpage():
    greetings = """
    <html>
    <body>

    <h1>This is a test page</h1>

    </body>
    </html>
    """
    return greetings