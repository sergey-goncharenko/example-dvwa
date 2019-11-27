FROM vulnerables/web-dvwa

COPY mysql /var/lib/mysql

ENTRYPOINT ["/main.sh"]
