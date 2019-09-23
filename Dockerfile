FROM pennlabs/django-base

RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates jp2a \
    && rm -rf /var/lib/apt/lists/*