# FoodieWoodie

FoodieWoodie is a web application that allows users to discover and share their favorite food hubs, explore new recipes, and connect with a community of food enthusiasts. It utilizes HTML, CSS, and Bootstrap for the frontend, while the backend is powered by Python, Django, and PostgreSQL. The project integrates two APIs, Trueway geocoding and Maptoolkit, to provide location-based services.

## Key Features

1. **User Signup/Login:** Users can create an account or log in to access personalized features and interact with the FoodieWoodie community.

2. **Home Page:** The home page showcases featured food hubs along with their locations and votes. Users can quickly browse through popular food destinations and get a glimpse of their popularity.

3. **Voting System:** Users can upvote or downvote food hubs, contributing to their overall rating. This allows the community to collectively determine the best food hubs.

4. **Explore New Food Hubs:** Users can feature newly discovered food hubs and earn credibility points. The credibility points are calculated based on the total upvotes minus the total downvotes received.

5. **Recipe Page:** FoodieWoodie includes a dedicated recipe page where users can share their unique recipes with others. This encourages a collaborative environment for culinary enthusiasts to exchange cooking ideas and techniques.

6. **Nearby Search:** One of the standout features of FoodieWoodie is the ability to search for nearby food hubs. Users can input an address and radius (in kilometers), and the application will provide a list of food hubs within the specified range.

7. **User Profile:** Each user has their own profile page that displays a collection of their featured food hubs and shared recipes. This personalized space allows users to showcase their contributions and keep track of their culinary journey.

## Future Work

In the future, the project aims to optimize the database operations for enhanced performance. This includes implementing a database structure with a time complexity of O(Nlog(N)) and optimizing the nearby search feature by utilizing a quadtree data structure. By leveraging S2 cell IDs, the application can efficiently denote latitude and longitude, resulting in faster query retrieval with a time complexity of O(log(N)).

## Installation

To run FoodieWoodie locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/FoodieWoodie.git`
2. Navigate to the project directory: `cd foodiewoodie-project`
3. Set up a virtual environment (optional but recommended): `python3 -m venv venv`
4. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`
6. Set up the database connection in the settings file (`settings.py`) using your PostgreSQL credentials.
7. Apply the database migrations: `python manage.py migrate`
8. Start the development server: `python manage.py runserver`
9. Open your web browser and visit `http://localhost:8000` to access FoodieWoodie.

Make sure you have the necessary API keys for Trueway geocoding and Maptoolkit and update them in the appropriate configuration files.

## Contributing

FoodieWoodie welcomes contributions from the open-source community. If you would like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch from the `main` branch: `git checkout -b feature/your-feature-name`
3. Make your modifications and commit the changes.
4. Push your branch to your forked repository: `git push origin feature/your-feature-name`
5. Open a pull request on the main

 repository, describing your changes and improvements.

Please ensure that your code adheres to the project's coding conventions and includes appropriate tests.

## License

FoodieWoodie is released under the [MIT License](LICENSE).

## Acknowledgments

FoodieWoodie makes use of the following APIs:

- [Trueway geocoding](https://www.trueway.com/geocoding-api/)
- [Maptoolkit](https://www.maptoolkit.net)

Special thanks to the developers and contributors of these APIs for enabling the functionality of FoodieWoodie.

## Contact

If you have any questions, suggestions, or feedback, please reach out to the FoodieWoodie development team at [imprakhar.ps@gmail.com](mailto:imprakhar.ps@gmail.com).
