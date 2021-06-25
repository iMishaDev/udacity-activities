
## Udacity Activity Week#3 <img src="https://user-images.githubusercontent.com/12359091/123443722-d486eb80-d5de-11eb-811a-1db78c4bb925.png" width="35" />


This project is built as activity for the Full Stack Nanodegree. Students are required to complete the requirments to integrate with [SWAPI](https://swapi.dev/). the focus of this activity is to give students more practicing of APIs integration.

### about the acitivty
we all know starwars, the American epic space opera media franchise created by George Lucas, which began with the eponymous 1977 film and quickly became a worldwide pop-culture phenomenon. an open source api named [SWAPI](https://swapi.dev/) built to fetch all data related to starwars, the movies, characters, ..etc. the activity is integrating with this API and list all the characters, when clicking on a character, a details shows his general data along with the films he/she was in. also the character's Species, Starships and Vehicles. 

## setup 
all you need to do is clone this repo locally and run `npm install` then `npm run start` to start the server. 


### [SWAPI](https://swapi.dev/) review 
#### What is it ? 
The Star Wars API, or "swapi" (Swah-pee) is the world's first quantified and programmatically-accessible data source for all the data from the Star Wars canon universe!

they've taken all the rich contextual stuff from the universe and formatted into something easier to consume with software. Then they went and stuck an API on the front so you can access it all!

#### How to use it ? 
All the data is accessible through HTTP web API. Consult their [documentation](https://swapi.dev/documentation) for understanding how to use it.

Helper libraries for popular programming languages are also provided so you can consume swapi in your favourite programming language, in a style that suits you.

### Project review 
this activity is built using React Frawework, let's see how a Reaact app looks Like : 
.
```
+-- public
|   +-- index.html
+-- src
|   +-- assets
|   +-- components
|   |   +-- CharacterCard.js
|   |   +-- FigureCard.js
|   |   +-- FilmCard.js
|   |   +-- InfoBox.js
|   +-- App.css
|   +-- App.js
+-- package.json
+-- package-lock.json
+-- README.md
```

What are we interested to look at is the `App.js` file. the other files, if you know React you will be familiar with. 

in `App.js` you will find many predeclared states, characters, selected character, films, speices, starships and vehicles. these made for you to store the data coming from the API. 



## requirments 
- [ ] fetch all characters, something to note is that get characters endpoint returns a paginated list of characters, no need to implement the pagination.. you're only required to list the first page. 

- [ ] when user clicks on a character, you should fetch this character data and show it in the detailed box. initially, we're fetching the first character. 

- [ ] after recieving the character data, you will notice that its films, speices, starships and vehicles are returned ar a list of urls (their endpoints). you need to fetch each film and add it to the films list, and fetch the others the same way. so you need to create the following: 
    - `getCharacterByUrl` to fetch a certain character data.
    - `getCharacterFilmByUrl` to fetch the character Films, this function takes one url so you need to iterate through the character's films and call this function and update the films state. 
    - `getCharacterSpeiceByUrl` to fetch the character Speices, this function takes one url so you need to iterate through the character's speices and call this function and update the speices state. 
    - `getCharacterStarshipsByUrl` to fetch the character Starships, this function takes one url so you need to iterate through the character's starships and call this function and update the starships state. 
    - `getCharacterVehiclesByUrl` to fetch the character Vehicles, this function takes one url so you need to iterate through the character's vehicles and call this function and update the vehicles state. 



This is how the app should look like when you first run it : 
![Screen Shot 2021-06-25 at 5 25 55 PM](https://user-images.githubusercontent.com/12359091/123443244-68a48300-d5de-11eb-890f-60262e3db7d5.png)


and this is how it should look like after applyting the requirments:
![Screen Shot 2021-06-25 at 5 49 09 PM](https://user-images.githubusercontent.com/12359091/123443462-97baf480-d5de-11eb-9189-73a9d4510f16.png)
![Screen Shot 2021-06-25 at 5 49 14 PM](https://user-images.githubusercontent.com/12359091/123443535-a7d2d400-d5de-11eb-858d-5508767fa54c.png)


