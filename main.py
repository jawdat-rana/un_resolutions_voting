from model import Resolution
from past_50_resolutions import extract_last_50_resolutions


def get_url_ids(df):
    return df['Links']


if __name__ == "__main__":

    URL = "https://digitallibrary.un.org/search?cc=Voting+Data&ln=en&c=Voting+Data"

    # download last 50 resolutions from UN Digital Library
    df = extract_last_50_resolutions(URL)

    if not df.empty:
        url_ids = get_url_ids(df)

    # iteraters over all resolutions' page and extract voting information
    for id in url_ids:
        resolution = Resolution(id=id)

        print(resolution.__str__())
        print('\n\n')