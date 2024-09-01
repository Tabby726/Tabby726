<!DOCTYPE html>
<html>
<head>
    <title>Dawgs Dogs Landscaping</title>
    <link rel="stylesheet" href="static/style.css">
</head>
<body>
    <h1>Dawgs Dogs Landscaping</h1>
    <p>Your trusted landscaping partner.</p>
    <ul>
        <li><a href="/services">Services</a></li>
        <li><a href="/contact">Contact Us</a></li>
        <li><a href="/signup">Sign Up</a></li>
    </ul>
    </body>
</html>
if __name__ == '__main__':
    app.run(debug=Truefrom flask import Flask, render_template, request
    
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        """Renders the homepage with banner, services, and call to action."""
        services = [
            {"name": "Tree Trimming", "icon": "path/to/tree_icon.png"},
            {"name": "Lawn Mowing", "icon": "path/to/lawn_icon.png"},
            {"name": "Flower Bed Planting", "icon": "path/to/flower_icon.png"},
            {"name": "Front & Backyard Design", "icon": "path/to/design_icon.png"},
            {"name": "Paver Installation", "icon": "path/to/paver_icon.png"},
            {"name": "Irrigation System Installation", "icon": "path/to/irrigation_icon.png"}
        ]
        return render_template('home.html', services=services)
    
    @app.route('/services')
    def services():
        """Renders the services page with detailed descriptions of services."""
        return render_template('services.html')
    
    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        """Renders the contact page with a form to send messages."""
        if request.method == 'POST':
            name = request.form['name']
            phone = request.form['phone']
            email = request.form['email']
            message = request.form['message']
            # Implement email sending logic here (e.g., using a library like smtplib)
            return render_template('contact.html', success=True)
        return render_template('contact.html')
    
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        """Renders the signup page with a form to collect customer information."""
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            address = request.form['address']
            services = request.form.getlist('services')
            # Process signup information here (e.g., store in a database)
            return render_template('signup.html', success=True)
        return render_template('signup.html')
    
    if __name__ == '__main__':
        app.run(debug=True)
<!DOCTYPE html>
        <html>
        <head>
            <title>Dawgs Dogs Landscaping</title>
            <style>
                body {
                    background-color: #000000;
                }
        
                h1 {
                    color: #00FFFF;
                    font-family: Georgia;
                    font-weight: bold;
                    font-style: italic;
                }
        
                h2 {
                    color: #FF1493;
                    font-family: Merriweather;
                    font-weight: bold;
                    font-style: italic;
                }
        
                /* Add more CSS rules for other elements as needed */
            </style>
        </head>
        <body>
            <h1>Dawgs Dogs Landscaping</h1>
            <img src="path/to/bulldog_mowing.jpg" alt="Bulldog pushing a lawn mower">
            <h2>Our Services</h2>
            <ul>
                <li>Tree Trimming</li>
                <li>Lawn Mowing</li>
                <li>Flower Bed Planting</li>
                <li>Front & Backyard Design</li>
                <li>Paver Installation</li>
                <li>Irrigation System Installation</li>
            </ul>
        </body>
        </html>
        