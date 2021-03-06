import csv

def main():
    all_map_bans = {"Villa": 0, "Oregon": 0, "Kafe": 0, "Coastline": 0, "Clubhouse": 0, "Themepark": 0, '': 0, "Consulate": 0 } # All the maps banned

    all_map_picks = {"Villa": 0, "Oregon": 0, "Kafe": 0, "Coastline": 0, "Clubhouse": 0, "Themepark": 0, '': 0, "Consulate": 0 } # All the maps picked



    with open('.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'\nWelcome to Snake Finder v0.1.7\n\nAll column names are {", ".join(row)}\n')
                line_count += 1
            else:
                all_map_bans[(row[8])] += 1
                all_map_bans[(row[9])] += 1
                all_map_bans[(row[10])] += 1
                all_map_bans[(row[11])] += 1
                all_map_picks[(row[12])] += 1
                
                line_count += 1
        print(f'Done reading {line_count} lines')

    print("\n--------------------------------\n\n\tMAP PICKS:\n")
    for key, value in all_map_picks.items():
        if key != '':
            print(f'{key} picked {value} times')

    print("\n\tMAP BANS:\n\t/(Both?)\\\n")

    for key, value in all_map_bans.items():
        if key != '':
            print(f'{key} banned {value} times')



if __name__ == "__main__":
    main()
