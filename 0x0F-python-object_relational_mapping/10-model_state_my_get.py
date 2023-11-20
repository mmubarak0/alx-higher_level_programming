#!/usr/bin/python3
"""Prints the first State object."""

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    import sys

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    host_name = "localhost"
    port = 3306

    if ";" in state_name:
        state_name = ""

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                    user, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).filter(State.name == state_name).one()
        print(state.id)
    except Exception as e:
        print('Not found')
    session.close()
