from flask import Flask, render_template, request
from model import Resolution

app = Flask(__name__)

def get_url_ids(df):
    return df['Links']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the 7-digit number from the form
        number_input = request.form['number_input']

        # Check if the input is a 7-digit number
        if number_input.isdigit() and len(number_input) == 7:

            resolution = Resolution(id=number_input)
            document_info = {
                'record_id': id,
                'title': resolution.title,
                'date': resolution.date,
                'resolution_id': resolution.resolution_id,
                'agenda_title': resolution.agenda_title,
                'agenda_subject': resolution.agenda_subject,
                'voting_summary': resolution.voting_summary,
            }
            all_countries = []
            for country in resolution.get_countries_with_yes_vote():
                all_countries.append({'name': country, 'vote': 'Yes'})
            for country in resolution.get_countries_with_no_vote():
                all_countries.append({'name': country, 'vote': 'No'})
            for country in resolution.get_countries_with_abstentions_vote():
                all_countries.append({'name': country, 'vote': 'Abstention'})
            for country in resolution.get_non_voting_countries():
                all_countries.append({'name': country, 'vote': 'NonVoting'})

            return render_template('votes.html', all_countries=all_countries,
                                   document_info=document_info, adopted_without_voting=len(all_countries))

        else:
            error_message = "Please enter a valid 7-digit number."
            return render_template('index.html', error_message=error_message)

    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
