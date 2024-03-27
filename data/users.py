import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class Users(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True,autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.Text)
    hashed_password = sqlalchemy.Column(sqlalchemy.Text)
    is_admin = sqlalchemy.Column(sqlalchemy.Boolean)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)