import json
import xmltodict, requests

class Resolution:
    def __init__(self, json_data: dict = None, id: str = None):
        # https://research.un.org/en/digitallibrary/export
        # documentation for tags and codes available on the above url

        if id:
            url = f'https://digitallibrary.un.org/record/{id}/export/xm'
            try:
                r = requests.get(url)
                json_data = xmltodict.parse(r.text)
            except requests.exceptions.RequestException as e:
                raise SystemExit(f'Unable to fetch data from url. Error Message({e})')

        try:
            self.data = json.loads(json.dumps(json_data))
        except Exception as e:
            raise SystemExit(f'Unable to load json. Error Message ({e})')

        self.date = self.get_date()
        self.title = self.get_title()
        self.resolution_id = self.get_resolution_id()
        self.agenda_title = self.get_agenda_title()
        self.agenda_subject = self.get_agenda_subject()

        self.voting_summary = {
            "Yes": self.get_voting_count('yes'),
            "No": self.get_voting_count('no'),
            "Abstentions": self.get_voting_count('abstentions'),
            "Non-voting": self.get_voting_count('non-voting'),
            "Total voting membership": self.get_voting_count('total')
        }

        self.votes = self.extract_votes()

    tags_dict = {'date': ['269', 'a'],
                 'title': ['245', 'a'],
                 'agenda_title': ['991', 'c'],
                 'agenda_subject': ['991', 'd'],
                 'resolution_id': ['791', 'a'],
                 'vote_summary': ['996'],
                 'vote_information': ['967']
                 }

    def __str__(self):
        return f"Title: {self.title} \n" \
               f"Date: {self.date} \n" \
               f"Resolution ID: {self.resolution_id}\n" \
               f"Agenda Title: {self.agenda_title}\n" \
               f"Agenda Subject: {self.agenda_subject} \n" \
               f"Voting Summary: {self.voting_summary}"

    def get_json_data(self):
        return self.data

    def get_date(self):
        tag, code = self.tags_dict['date']
        return self.extract_text_for_tag(tag, code)

    def get_title(self):
        tag, code = self.tags_dict['title']
        return self.extract_text_for_tag(tag, code)

    def get_agenda_title(self):
        # No agenda title in Security Council records
        tag, code = self.tags_dict['agenda_title']
        return self.extract_text_for_tag(tag, code)

    def get_agenda_subject(self):
        tag, code = self.tags_dict['agenda_subject']
        return self.extract_text_for_tag(tag, code)

    def get_resolution_id(self):
        tag, code = self.tags_dict['resolution_id']
        return self.extract_text_for_tag(tag, code)

    def get_voting_count(self, attr: str):

        tag = self.tags_dict['vote_summary'][0]

        if attr == 'yes':
            code = 'b'
        elif attr == 'no':
            code = 'c'
        elif attr == 'abstentions':
            code = 'd'
        elif attr == 'non-voting':
            code = 'e'
        elif attr == 'total':
            code = 'f'

        return self.extract_text_for_tag(tag, code)

    def extract_text_for_tag(self, tag, code):
        data = self.data

        datafields = data["collection"]["record"]["datafield"]
        for datafield in datafields:
            if datafield["@tag"] == tag:
                subfields = datafield.get("subfield")
                if isinstance(subfields, list):
                    for subfield in subfields:
                        if subfield["@code"] == code:
                            text = subfield["#text"]
                            return text
                elif isinstance(subfields, dict) and subfields["@code"] == code:
                    text = subfields["#text"]
                    return text
        return None

    def extract_votes(self):
        data = self.data
        tag = self.tags_dict['vote_information'][0]
        votes = []

        datafields = data["collection"]["record"]["datafield"]
        for datafield in datafields:
            if datafield["@tag"] == tag:
                subfields = datafield.get("subfield")
                if isinstance(subfields, list):
                    result = {}
                    for subfield in subfields:
                        code = subfield["@code"]
                        if code in ['c', 'd', 'e']:
                            result[code] = subfield["#text"]
                    votes.append(result)
                elif isinstance(subfields, dict) and subfields["@code"] in ['c', 'd', 'e']:
                    print("dict")
                    return {subfields["@code"]: subfields["#text"]}
        return votes

    def get_countries_with_yes_vote(self):
        return [item['e'] for item in self.votes if item.get('d') == 'Y']

    def get_countries_with_abstentions_vote(self):
        return [item['e'] for item in self.votes if item.get('d') == 'A']

    def get_non_voting_countries(self):
        return [item['e'] for item in self.votes if item.get('d') is None]

    def get_countries_with_no_vote(self):
        return [item['e'] for item in self.votes if item.get('d') == 'N']
