import sqlite3
# import json

def generate_jsonl_file():
    c.execute('SELECT * FROM my_table')
    rows = c.fetchall()
    column_names = [column[0] for column in c.description]
    
    with open('data/data.jsonl', 'w') as f:
        for row in rows:
            inner_dict_str = str({column_names[i]: row[i] for i in range(len(column_names))})
            outer_json_str = '{"doc": "' + inner_dict_str.replace('"', '\\"') + '"}'
            f.write(outer_json_str + '\n')

# Initialize last_known_row_count
last_known_row_count = 0

conn = sqlite3.connect('nutri_nfhs5_india.db')
c = conn.cursor()

while True:  
    # Check current row count
    c.execute('SELECT COUNT(*) FROM my_table')
    current_row_count = c.fetchone()[0]
    
    # Compare with last known row count
    if current_row_count != last_known_row_count:
        generate_jsonl_file()
        last_known_row_count = current_row_count

