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

<br><br>

- Success/error messages.

<img src="static/images/messages.png" alt="User action confirmation message" width="50%">

<img src="static/images/messages_2.png" alt="User action confirmation message" width="50%">

<img src="static/images/messages_3.png" alt="User action confirmation message" width="50%">

<br><br>

- Django Admin panel for superusers.

<img src="static/images/admin_panel.png" alt="Django admin panel" width="50%">

### Future Features

- Custom admin dashboard outside Django admin.
- Email confirmations/reminders.
- Password reset functionality.
- Customer reviews/testimonials.
- Prevent double booking.
- Able to signup with email.

---

## Technologies Used

**Languages**: HTML5, CSS3, Python

- HTML5 – Provided the semantic structure of the website, ensuring accessibility and compatibility across browsers.
- CSS3 – Used for styling, layout, and responsive design, with Bootstrap classes supplemented by custom CSS tweaks.
- Python 3 – The core programming language used with Django to handle backend logic, form validation, and database interactions.

<br><br>

**Frameworks/Libraries**: Django 4.x, Bootstrap 5, Django Allauth, WhiteNoise, Gunicorn, Psycopg2

- Django 4.x – The main web framework, providing the MVC structure, ORM for database queries, authentication system, and built‑in admin panel.
- Bootstrap 5 – Frontend framework used for responsive grid layout, navigation bar, buttons, and form styling.
- Django Allauth – Simplified user authentication and registration, handling login, logout, and account management securely.
- WhiteNoise – Enabled efficient serving of static files (CSS, JS, images) directly from Django in production, with cache‑control headers.
- Gunicorn – A WSGI HTTP server used to run the Django application on Heroku.
- Psycopg2 – PostgreSQL database adapter for Python, allowing Django to communicate with the production database.

<br><br>

**Database**: PostgreSQL (Heroku)

- PostgreSQL (Heroku) – Relational database used in production. Hosted via Heroku’s Postgres add‑on, replacing the default SQLite used in local development.

<br><br>

**Tools**: GitHub, VS Code, Heroku, W3C Validators, Lighthouse, Chrome DevTools, Pexels/Pixabay (images)

- GitHub – Version control and repository hosting, also used for issue tracking and Agile methodology (user stories, Kanban board).
- VS Code – Local development environment, with integrated terminal and extensions for Python/Django.
- Heroku – Cloud platform used for deployment, environment variable management, and database hosting.
- W3C HTML & CSS Validators – Ensured semantic, standards‑compliant markup and styling.
- Lighthouse (Chrome DevTools) – Audited performance, accessibility, SEO, and best practices, guiding improvements.
- Chrome DevTools – Used extensively for debugging layout issues, testing responsiveness, and inspecting network requests.
- Pexels / Pixabay – Sources of royalty‑free images used in the project (hero images, menu illustrations).

---
