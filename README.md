# srt-channel-management-system
A Django-based web application for managing broadcast channel delivery configurations and SRT service records.

# SRT Channel Management System

A web-based application designed to centralize and manage broadcast channel delivery configurations, customer information, and streaming service records.

## Overview

SRT Channel Management System simplifies the organization of broadcast delivery services by providing a centralized interface for managing customers, channels, protocols, network endpoints, and service statuses.

The application was developed to address operational challenges encountered in broadcast engineering environments and has been deployed on a Linux server.

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap, JavaScript, AJAX
- **Database:** PostgreSQL (SQLite during initial development)
- **Deployment:** Ubuntu Linux, Gunicorn, systemd
- **Web Server:** Nginx (configured during deployment)

## Features

- Create, view, edit, and manage broadcast delivery service records
- Manage customers and television channels
- Search and filter services by status
- Track active, test, and removed services
- Configure delivery protocols, network addresses, and ports
- Record SRT Caller and Listener modes
- User authentication and administrative access
- Dynamically add customers and channels using AJAX-powered forms

## Architecture

Browser → Django Web Application → PostgreSQL Database

The application uses Django's ORM for database operations, Django templates for the user interface, and Gunicorn for application hosting on Ubuntu Linux.

## Deployment

The application has been deployed on a dedicated Ubuntu Linux system using PostgreSQL, Gunicorn, and systemd.

## Project Status

**Deployed — Portfolio Documentation**

The application manages streaming service configuration records. It does not automatically provision SRT streams or provide real-time stream monitoring.

## Screenshots

Screenshots will be added here.

## Author

Walter Vasquez

