import json

def write_json(acronym, primary_color, secondary_color, alliases):
    data = {
        acronym : {
            "primary-color": primary_color,
            "secondary-color": secondary_color,
            "alliases": alliases
        }
    }

    with open("data.json", "w") as write_file:
        json.dump(data, write_file);

if __name__ == '__main__':
    acronym = input("college acronym: ")
    primary_color = input("primary-color (HEX): ")
    secondary_color = input("secondary-color (HEX): ")
    alliases = input("enter alliases, seperated by commas (hit enter when done): ")
    write_json(acronym, primary_color, secondary_color, list(alliases.split(',')))
