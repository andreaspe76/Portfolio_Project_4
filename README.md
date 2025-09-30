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

## Testing

- **Lighthouse**: Passed performance, accessibility, best practices, SEO.

<img src="static/images/lighthouse.png" alt="Lighthouse result image" width="50%">

<br><br>

- **W3C HTML & CSS Validators**: No errors.

<img src="static/images/w3c_html.png" alt="W3C html validation" width="50%">

**Validation Link:** https://validator.w3.org/nu/?doc=https%3A%2F%2Fandreaspe-project-4-3264390b1a4b.herokuapp.com%2F/

<img src="static/images/w3c_css.png" alt="W3C css validation" width="50%">

**Validation Link:** https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fandreaspe-project-4-3264390b1a4b.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en/

<br><br>

- **Cross‑browser/device**: Tested on Chrome, Edge, Safari, mobile devices.

- **Functional testing**:

  - Register/Login/Logout works as expected.
  - Booking CRUD tested.
  - Validation prevents past dates, booking during no working hours, invalid number of guests.
  - Bookings can be accessed, edited and deleted from the Django admin panel.

---

## Challenges & Solutions:

- **Preventing Users from Booking in the Past.**
- Challenge: Initially, the reservation form allowed users to select any date, including past dates. This would have made the booking system unrealistic and potentially confusing.
- Solution: I implemented custom validation logic in the form to restrict the date field. The validation checks that the chosen date is today or in the future.
- Result: Users can now only book valid dates within the allowed range, ensuring the system reflects real‑world restaurant operations.

<br><br>

- **Restricting Access to Other Users’ Bookings.**
- Challenge: By default, Django models and views don’t automatically restrict which records a logged‑in user can see. Without extra logic, one user could potentially view or manipulate another user’s reservations by guessing URLs or IDs.
- Solution: I filtered all booking queries by the currently logged‑in user (request.user). In the views, only reservations belonging to that user are retrieved. Update and delete actions are also restricted so that a user can only edit or cancel their own bookings.
- Result: Each user now has a private booking history. This prevents unauthorized access and ensures data privacy, which is critical for a production‑ready system.

<br><br>

- **Implementing Clear Confirmation Messages.**
- Challenge: During early testing, users had no feedback after actions like logging in, logging out, or creating a booking. This made the experience confusing, as it wasn’t clear whether the action had succeeded.
- Solution: I used Django’s built‑in messages framework to display contextual alerts. Success messages appear in the navbar after login, logout, booking creation, update, or cancellation. Error messages are shown inline on forms when validation fails.
- Result: Users now receive immediate, clear feedback for every action. This improves usability and builds trust in the system.

---

## Bugs:

- **Resolved:** dj-database-url not recognised in the virtual environment, booking on a past date possible.

<br><br>

- **dj-database-url not recognised in the virtual environment.**
- Symptom: Even though dj-database-url was installed and listed in requirements.txt, Django raised an ImportError when trying to run migrations or start the server.
- Cause: The package was installed globally but not properly registered in the active virtual environment.
- Fix: Reinstalled the package inside the virtual environment with:
  <br>
  **pip install dj-database-url**
  <br>
  **pip freeze > requirements.txt**
  <br>
  Then redeployed to Heroku to ensure the dependency was available in production.
- Result: Django successfully connected to the PostgreSQL database using the parsed DATABASE_URL.

<br><br>

- **Booking on a past date possible**
- Symptom: During testing, the reservation form allowed users to select dates that were already in the past. This meant a user could, for example, book a table for “yesterday,” which is not realistic for a restaurant booking system.
- Cause: The initial form and model validation only checked that the date field was a valid date, but did not restrict it relative to the current date.
- Fix: I added custom validation logic in the form’s clean_date method to ensure that:
  <br>
  The booking date must be today or later.
  <br>
  <img src="static/images/snippet.png" alt="Code snippet" width="50%">
  <br>
  Result: Users can no longer make bookings in the past. The form now enforces realistic booking behaviour, improving both data integrity and user experience.

- **Remaining**: Minor button alignment issue (cosmetic, does not affect functionality),
