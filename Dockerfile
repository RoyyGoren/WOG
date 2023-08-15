FROM python:alpine3.18
WORKDIR /homework
RUN pip install Flask
COPY MainScores.py .
COPY Utils.py .
COPY Scores.txt /homework/
COPY templates .
CMD python MainScores.py 

