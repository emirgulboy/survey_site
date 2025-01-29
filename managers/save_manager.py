
import json
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import supabase


class save_manager:
    def __init__(self):
        return

    def save_to_db(self, return_data, session_data):
        self.parse_return(return_data, session_data)
        with open('.streamlit/credentials.json', 'r') as f:
            credentials = json.load(f)
        url = credentials['url']
        key = credentials['authtoken']
        supabase_client = supabase.create_client(url, key)

        response = supabase_client.table('session_data').insert({"session_details": self._parsed}).execute()

    def save_to_file(self, return_data):
        with open('results.jsonl', 'a') as f:
            f.write(json.dumps(return_data) + '\n')

    def parse_return(self, return_data, session_data):
        self._parsed = {}
        self._parsed['session_data'] = session_data
        self._parsed['results'] = return_data
