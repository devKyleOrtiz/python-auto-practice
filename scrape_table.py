import pandas as pd #panda import with alias of pd for ease of use / less typing

#using the read html method to "scrape" this page for tables and putting the list of tables it finds into var called bool_tables
bool_tables = pd.read_html('https://en.wikipedia.org/wiki/Boolean_algebra')

print(bool_tables)