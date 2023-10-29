FROM python:3.8
#RUN apk --no-cache add python3
#ADD repositories /etc/apk/repositories
#RUN apk --no-cache add py3-numpy@community
#RUN apk add py3-numpy
#RUN pip3 install fastapi
#RUN apk add --no-cache bash
WORKDIR /app
COPY colorneuron.py /app/colorneuron.py
RUN pip install numpy fastapi python-multipart uvicorn
CMD ["python", "colorneuron.py"]
EXPOSE 8000
