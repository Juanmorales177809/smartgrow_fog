from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os, json
import time

Base = declarative_base()

url = "10.220.85.126"
cmd="curl -s -k " + url


class Measurement(Base):
    __tablename__ = 'measurement'
    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    timestamp = Column(String, primary_key=True)

def main():
    engine = create_engine('influxdb://smartgrow:abcd1234@172.16.20.104:8086/microclima')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = os.popen(cmd).read()
    arr = json.loads(result)
    measurement = Measurement(value=arr['variables']['temperature'], timestamp=time.time)
    session.add(measurement)
    session.commit()

    results = session.query(Measurement).filter(Measurement.value == 42).all()
    print(results)

if __name__ == "__main__":
    main()