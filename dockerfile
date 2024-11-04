FROM python:3.12.7-slim-bookworm
WORKDIR /home
COPY . .
EXPOSE 8000
RUN pip install -r requirements.txt
CMD ["uvicorn","main:app","--reload", "--port","8000"]
# uvicorn main:app --reload

