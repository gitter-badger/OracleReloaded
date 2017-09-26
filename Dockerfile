FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install all dependancies
RUN pip install -r requirements.txt

EXPOSE # PORT NUMBER

CMD ["python3.6, "main.py", "-p xyz"]

