from website import create_app
from website.extensions import db
from website.auth.models import User

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'user': User}

if __name__ == "__main__":
    app.run()