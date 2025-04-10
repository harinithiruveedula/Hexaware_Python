import os

class PropertyUtil:

    @staticmethod
    def get_property_string():
        props = {}
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resources', 'db.properties'))

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        key, value = line.split('=')
                        props[key.strip()] = value.strip()
        except Exception as e:
            print("error reading in files")
            print(e)

        conn_str = (
            f"DRIVER={{{props.get('driver')}}};"
            f"SERVER={props.get('server')};"
            f"DATABASE={props.get('database')};"
            f"Trusted_Connection={props.get('trusted_connection')};"
        )
        return conn_str
