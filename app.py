from chalice import Chalice
import requests
import time
app = Chalice(app_name='helloworld')

@app.route('/')
def index():
    url = 'https://v2.jokeapi.dev/joke/Any'
    response = requests.get(url)
    data = response.json()
    if data['type'] == 'single':
        joke = data['joke']
    else:
        joke = f"{data['setup']}\n{data['delivery']}"
    time_asleep = 2
    time.sleep(time_asleep)
    return {
        'joke': joke,
        'time_taken': time_asleep
    }
