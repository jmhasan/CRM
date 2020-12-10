# SQLAlchemy
from sqlalchemy.orm import *
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, or_
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine("mssql+pyodbc://:@localhost:1433/VAT?driver=SQL+Server+Native+Client+10.0")
session = sa.orm.scoped_session(sa.orm.sessionmaker(bind=engine))
Base = declarative_base()
Base.query = session.query_property()


from rest_framework import serializers

from accounts.models import Matching, Student, Ritarget


class MatchingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ritarget
        fields = '__all__'


class MatchingSerializerNew(serializers.ModelSerializer):
    class Meta:
        model = Matching
        session = session
        fields = '__all__'
