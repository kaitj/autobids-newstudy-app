from autobidsportal import app, db
from autobidsportal.dcm4cheutils import Dcm4cheUtils, gen_utils, Dcm4cheError
from autobidsportal.models import User, Answer, Submitter, Principal
from datetime import datetime
import time


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Answer': Answer, 'Submitter': Submitter, 'Principal': Principal}

@app.cli.command()
def scheduled():
    """Run scheduled job."""
    db.session.query(Principal).delete()
    try:
        principal_names = gen_utils().get_all_pi_names()
        for p in principal_names:
            principal = Principal(principal_name=p)
            db.session.add(principal)
            db.session.commit()
    except Dcm4cheError as err:
        principal = Principal(principal_name='')
        db.session.add(principal)
        db.session.commit()
    return "Success"