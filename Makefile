install:
    RUN python -m venv /py && \
        /py/bin/pip install --upgrade pip && \
        apk add --update --no-cache postgresql-client && \
        apk add --update --no-cache --virtual .tmp-build-deps \
            build-base postgresql-dev musl-dev && \
        if [ $DEV=true ]; \
            then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
        else  \
            /py/bin/pip install -r /tmp/requirements.txt ; \
        fi && \
        rm -rf /tmp && \
        apk del .tmp-build-deps && \
        adduser \
            --disabled-password \
            --no-create-home \
            django-user