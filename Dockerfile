FROM python:3.12

WORKDIR /web-app

COPY . .

RUN python3 -m pip install -r ./requirements.txt

EXPOSE 7860

CMD [ "python3", "app.py" ]
