from Entity.User import User

from src.Main.ConcreteFactory import ConcreteFactory


def main():
    fac = ConcreteFactory()
    fac.CreateWebHost("localhost")



if __name__ == '__main__':
    main()
