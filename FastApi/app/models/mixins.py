from sqlalchemy import Column, TIMESTAMP as Timestamp, text


class TimstampMixin(object):
    create_at = Column(Timestamp,nullable=True, server_default =text("current_timestamp"))
    updated_at = Column(Timestamp,nullable=True, server_default =text("current_timestamp on update current_timestamp"))
