# WebLOAD 13.4.0 Dependencies Installation Guide

## Overview
During WebLOAD setup, certain system libraries may need to be installed depending on your Linux distribution. This guide provides the installation commands for different Linux distributions.

## CentOS 9 / AlmaLinux 9 / RHEL 9

If you encounter errors like `error while loading shared libraries: libnsl.so.1: cannot open shared object file`, install the required dependencies:

```bash
yum update -y && \
yum install -y --allowerasing \
    curl \
    tar \
    gzip \
    wget \
    libnsl \
    libstdc++ \
    glibc \
    libxcrypt-compat
```

### Required Packages Explained:
- **curl**: Download files from remote servers
- **tar**: Extract tar archives
- **gzip**: Compression utility
- **wget**: Alternative download tool
- **libnsl**: Network Services Library (required for network operations)
- **libstdc++**: C++ Standard Library
- **glibc**: GNU C Library
- **libxcrypt-compat**: Legacy password encryption compatibility

## Ubuntu 20.04 / 22.04 / Debian-based

If you encounter similar library errors, install the required dependencies:

```bash
apt-get update && \
apt-get install -y \
    curl \
    tar \
    gzip \
    wget \
    libnsl2 \
    libstdc++6 \
    libc6 \
    libgcrypt20
```

### Required Packages Explained:
- **curl**: Download files from remote servers
- **tar**: Extract tar archives
- **gzip**: Compression utility
- **wget**: Alternative download tool
- **libnsl2**: Network Services Library (Debian/Ubuntu equivalent of libnsl)
- **libstdc++6**: C++ Standard Library
- **libc6**: GNU C Library
- **libgcrypt20**: Cryptography library

## Installation Steps

### For CentOS 9 / AlmaLinux 9 / RHEL 9:

1. Extract WebLOAD:
```bash
tar -zvxf WebLoad-linux-v13.4.0.231_64.tar.gz
cd radview/webload13.4.0_64/linux/bin
```

2. Install dependencies (if not already installed):
```bash
yum install -y --allowerasing libnsl libstdc++ glibc libxcrypt-compat
```

3. Run setup:
```bash
./setup -y
```

### For Ubuntu / Debian-based systems:

1. Extract WebLOAD:
```bash
tar -zvxf WebLoad-linux-v13.4.0.231_64.tar.gz
cd radview/webload13.4.0_64/linux/bin
```

2. Install dependencies (if not already installed):
```bash
apt-get update && \
apt-get install -y libnsl2 libstdc++6 libc6 libgcrypt20
```

3. Run setup:
```bash
./setup -y
```

## Docker Installation

### AlmaLinux 9 Dockerfile

```dockerfile
FROM almalinux:9

# Install dependencies for AlmaLinux 9
RUN yum update -y && \
    yum install -y --allowerasing \
    curl \
    tar \
    gzip \
    wget \
    libnsl \
    libstdc++ \
    glibc \
    libxcrypt-compat && \
    yum clean all

# Download and extract WebLoad
RUN mkdir -p /opt/webload && \
    curl -o /tmp/WebLoad-linux-v13.4.0.231_64.tar.gz \
    http://10.0.1.11/data/RND/CM/WebLOAD13.4.0/Build13.4.0.231/WebLoad-linux-v13.4.0.231_64.tar.gz && \
    tar -xzf /tmp/WebLoad-linux-v13.4.0.231_64.tar.gz -C /opt/webload && \
    rm /tmp/WebLoad-linux-v13.4.0.231_64.tar.gz

# Run WebLoad setup
RUN /opt/webload/radview/webload13.4.0_64/linux/bin/setup -y

# Set working directory
WORKDIR /opt/webload

CMD ["/bin/bash"]
```

### Ubuntu Dockerfile

```dockerfile
FROM ubuntu:22.04

# Install dependencies for Ubuntu
RUN apt-get update && \
    apt-get install -y \
    curl \
    tar \
    gzip \
    wget \
    libnsl2 \
    libstdc++6 \
    libc6 \
    libgcrypt20 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download and extract WebLoad
RUN mkdir -p /opt/webload && \
    curl -o /tmp/WebLoad-linux-v13.4.0.231_64.tar.gz \
    http://10.0.1.11/data/RND/CM/WebLOAD13.4.0/Build13.4.0.231/WebLoad-linux-v13.4.0.231_64.tar.gz && \
    tar -xzf /tmp/WebLoad-linux-v13.4.0.231_64.tar.gz -C /opt/webload && \
    rm /tmp/WebLoad-linux-v13.4.0.231_64.tar.gz

# Run WebLoad setup
RUN /opt/webload/radview/webload13.4.0_64/linux/bin/setup -y

# Set working directory
WORKDIR /opt/webload

CMD ["/bin/bash"]
```

## Troubleshooting

### Common Errors:

**Error: `error while loading shared libraries: libnsl.so.1: cannot open shared object file`**
- Solution: Install `libnsl` (CentOS/RHEL) or `libnsl2` (Ubuntu/Debian)

**Error: `error while loading shared libraries: libstdc++.so.6: version GLIBCXX_x.x.xx not found`**
- Solution: Install or upgrade `libstdc++` or `libstdc++6`

**Error: Certificate verification failed during setup**
- This is expected in Docker environments where systemd is not running
- The setup will continue and install TestTalk service configuration

## References

- [WebLOAD Documentation - Installation](https://github.com/radview/webload-documentation/blob/main/docs/installation.md)
- AlmaLinux Package Repository: https://packages.almalinux.org/
- Ubuntu Packages: https://packages.ubuntu.com/
