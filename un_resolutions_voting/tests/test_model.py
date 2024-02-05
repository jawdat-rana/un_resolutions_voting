import unittest
from un_resolutions_voting.model import Resolution


class TestResolution(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        sample_data = {
            "collection": {
                "@xmlns": "http://www.loc.gov/MARC21/slim",
                "record": {
                    "controlfield": [
                        {"@tag": "000", "#text": "01241nam a2200397#a 4500"},
                        {"@tag": "001", "#text": "4033397"},
                        {"@tag": "005", "#text": "20240119110628.0"}
                    ],
                    "datafield": [
                        {"@tag": "035", "@ind1": " ", "@ind2": " ", "subfield": {"@code": "a", "#text": "(DHL)1393952"}},
                        {"@tag": "039", "@ind1": " ", "@ind2": " ", "subfield": {"@code": "a", "#text": "VOT"}},
                        {"@tag": "040", "@ind1": " ", "@ind2": " ", "subfield": {"@code": "a", "#text": "NNUN"}},
                        {"@tag": "089", "@ind1": " ", "@ind2": " ", "subfield": {"@code": "b", "#text": "B23"}},
                        {"@tag": "245", "@ind1": " ", "@ind2": " ", "subfield": {"@code": "a", "#text": "Security Council resolution 2722 (2024) [on attacks by Houthis on merchant and commercial vessels]"}},
                        {"@tag": "269", "@ind1": " ", "@ind2": " ", "subfield": {"@code": "a", "#text": "2024-01-10"}},
                        {"@tag": "590", "@ind1": " ", "@ind2": " ", "subfield": {"@code": "a", "#text": "Vote"}},
                        {"@tag": "791", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "S/RES/2722(2024)"},
                            {"@code": "b", "#text": "S/"},
                            {"@code": "c", "#text": "79"},
                            {"@code": "0", "#text": "(DHLAUTH)938242"}
                        ]},
                        {"@tag": "930", "@ind1": " ", "@ind2": " ", "subfield": {"@code": "a", "#text": "VOT"}},
                        {"@tag": "952", "@ind1": " ", "@ind2": " ", "subfield": {"@code": "a", "#text": "S/PV.9527"}},
                        {"@tag": "967", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "001"},
                            {"@code": "b", "#text": "R"},
                            {"@code": "c", "#text": "DZA"},
                            {"@code": "d", "#text": "A"},
                            {"@code": "e", "#text": "ALGERIA"}
                        ]},
                        {"@tag": "967", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "002"},
                            {"@code": "b", "#text": "P"},
                            {"@code": "c", "#text": "CHN"},
                            {"@code": "d", "#text": "A"},
                            {"@code": "e", "#text": "CHINA"}
                        ]},
                        {"@tag": "967", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "003"},
                            {"@code": "b", "#text": "R"},
                            {"@code": "c", "#text": "ECU"},
                            {"@code": "d", "#text": "Y"},
                            {"@code": "e", "#text": "ECUADOR"}
                        ]},
                        {"@tag": "967", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "004"},
                            {"@code": "b", "#text": "P"},
                            {"@code": "c", "#text": "FRA"},
                            {"@code": "d", "#text": "Y"},
                            {"@code": "e", "#text": "FRANCE"}
                        ]},
                        {"@tag": "967", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "005"},
                            {"@code": "b", "#text": "R"},
                            {"@code": "c", "#text": "GUY"},
                            {"@code": "d", "#text": "Y"},
                            {"@code": "e", "#text": "GUYANA"}
                        ]},
                        {"@tag": "967", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "006"},
                            {"@code": "b", "#text": "R"},
                            {"@code": "c", "#text": "JPN"},
                            {"@code": "d", "#text": "Y"},
                            {"@code": "e", "#text": "JAPAN"}
                        ]},
                        {"@tag": "967", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "007"},
                            {"@code": "b", "#text": "R"},
                            {"@code": "c", "#text": "MLT"},
                            {"@code": "d", "#text": "Y"},
                            {"@code": "e", "#text": "MALTA"}
                        ]},
                        {"@tag": "967", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "008"},
                            {"@code": "b", "#text": "R"},
                            {"@code": "c", "#text": "MOZ"},
                            {"@code": "d", "#text": "A"},
                            {"@code": "e", "#text": "MOZAMBIQUE"}
                        ]},
                        {"@tag": "967", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "009"},
                            {"@code": "b", "#text": "R"},
                            {"@code": "c", "#text": "KOR"},
                            {"@code": "d", "#text": "Y"},
                            {"@code": "e", "#text": "REPUBLIC OF KOREA"}
                        ]},
                        {"@tag": "967", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "010"},
                            {"@code": "b", "#text": "P"},
                            {"@code": "c", "#text": "RUS"},
                            {"@code": "d", "#text": "A"},
                            {"@code": "e", "#text": "RUSSIAN FEDERATION"}
                        ]},
                        {"@tag": "967", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "011"},
                            {"@code": "b", "#text": "R"},
                            {"@code": "c", "#text": "SLE"},
                            {"@code": "d", "#text": "Y"},
                            {"@code": "e", "#text": "SIERRA LEONE"}
                        ]},
                        {"@tag": "967", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "012"},
                            {"@code": "b", "#text": "R"},
                            {"@code": "c", "#text": "SVN"},
                            {"@code": "d", "#text": "Y"},
                            {"@code": "e", "#text": "SLOVENIA"}
                        ]},
                        {"@tag": "967", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "013"},
                            {"@code": "b", "#text": "P"},
                            {"@code": "c", "#text": "CHE"},
                            {"@code": "d", "#text": "Y"},
                            {"@code": "e", "#text": "SWITZERLAND"}
                        ]},
                        {"@tag": "967", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "014"},
                            {"@code": "b", "#text": "P"},
                            {"@code": "c", "#text": "GBR"},
                            {"@code": "d", "#text": "Y"},
                            {"@code": "e", "#text": "UNITED KINGDOM"}
                        ]},
                        {"@tag": "967", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "015"},
                            {"@code": "b", "#text": "P"},
                            {"@code": "c", "#text": "USA"},
                            {"@code": "d", "#text": "Y"},
                            {"@code": "e", "#text": "UNITED STATES"}
                        ]},
                        {"@tag": "980", "@ind1": " ", "@ind2": " ", "subfield": {"@code": "a", "#text": "BIB"}},
                        {"@tag": "981", "@ind1": " ", "@ind2": " ", "subfield": {"@code": "a", "#text": "Security Council"}},
                        {"@tag": "989", "@ind1": " ", "@ind2": " ", "subfield": {"@code": "a", "#text": "Voting Data"}},
                        {"@tag": "991", "@ind1": "3", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "S/70"},
                            {"@code": "b", "#text": "[58]"},
                            {"@code": "d", "#text": "YEMEN--POLITICAL CONDITIONS"},
                            {"@code": "0", "#text": "(DHLAUTH)861063"}
                        ]},
                        {"@tag": "991", "@ind1": "3", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "S/"},
                            {"@code": "b", "#text": "X"},
                            {"@code": "c", "#text": "Maintenance of international peace and security."},
                            {"@code": "0", "#text": "(DHLAUTH)921222"}
                        ]},
                        {"@tag": "992", "@ind1": " ", "@ind2": " ", "subfield": {"@code": "a", "#text": "2024-01-10"}},
                        {"@tag": "993", "@ind1": "2", "@ind2": " ", "subfield": {"@code": "a", "#text": "S/2024/37"}},
                        {"@tag": "996", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "b", "#text": "011"},
                            {"@code": "c", "#text": "000"},
                            {"@code": "d", "#text": "004"},
                            {"@code": "e", "#text": "000"},
                            {"@code": "f", "#text": "015"}
                        ]},
                        {"@tag": "999", "@ind1": " ", "@ind2": " ", "subfield": [
                            {"@code": "a", "#text": "vvv20240115"},
                            {"@code": "b", "#text": "20240115"},
                            {"@code": "c", "#text": "v"}
                        ]}
                    ]
                }
            }
        }
        # id='4033397'

        self.resolution_instance = Resolution(json_data=sample_data)

    def test_get_date(self):
        self.assertEqual(self.resolution_instance.get_date(), "2024-01-10")

    def test_get_title(self):
        expected_title = "Security Council resolution 2722 (2024) [on attacks by Houthis on merchant and commercial vessels]"
        self.assertEqual(self.resolution_instance.get_title(), expected_title)

    def test_get_agenda_title(self):
        self.assertEqual(self.resolution_instance.get_agenda_title(), "Maintenance of international peace and security.")

    def test_get_agenda_subject(self):
        self.assertEqual(self.resolution_instance.get_agenda_subject(), "YEMEN--POLITICAL CONDITIONS")

    def test_get_resolution(self):
        self.assertEqual(self.resolution_instance.get_resolution_id(), "S/RES/2722(2024)")

    def test_get_voting_count(self):
        self.assertEqual(self.resolution_instance.get_voting_count('yes'), "011")
        self.assertEqual(self.resolution_instance.get_voting_count('no'), "000")
        self.assertEqual(self.resolution_instance.get_voting_count('abstentions'), "004")
        self.assertEqual(self.resolution_instance.get_voting_count('non-voting'), "000")
        self.assertEqual(self.resolution_instance.get_voting_count('total'), "015")

    def test_extract_votes(self):
        expected_votes = [{'c': 'DZA', 'd': 'A', 'e': 'ALGERIA'}, {'c': 'CHN', 'd': 'A', 'e': 'CHINA'},
                          {'c': 'ECU', 'd': 'Y', 'e': 'ECUADOR'}, {'c': 'FRA', 'd': 'Y', 'e': 'FRANCE'},
                          {'c': 'GUY', 'd': 'Y', 'e': 'GUYANA'}, {'c': 'JPN', 'd': 'Y', 'e': 'JAPAN'},
                          {'c': 'MLT', 'd': 'Y', 'e': 'MALTA'}, {'c': 'MOZ', 'd': 'A', 'e': 'MOZAMBIQUE'},
                          {'c': 'KOR', 'd': 'Y', 'e': 'REPUBLIC OF KOREA'},
                          {'c': 'RUS', 'd': 'A', 'e': 'RUSSIAN FEDERATION'},
                          {'c': 'SLE', 'd': 'Y', 'e': 'SIERRA LEONE'}, {'c': 'SVN', 'd': 'Y', 'e': 'SLOVENIA'},
                          {'c': 'CHE', 'd': 'Y', 'e': 'SWITZERLAND'}, {'c': 'GBR', 'd': 'Y', 'e': 'UNITED KINGDOM'},
                          {'c': 'USA', 'd': 'Y', 'e': 'UNITED STATES'}]
        self.assertEqual(self.resolution_instance.extract_votes(), expected_votes)

    def test_get_countries_with_yes_vote(self):
        self.assertEqual(self.resolution_instance.get_countries_with_yes_vote(),
                         ['ECUADOR', 'FRANCE', 'GUYANA', 'JAPAN', 'MALTA', 'REPUBLIC OF KOREA', 'SIERRA LEONE',
                          'SLOVENIA', 'SWITZERLAND', 'UNITED KINGDOM', 'UNITED STATES'])

    def test_get_countries_with_abstentions_vote(self):
        self.assertEqual(self.resolution_instance.get_countries_with_abstentions_vote(),
                         ['ALGERIA', 'CHINA', 'MOZAMBIQUE', 'RUSSIAN FEDERATION'])

    def test_get_non_voting_countries(self):
        self.assertEqual(self.resolution_instance.get_non_voting_countries(), [])

    def test_get_countries_with_no_vote(self):
        self.assertEqual(self.resolution_instance.get_countries_with_no_vote(), [])

if __name__ == '__main__':
    unittest.main()
