'''Welcome to Aoi Araki's analyzing/printing and counting software'''

def main():
    filename = input("Please enter the name of the file you want to enter: ")
    show_counts = {}
    with open(filename, 'r') as file:
        for line in file:
            show = line.strip()
            if show in show_counts:
                show_counts[show] += 1
            else:
                show_counts[show] = 1

    def get_count(item):
        return item[1]

    sorted_shows = sorted(show_counts.items(), key=get_count, reverse=True) #Review the concept of key and reverse
    with open('filtered_file.txt', 'w') as file:
        for show, count in sorted_shows:
            file.write(f"{show}: {count}\n")

    print("It has been printed to 'filtered_file.txt'! ")

main()