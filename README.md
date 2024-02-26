# FSBC
1) Project Description:
   - Our project will find the closest satellite to the user's current location by querying the N2YO api. A song is then played which is related to that satellite’s country of origin (probably the national anthem of that country). The songs will be provided using the Spotify API. The list of satellites found will also be stored in a log for future reference so users can see a list of all seen satellites.

2) Product Requirements
   - Goal: Create a web-interface that allows a user to see what satellites pass over them and play a song corresponding to that satellites country of origin.
   - Non-Goal: The web-interface will not track satellites leaving the region above the query. A new query is only made when the previous song ends.
   - Non-Functional Requirements: Song / Satellite Metadata
		- Functional Requirements:
			- N2YO Satellite API connection
			- Spotify API connection
   - Non-Functional Requirements: Interactivity
		- Functional Requirements:
			- Javascript / similar web-embedded code
			- On-demand query capabilities (upon request)


3) Project Management
	- Theme: Provide an entertaining and varied semi-randomized audio background for as long as the user would like.
	- Epic: Provide a safe and rewarding experience for returning users
	- User story 1: As a new user, I want to feel comfortable sharing my location with this website. I don’t want my location being leaked online. (Security)
		- Task: make sure all data is secured
   			- Ticket 1: make sure important data is made private and only kept inside our own secure data fields
         			- Look into ways to make sure we are using the most secure methods of storing data available to us
   			- Ticket 2: Only ask for location based on users preferences 
         			-Provide a way for users to input how specific their locational data will be
	- User story 2: As a recurring user, I want to show a friend satellites that frequent my location. Then we can compare how our seen satellites differ based on our locations.
		- Task: Store previously seen satellites in a per-user fashion (Replicability)
   			- Ticket 1: Create a DB to store seen satellites for a particular user key
         			-Users likely want to be able to return and continue their experience seamlessly
   			- Ticket 2: DB security must be maintained to prevent user locational data from being misused
         			-Due to the nature of geographic queries, user data must be protected to ensure privacy and safe-use of the web interface.

