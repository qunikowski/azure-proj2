import os
import sqlalchemy.exc
from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
from sqlalchemy.orm import sessionmaker, declarative_base
import datetime
from collections import Counter

engine = create_engine(os.environ.get('DATABASE_URL', 'postgresql://dev:dev@localhost/dev'))
Session = sessionmaker(bind=engine)

class DBPrediction(declarative_base()):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True)
    img = Column(LargeBinary)
    tagName = Column(String)
    dateTime = Column(String)

    def __init__(self, id, img, tagName, dateTime):
        self.id = id
        self.img = img
        self.tagName = tagName
        self.dateTime = dateTime
    
    def as_dict(self):
        return {
            "id": self.id,
            "tagName": self.tagName,
            "datetime": datetime.datetime.strptime(self.dateTime, "%Y-%m-%d %H:%M:%S.%f")
        }

DBPrediction.metadata.create_all(bind=engine)

def add_prediction(img, prediction):
    session = Session()
    prediction = DBPrediction(
        None, 
        img,
        prediction.get("tagName"),
        datetime.datetime.now()
    )
    session.add(prediction)
    session.commit()
    pre_dict = prediction.as_dict()
    session.close()
    return pre_dict

def get_image(id):
    session = Session()
    pre = session.query(DBPrediction).filter(DBPrediction.id == id).one().img
    session.close()
    return image

def get_last_week_predictions():
    week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
    session = Session()
    predictions = [x.as_dict() for x in session.query(DBPrediction).all()]
    predictions = [x['tagName'] for x in predictions if week_ago < x['datetime']]
    predictions = dict(Counter(predictions))
    print(predictions)
    session.commit()
    session.close()
    return predictions
