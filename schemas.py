from graphene_sqlalchemy import SQLAlchemyObjectType
from pydantic import BaseModel

from models import Post


class PostSchema(BaseModel):
    title: str
    content: str


class PostModel(SQLAlchemyObjectType):
    class Meta:
        model = Post


class UserSchema(BaseModel):
    username: str
    password: str
