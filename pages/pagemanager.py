# Number of pages you want to generate
num_pages = 204

# Loop to generate pages
for page in range(3, num_pages + 3):
    # Define the previous and next page numbers
    prev_page = page - 1
    next_page = page + 1

    # HTML template for each page
    html_template = f'''
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Read Comic</title>
    <link rel="stylesheet" href="../style.css">
</head>

<body>
    <header>
        <h1 class="header_img">
            The Night Class
        </h1>
        <br>

    </header>


        <nav>
            <ul>
                <li><a href="../index.html">Home</a></li>
                <li><a href="../about.html">About</a></li>
                <li><a href="../contact.html">Contact</a></li>
                <li><a href="../setting.html">Setting</a></li>
                <li><a href="../readcomic.html">Read Comic</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="comic-page">
            <h2>Chapter 1: The Transformation</h2>
        </section>

        <div class="comic-page">
            <button class="next-page-btn"><a href="1_PREV.html"><</a></button>
            <img src="../pg/1_PAGE.png" alt="Page 1" class="page-image">
            <button class="next-page-btn"><a href="1_NEXT.html">></a></button>
        </div>


    </main>

    <footer>
            <p>
            2023 Night Corp Inc. - 
            Contact information: jessietorresacosta@gmail.com
            </p>
    </footer>

</body>

</html>
    '''

    html_template = html_template.replace("PAGE", f'{page:03d}')
    html_template = html_template.replace("PREV", f'{prev_page:03d}')
    html_template = html_template.replace("NEXT", f'{next_page:03d}')

# Save the HTML to a file
    with open(f'1_{page:03d}.html', 'w') as file:
        file.write(html_template)

print(f'{num_pages} HTML pages generated.')
