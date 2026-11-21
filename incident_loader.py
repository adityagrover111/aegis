import json

def load_incidents(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            incidents = json.load(file)
            return incidents

    except FileNotFoundError:
        print("Unable to find an incident source")
        raise
    except json.JSONDecodeError:
        print("Invalid JSON format")
        raise


if __name__ == "__main__":
    incidents = load_incidents("data/incidents.json")
    print(incidents)