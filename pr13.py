from bs4 import BeautifulSoup

html_doc = """
<html>
    <head><title>PDS Practical</title></head>
    <body>
        <h1 class="heading">Data Science Overview</h1>
        <p class="description">Extracting web elements using BeautifulSoup in Python.</p>
        <ul id="skills">
            <li>Python</li>
            <li>Pandas</li>
            <li>NumPy</li>
        </ul>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, "html.parser")

print("Title Tag:", soup.title.string)
print("Heading Text:", soup.find("h1", class_="heading").text)

items = soup.find("ul", id="skills").find_all("li")
print("Skills List:")
for item in items:
    print("-", item.text)