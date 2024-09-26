import csv
import os

# HTML template for index.html
index_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Compost or Not - Your Guide to Composting</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <h1>Compost or Not</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#items">Compost Items</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="home">
            <h2>Welcome to Compost or Not</h2>
            <p>Your ultimate guide to what can and cannot be composted.</p>
        </section>

        <section id="about">
            <h2>About Compost or Not</h2>
            <p>Our mission is to provide clear, concise information to help you make informed decisions about composting. Whether you're a beginner or an experienced composter, we're here to help you create rich, healthy compost for your garden.</p>
        </section>

        <section id="items">
            <h2>Can I Compost This?</h2>
            <ul>
                {item_links}
            </ul>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Compost or Not. All rights reserved.</p>
    </footer>

    <script src="js/script.js"></script>
</body>
</html>
"""

# Read the CSV file and generate item links
item_links = []
with open('combined_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        item = row['item'].capitalize()
        filename = item.lower().replace(' ', '-')
        link = f'<li><a href="items/{filename}.html">{item}</a></li>'
        item_links.append(link)

# Sort the links alphabetically
item_links.sort()

# Fill in the HTML template
index_content = index_template.format(item_links='\n                '.join(item_links))

# Generate the index.html file
with open('index.html', 'w') as indexfile:
    indexfile.write(index_content)

print("index.html generated successfully!")