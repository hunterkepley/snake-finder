import csv

def main():
    all_map_bans = {"Villa": 0, "Oregon": 0, "Kafe": 0, "Coastline": 0, "Clubhouse": 0, "Themepark": 0, '': 0, "Consulate": 0 } # All the maps banned

    all_map_picks = {"Villa": 0, "Oregon": 0, "Kafe": 0, "Coastline": 0, "Clubhouse": 0, "Themepark": 0, '': 0, "Consulate": 0 } # All the maps picked
    with open('.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'\nWelcome to Snake Finder v0.1.3\n\nAll column names are {", ".join(row)}\n')
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
    for i in range(len(all_map_picks)):
        if list(all_map_picks.keys())[i] != '':
            print(f'{list(all_map_picks)[i]} picked {list(all_map_picks)[i]} times') 



if __name__ == "__main__":
    main()
