import functools, tarfile, tempfile, os
from flask_login import current_user
from flask import current_app, abort, request

generate = lambda x: os.urandom(x).hex()

def is_admin(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        if current_user.username == current_app.config['ADMIN_USERNAME'] and request.remote_addr == '127.0.0.1':
            return f(*args, **kwargs)
        else:
            return abort(401)

    return wrap

def extract_firmware(file):
    tmp  = tempfile.gettempdir()
    path = os.path.join(tmp, file.filename)
    file.save(path)

    if tarfile.is_tarfile(path):
        tar = tarfile.open(path, 'r:gz')
        tar.extractall(tmp)

        rand_dir = generate(15)
        extractdir = f"{current_app.config['UPLOAD_FOLDER']}/{rand_dir}"
        os.makedirs(extractdir, exist_ok=True)
        for tarinfo in tar:
            name = tarinfo.name
            if tarinfo.isreg():
                try:
                    filename = f'{extractdir}/{name}'
                    os.rename(os.path.join(tmp, name), filename)
                    continue
                except:
                    pass
            os.makedirs(f'{extractdir}/{name}', exist_ok=True)
        tar.close()
        return True

    return False
