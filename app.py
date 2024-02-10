from flask import Flask

# Crie uma instância do Flask
app = Flask(__name__)

# Defina suas rotas e lógica de aplicativo Flask abaixo

# Se você estiver usando o arquivo app.py para executar o Flask, adicione este bloco de código
if __name__ == "__main__":
    # Execute o aplicativo com Gunicorn em vez de usar o método app.run()
    # Isso permite que o Gunicorn gerencie o servidor em vez do Flask
    import os
    import sys
    from gunicorn.app.wsgiapp import WSGIApplication

    class FlaskApplication(WSGIApplication):
        def init(self, parser, opts, args):
            return {
                'bind': '{}:{}'.format(os.getenv('HOST', '127.0.0.1'), os.getenv('PORT', '5000')),
                'workers': os.getenv('WORKERS', '1')
            }

        def load(self):
            return app

    sys.argv[0] = __file__
    FlaskApplication().run()
