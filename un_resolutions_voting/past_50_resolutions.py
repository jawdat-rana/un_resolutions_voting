import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract_last_50_resolutions(url: str) -> pd.DataFrame:
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    titles = soup.find_all('div', attrs={'class': 'result-title'})
    titles = [title.text.strip() for title in titles]

    abstracts = soup.find_all('div', attrs={'class': 'result-abstract'})
    abstracts = [abstract.find_all('div', attrs={'class': ''}) for abstract in abstracts]
    abstracts = [abstract[1].text.strip() if len(abstract)>1 else '' for abstract in abstracts]

    briefs = soup.find_all('div', attrs={'class': 'brief-options'})
    briefs = [brief.text.strip() for brief in briefs]

    links = soup.find_all('a', href=True)
    links = [
        link['href'] for link in links
        if '/record/' in link['href']
    ]

    df = pd.DataFrame()
    df['Titles'] = titles
    df['Abstracts'] = abstracts
    df['Links'] = links
    df['Briefs'] = briefs

    df['Links'] = df['Links'].str.extract(r'(\d+)')

    df['Abstracts'] = df['Abstracts'].str.replace('\n', '')
    df[['Yes', 'No', 'Abstentions',
        'Non-voting', 'Total']] = df['Abstracts'].str.split('|', expand=True)

    df['Briefs'] = df['Briefs'].str.replace('\n', '')
    df[['Resolution Article', 'Date', 'Tag', 'n']] = df['Briefs'].str.split('|', expand=True)

    df = df[['Titles', 'Links', 'Yes', 'No', 'Abstentions',
        'Non-voting', 'Total', 'Resolution Article', 'Date', 'Tag']]

    return df

def get_url_ids(df: pd.DataFrame):
    return df['Links']


if __name__ == "__main__":

    URL = "https://digitallibrary.un.org/search?cc=Voting+Data&ln=en&c=Voting+Data"
    df = extract_last_50_resolutions(URL)

    df.to_csv('UN-resolutions.csv', index=False)
