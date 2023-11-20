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
    host_name = "localhost"
    port = 3306

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                    user, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    state = session.query(State).filter(State.name == "Louisiana")\
        .order_by(-State.id).first()

    print(state.id)

    session.close()
