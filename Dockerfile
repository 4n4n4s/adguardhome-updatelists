FROM python:3.13.3-slim

ENV ADGUARD_URL="https://adguard"
ENV USERNAME="admin"
ENV PASSWORD=""
ENV ADLIST_URL="https://v.firebog.net/hosts/lists.php?type=tick"

RUN apt-get update && apt-get install -y cron

WORKDIR /app
COPY app/* /app
RUN pip install -r requirements.txt

# Add a cron job based on environment variable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
