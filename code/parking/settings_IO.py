import json, settings, fileIO


def export_settings() -> None:
    json_data = json.dumps(settings.settings(), ensure_ascii=False)
    fileIO.write('settings.json', json_data)


def import_settings() -> dict:
    json_data = fileIO.read('settings.json')
    return json.loads(json_data)


if __name__ == "__main__":
    export_settings()
    print(import_settings())
