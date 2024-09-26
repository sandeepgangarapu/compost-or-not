import csv
import os

# HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Can I Compost {item}? | Compost or Not</title>
    <meta name="description" content="Learn whether you can compost {item} and how to do it properly.">
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <header>
        <h1>Compost or Not</h1>
        <nav>
            <ul>
                <li><a href="../index.html">Home</a></li>
                <li><a href="../index.html#about">About</a></li>
                <li><a href="../index.html#items">Compost Items</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <article>
            <h1>Can I Compost {item}?</h1>
            <div class="compost-status">
                <span class="status {status_class}">{can_compost}</span>
                <p>{status_description}</p>
            </div>
            <section>
                <h2>What to Know</h2>
                <ul>
                    {what_to_know}
                </ul>
            </section>
            <section>
                <h2>Tips</h2>
                <ul>
                    {tips}
                </ul>
            </section>
        </article>
    </main>

    <footer>
        <p>&copy; 2024 Compost or Not. All rights reserved.</p>
    </footer>

    <script src="../js/script.js"></script>
</body>
</html>
"""

# Ensure the 'items' directory exists
if not os.path.exists('items'):
    os.makedirs('items')

import os

print("Current working directory:", os.getcwd())
# Read the CSV file and generate HTML pages
with open('compost-or-not/combined_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        item = row['item'].capitalize()
        can_compost = row['can_compost']
        what_to_know = row['what_to_know']
        tips = row['tips']

        # Prepare the data for the HTML template
        status_class = 'yes' if can_compost.lower() == 'yes' else 'no'
        status_description = f"{item} {'can' if status_class == 'yes' else 'cannot'} be composted."

        # Split what_to_know and tips into list items
        what_to_know_list = [f"<li>{point.strip()}</li>" for point in what_to_know.split('.') if point.strip()]
        tips_list = [f"<li>{point.strip()}</li>" for point in tips.split('.') if point.strip()]

        # Fill in the HTML template
        html_content = html_template.format(
            item=item,
            can_compost=can_compost,
            status_class=status_class,
            status_description=status_description,
            what_to_know='\n                    '.join(what_to_know_list),
            tips='\n                    '.join(tips_list)
        )

        # Generate the HTML file
        filename = f"compost-or-not/items/{item.lower().replace(' ', '-')}.html"
        print(filename)
        with open(filename, 'w') as htmlfile:
            htmlfile.write(html_content)

print("HTML pages generated successfully!")