import settings
from src.controllers.index import server

#動作確認用
if __name__ == '__main__':
    server.start(settings.DEBUG)