FROM python:3.12.6-slim

ENV ADGUARD_URL="https://adguard"
ENV USERNAME="admin"
ENV PASSWORD=""
ENV ADLIST_URL="https://v.firebog.net/hosts/lists.php?type=tick"

WORKDIR /app
COPY * /app
RUN pip install -r requirements.txt

CMD python main.py --adguard_url ${ADGUARD_URL} --username ${USERNAME} --password ${PASSWORD} --adlist_url ${ADLIST_URL}
