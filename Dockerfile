FROM python:3.11.7-alpine3.19

ENV APP /Team_Project_CORE

WORKDIR $APP

RUN pip install prettytable

COPY personal_helper/personal_helper .

ENTRYPOINT ["python", "personal_helper.py"]
