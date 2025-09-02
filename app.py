from flask import Flask, jsonify, request, render_template
import requests

import random
colors = ['orange', 'FFFF00', 'green', 'blue', 
          'teal', 'FF5733', 'indigo', '3498DB', 'D35400', 
          'red', '27AE60', 'yellowgreen']

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


shields = []
combined_badges = ''
@app.route('/shields', methods=['POST'])
def generate():
    global shields, combined_badges, colors
    try:
        data = request.get_json()
        link = str(data.get('link'))
        color_state = str(data.get('color'))
        user = link.split('/')[-2]
        repo = link.split('/')[-1]

        response = requests.get(f'https://api.github.com/repos/{user}/{repo}/languages')
        languages = dict(response.json())

        shields = []
        combined_badges = ''

        for key in languages.keys():
            value = languages[key]
            percentage = round( value / sum(languages.values()) * 100 , 2)

            if color_state == 'random':
                color = random.choice(colors)
                colors.remove(color)
            else:
                color = color_state
            badge_url = f'https://img.shields.io/badge/{key}-{percentage}%25-{color}'
            readme_badge = f'![Badge]({badge_url})'
            combined_badges += f'{readme_badge}\n'

            shields.append({
                'badge_url': badge_url,
                'readme_badge': readme_badge,
            })
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo'] 
    except:
        return jsonify({'message':"Error! Check your URL"})
    return jsonify({'message':"Success!"})

@app.route('/generated')
def generated():

    return render_template('shields.html', shields=shields, combined_badges=combined_badges)

app.run(debug=True)