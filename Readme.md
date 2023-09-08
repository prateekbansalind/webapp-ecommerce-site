---

# E-commerce Web Service

This repository contains the Flask web application for our e-commerce platform. It showcases products, current sales, and provides customer support information.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup & Installation](#setup--installation)
- [Running with Docker](#running-with-docker)
- [Accessing the Application](#accessing-the-application)


## Features

- **Home Page**: Provides an overview of our e-commerce site.
- **Products Page**: Showcases our range of products.
- **Sale Page**: Highlights ongoing sales and promotions.
- **Support Page**: Gives information about our customer support.

## Prerequisites

- Python 3.8 or newer
- Flask
- Docker (for containerized deployment)

## Setup & Installation

1. Clone this repository:
```bash
git clone https://github.com/prateekbansalind/webapp-ecommerce-site.git
```

2. Navigate to the project directory:
```bash
cd webapp-ecommerce-site
```

5. Run the Flask application:
```bash
python run.py
```

## Running with Docker

1. Build the Docker image:
```bash
docker build -t webapp-ecommerce:v1.0 .
```

2. Run the container:
```bash
docker run -p 8080:80 webapp-ecommerce:v1.0
```

## Accessing the Application

The application should be accessible at: [http://localhost:8080/]

