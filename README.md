# I BANDITI RESTAURANT BOOKING SYSTEM

I Banditi is a full‑stack, responsive website built for a fictional restaurant business as part of a portfolio project.

The website allows users to view the menu and, once registered, book, view, edit, and delete table reservations. It is built with Django, Bootstrap 5, and deployed on Heroku with a PostgreSQL database.

<img src="static/images/all-devices-white.webp" alt="Responsive Mockup" width="70%">

**Live Website:** https://andreaspe-project-4-3264390b1a4b.herokuapp.com/

---

## Table of Contents

- [Overview](#overview)
- [Agile Methodology](#agile-methodology)
- [User Experience (UX)](#user-experience-ux)
  - [Strategy / Site Goals](#strategy--site-goals)
  - [Scope / User Stories](#scope--user-stories)
  - [Structure / Design Choices](#structure--design-choices)
  - [Surface](#surface)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Challenges & Solutions](#challenges--solutions)
- [Bugs](#bugs)
- [Deployment](#deployment)
  - [Forking the GitHub Repository](#forking-the-github-repository)
  - [Creating a Local Clone](#creating-a-local-clone)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

---

## Overview

I Banditi is a responsive, mobile‑first restaurant booking system. Users can browse the menu, register for an account, and manage their own reservations.
The project demonstrates full CRUD functionality, authentication, and production‑ready deployment.

---

## Agile Methodology

The project was developed iteratively, using GitHub Issues to track user stories and tasks. Stories were prioritized using the MoSCoW method (Must Have, Should Have, Could Have).
Iterative testing and feedback loops guided refinements until the Minimum Viable Product was achieved.

---

## User Experience (UX)

### Strategy / Site Goals

- Provide a simple, intuitive booking system for customers.
- Ensure responsive design across devices.
- Deliver a professional, production‑ready deployment.

### Scope / User Stories

**As a User**

- Register an account to access the booking system.
- Log in/out securely.
- Create, view, edit, and delete my reservations.
- Receive clear success/error messages.
- Access the site on mobile, tablet, and desktop.

**As an Administrator**

- See all the bookings in the admin panel.
- Be able to edit or delete user bookings.
- Prevent the users from making bookings with dates in the past.

**As a Developer**

- Ensure static assets are cached correctly.
- Pass Lighthouse and W3C validation.
- Keep production secure with `DEBUG=False`.

---

## Structure / Design Choices

- **Navigation**: Responsive navbar with logo, links to Home, Menu, Bookings, Register/Login/Logout.

  <img src="static/images/navbar.png" alt="Expanded Navbar">

  <img src="static/images/navbar_2.png" alt="Clamed up Navbar">

  <br><br>

- **Footer**: Social links, consistent across all pages.

  <img src="static/images/footer.png" alt="Footer with social links">

  <br><br>

- **Home Page**: Hero section with CTA buttons to Menu and Bookings.

<img src="static/images/home.png" alt="The home page" width="50%">

<br><br>

- **Menu Page**: Categorized dishes, dish description and pricing.

<img src="static/images/menu.png" alt="The menu page" width="50%">

<br><br>

- **Authentication**: Register, Login, Logout via Django Allauth

<img src="static/images/register.png" alt="The user registration page" width="50%">

<img src="static/images/log_in.png" alt="The user log in page" width="50%">

<img src="static/images/log_out.png" alt="The user log out page" width="50%">

<br><br>

- **Booking Pages**: CRUD functionality for logged‑in users.

<img src="static/images/create.png" alt="Create a booking page" width="50%">

<img src="static/images/read.png" alt="See all user bookings page" width="50%">

<img src="static/images/update.png" alt="Update a booking page" width="50%">

<img src="static/images/delete.png" alt="Delete a booking page" width="50%">

---

## Surface

- **Colour Scheme**: Neutral background with Bootstrap accent colours.
- **Typography**: Sans‑serif fonts for readability.
- **Icons**: Font Awesome/Bootstrap icons for social links and navigation.
- **Accessibility**: Improved via Lighthouse audits, ARIA labels, and alt text

---

## Features

### Existing Features

- Responsive navigation and footer.
- Home page with hero and CTAs.
- Menu page with categories.
- User authentication (Register, Login, Logout).
- Booking system (Create, Read, Update, Delete).
- Validation on booking forms (dates, time, number of guests).
- Prevent users from making a booking in the past.
- Prevent users from seeing and editing other users bookings.
- Sign out users upon browser close or after 30 minutes.

<img src="static/images/session_expiration.png" alt="Session expiration settings" width="50%">

- Success/error messages.

<img src="static/images/messages.png" alt="User action confirmation message" width="50%">

<img src="static/images/messages_2.png" alt="User action confirmation message" width="50%">

<img src="static/images/messages_3.png" alt="User action confirmation message" width="50%">

- Django Admin panel for superusers.

<img src="static/images/admin_panel.png" alt="Django admin panel" width="50%">
