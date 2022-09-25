# syntax=docker/dockerfile:latest
FROM ubuntu:jammy AS builder

# Enable APT package caching
RUN rm -f /etc/apt/apt.conf.d/docker-clean && \
    echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache

# Install base packages
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        binutils \
        libc6-dev \
        python3-minimal

RUN useradd -u 1000 jail

FROM pwn.red/jail

COPY --from=builder / /srv

COPY challenge.py /srv/app/run

RUN chmod 755 /srv/app/run

ENV JAIL_TIME 60
ENV JAIL_CONNS_PER_IP 5
ENV JAIL_MEM 50M
ENV JAIL_TMP_SIZE 5M
ENV JAIL_ENV_PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
