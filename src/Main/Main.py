from Entity.User import User

from src.Main.ConcreteFactory import ConcreteFactory


def main():
    fac = ConcreteFactory()
    webhost = fac.CreateWebHost("localhost")
    webhost.e



if __name__ == '__main__':
    main()
