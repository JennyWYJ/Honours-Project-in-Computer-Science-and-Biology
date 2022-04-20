import csv as c

file = open("eIPSC_cell_coords_2022_04_02.csv")
csvreader = c.reader(file)

# Skip first 3 lines to get to get to data
next(csvreader)
next(csvreader)
next(csvreader)

# Get data by rows
rows = []
for r in csvreader:
    rows.append(r)

file.close()

# Gets the number of cells (rows) in the csv file
def num_cells(row_list):
    return len(row_list)

# Gives the name of a cell as a string in the format "cell_year_month_day_num"
def cell_name(row):
    date = row[0]
    if '-' in date:
        return "cell_" + date.replace('-', '_')
    return "cell_" + date

# Gives the x position value (int) of a cell. If no value in csv, return 'None'.
def cell_x(row):
    x = row[1]
    if x == '' or '.' in x:
        return 'None'
    return int(x)

# Gives the y position value (int) of a cell. If no value in csv, return 'None'.
def cell_y(row):
    y = row[2]
    if y == '' or '.' in y:
        return 'None'
    return int(y)

# Gives the z position value (int) of a cell. If no value in csv, return 'None'.
def cell_z(row):
    z = row[3]
    if z == '' or '.' in z:
        return 'None'
    return int(z)

# Gives the connectivity zones associated with a cell. If no zones, then returns 'None'. If multiple zones, then returns a list of zone strings. Else, returns single string of zone.
def cell_zone(row):
    zones = row[5]
    if 'None' in zones:
        return 'None'
    if ',' in zones:
        return zones.split(', ')
    return zones

# Gives a dictionary with the necessary info to create a cell.
def cell_info(name, x, y, z, zones):
    info = {}
    info['name'] = name
    info['x'] = x
    info['y'] = y
    info['z'] = z
    info['zones'] = zones

    return info

# Gives a list of info dictionaries for all cells in csv.
def all_cells():
    cells = []
    for r in rows:
        name = cell_name(r)
        x = cell_x(r)
        y = cell_y(r)
        z = cell_z(r)
        zones = cell_zone(r)

        info = cell_info(name, x, y, z, zones)
        cells.append(info)
    return cells