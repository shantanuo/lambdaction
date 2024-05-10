from chalice import Chalice

app = Chalice(app_name='helloworld')

@app.route('/')
def index():
    sample_text = (
        "The squirrel was in charge of acorn muffins, the rabbit brought a basket of the freshest carrots, and the owl",
        "brewed a pot of the most aromatic tea. As the sun dipped below the horizon, casting a golden glow over the",
        "garden, laughter and chatter filled the air, creating a melody that even the stars above paused to listen to."
    )
    print('Running the index function')
    return {'hello': 'galaxy', 'sample_text': sample_text}

