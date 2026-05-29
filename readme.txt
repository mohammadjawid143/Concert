# TicketSphere :An All-in-One Concert Booking Platform

 #### Video Demo: <https://youtu.be/3so1Loc91MA?si=LsNXFRThHO0Vk87K>

 #### Description:
Overview The project,
 TicketSphere, is a complex web-based platform designed to facilitate an easy and effective process of booking concert tickets. It features intuitive navigation, full details about the concerts, and a powerful backend side. From casual users to event organizers, the platform will satisfy a wide range of user needs.
The first view when the user enters the homepage is beautiful and neat. In this context, the most critical part of a web page is the top navigation bar, including: 
• Logo and Platform Name: This is located on the left and is intended for branding.
• Essential Buttons: On the right-hand side, it contains the Home, Login, and Register buttons. Once they are logged in, these will be replaced by Profile and Logout.
• Menu Dropdown: The menu allows users to filter the concerts by location and time. Upon selection, users are taken to detailed lists of concerts that they prefer.
• Cart Icon: Allows for easy access to the shopping cart, where a user can complete a ticket purchase.
The homepage also includes a search bar to make it easier for users to find the concerts they are interested in. Immediately after that, one can view the total number of concerts currently available on the site. In the main content section, a list of concerts shows, including venue, date, and pricing. Clicking a concert opens up a more detailed page about it.
For superusers, or administrators, this interface changes to an advanced management tool. Instead of a "Buy Ticket" button, superusers will see an "Edit" button, which will enable them to edit concert details directly. These edits are reflected across the platform in real time.
To enhance user interaction, there is a carousel slider that displays featured concerts along with their posters and promotional content. This feature adds not only dynamism to the view but also helps users find out about popular or upcoming events.
Detailed Features and Functionalities
User-Friendly Homepage
The homepage has been designed to be simple and handy. At the top, one can see fast links to other sections using the navbar or explore concerts laid out in a clean, grid-style manner. Each concert card would include:
• Concert name and short description.
• Basic information: venue, date, and available seats.
• Action buttons, customized by the user's role - "Buy Ticket" in case of a regular user, "Edit" in case of a superuser.
Below the concert cards, users will have extra information and links for browsing locations or time-based categories. The search functionality further enhances that experience by enabling quick access to specific events using keywords or filters.
Advanced Profile Management
The registered user has a profile page, personal information is visible, and, if necessary, he may change it. A straightforward interface for editing the profile will also allow users to do what they need quickly. All changes were saved securely in the SQLite database, where no outsider could access user data.
It also gives the profile section, where a rundown of his activities is kept in terms of previous tickets purchased and other preferences saved. This therefore adds value by helping to keep the user's activity with the site in check.
Secure Purchases of Tickets
The platform prioritizes the security and convenience of ticket purchases. Users can add tickets to their shopping cart, review their selections, and proceed to checkout. During the purchase process, all relevant details, such as ticket price, concert location, and event date, are clearly displayed.
Superuser Capabilities
Superusers are granted special privileges to manage the platform effectively. They can:
• Edit Concerts: Modify event details, including the name, location, time, and ticket pricing.
• Edit Concert Status: Concerts' status are changed based on the availability of tickets or cancellations.
These features will help to keep the platform fresh and timely for users.

Authentication and Registration
Account Creation and Login
TicketSphere provides a very smooth process in the registration and authentication of users. In this regard, any new user can create an account on the site by sharing personal information such as their names, email addresses, and strong passwords. On completion, it readdresses the user to the login webpage with credentials to access the web-based platform.
For further security, passwords are encrypted before storage in the SQLite database, whereby data protection will be assured. Besides, the password recovery feature is available on this platform, enabling users to reset credentials via secure email verification.
Dynamic Navigation and User Roles
It navigates dynamically, depending on whether the user is logged in and based on the user's role. If a user is not logged in, there are options to log in or register. Once a user is logged in, it gives way to a Logout and Profile button that links to personalized features.
Superusers benefit from additional tools embedded within the interface, including the ability to edit concerts directly. These dynamic changes improve usability and enhance the overall experience for all users.
________________________________________
Specialized Dropdown Features
The dropdown menu in the navbar offers additional filtering options for concert exploration:
1. Location Model: This shows a categorized listing of concert venues. Every location entry has specific details such as the city, venue name, and events upcoming at every location. Users can view the listed concerts by clicking on the venue.
2. Time Model: The list of concerts sorted in chronological order aids users in quickly determining a concert that will fit into their schedule. It also maintains the status of each concert: "Available" or "Sold Out". It provides detailed information: price, promotional poster, etc.
These filters will help the users to find out events in keeping with their preferences.
________________________________________
Technology Stack
Backend Development
The backend is powered by the Django framework, a versatile and secure Python-based web framework. Django's built-in capabilities for handling user authentication, database management, and server-side logic significantly enhance the platform's reliability. The framework also allows for rapid development and easy scalability, ensuring that the system can handle an increasing number of users and events over time.
Frontend Development
The front end is developed using HTML, CSS, and JavaScript to provide a responsive and attractive interface. It includes the main elements necessary to assure smooth interaction: a navigation bar, dropdown menus, and a search box. JavaScript adds interactive elements, like a carousel slider and form validation, to enhance user experience.
Database Integration
SQLite is an economical, efficient, yet powerful relational database system. Key data stored in the database include the following: 

• User Information: User names, email addresses, and securely hashed passwords.
• Concert Details: Event names, venues, dates, prices, and availability status.

Its simplicity and reliability make SQLite an ideal choice in handling structured data of the platform while ensuring data security and integrity.
