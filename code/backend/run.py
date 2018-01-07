from services import app, api
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', '5000'))
    debug = bool(os.environ.get('DEBUG', 'False').lower() == 'true')
    app.run(host='0.0.0.0', port=port, debug=debug)
