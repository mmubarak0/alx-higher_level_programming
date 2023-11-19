#!/usr/bin/python3
"""Lists all State objects."""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host_name = "localhost"
    port = 3306

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                    user, password, db_name, pool_pre_ping=True))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
