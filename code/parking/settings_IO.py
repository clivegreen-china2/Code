import json
import settings


def export_settings() -> None:
    with open("settings.json", "w") as outfile:
        json.dump(settings.settings(), outfile)


def import_settings() -> dict:
    with open("settings.json") as infile:
        return json.load(infile)


export_settings()
imported_settings = import_settings()
print(imported_settings)
