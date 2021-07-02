import { useEffect, useRef, useState } from 'react';
import './App.css'
import _ from 'lodash';
import CharacterCard from './components/CharacterCard'
import FilmCard from './components/FilmCard'
import FigureCard from './components/FigureCard'
import InfoBox from './components/InfoBox'


import starshipImage from './assets/starship.png'
import vehicleImage from './assets/snowspeeder.png'
import SpecieImage from './assets/species.png'

const App = (props) => {


  const isMountedRef = useRef(true);
  const baseUrl = 'https://swapi.dev/api/';


  const [selectCharacter, setSelectedCharacter] = useState({})
  const [characters, setCharacters] = useState([])
  const [films, setFilms] = useState([])
  const [species, setSpecies] = useState([])
  const [vehicles, setVehicles] = useState([])
  const [starships, setStarships] = useState([])


  useEffect(() => {
    getAllCharacter();
    getCharacter(`${baseUrl}/people/1`)
    return () => { isMountedRef.current = false; };
  }, [])

  const getAllCharacter = async (p=1)  => {
    fetch(`${baseUrl}/people/?page=${p}`)
    .then((response) => response.json())
    .then(({results}) => {
      setCharacters(results)
    })
  }


  const getCharacter = async (url)  => {
    fetch(url)
    .then((response) => response.json())
    .then((char) => {
      setSelectedCharacter(char)
      setFilms([])
      setVehicles([])
      setSpecies([])
      setStarships([])
      char.films.map((film) => getFilms(film))
      char.species.map((specie) => getSpecies(specie))
      char.vehicles.map((vehicle) => getVehicles(vehicle))
      char.starships.map((starship) => getStarships(starship))
    })
  }


  const getFilms = async (url)  => {
    fetch(url)
    .then((response) => response.json())
    .then((f) => {
      setFilms([...films, f])
      films.push(f)
    })
  }



  const getStarships = async (url)  => {
    fetch(url)
    .then((response) => response.json())
    .then((s) => {
      setStarships([...starships, s])
      starships.push(s)
    })
  }


  const getSpecies = async (url)  => {
    fetch(url)
    .then((response) => response.json())
    .then((s) => {
      setSpecies([...species, s])
      species.push(s)
    })
  }



  const getVehicles = async (url)  => {
    fetch(url)
    .then((response) => response.json())
    .then((v) => {
      setVehicles([...vehicles, v])
      vehicles.push(v)
    })
  }




  return (
    <div className="App">
      <div className="container">
        <div id='stars'></div>
        <div id='stars2'></div>
        <div id='stars3'></div>
        <div className="characters-box">
          {characters.map((character) => (<CharacterCard character={character} getCharacter={getCharacter} />))}
        </div>

      <div className="detail-box">
        <div className="detail-content"> 
          <div>
              <InfoBox title="Name" characterInfo={selectCharacter.name} />
              <InfoBox title="Birth Year" characterInfo={selectCharacter.birth_year} />
              <InfoBox title="Eye Color" characterInfo={selectCharacter.eye_color} />
              <InfoBox title="Hair Color" characterInfo={selectCharacter.hair_color} />

              <InfoBox title="Skin Color" characterInfo={selectCharacter.skin_color} />
              <InfoBox title="Gender" characterInfo={selectCharacter.gender} />
              <InfoBox title="Height" characterInfo={selectCharacter.height} />
              <InfoBox title="Mass" characterInfo={selectCharacter.mass} />
          </div>
          
          { !_.isEmpty(films) && (
            <>
            <InfoBox title="Films" characterInfo={''} />
              <div className="list">
                {films.map((film) =>(<FilmCard film={film} />))}
              </div>
            </>
          )}
          

          { !_.isEmpty(species) && (
            <>
              <InfoBox title="Species" characterInfo={''} />
              <div className="list">
                {species.map((specie) =>(<FigureCard figure={specie} figureImage={SpecieImage} />))}
              </div>
            </>
          )}
          

          {!_.isEmpty(starships) && (
            <>
              <InfoBox title="Starships" characterInfo={''} />
              <div className="list">
                {starships.map((starship) =>
                  (<FigureCard figure={starship} figureImage={starshipImage} />))}
              </div>
            </>
          )}
          
          
          { !_.isEmpty(vehicles) && (
            <>
              <InfoBox title="Vehicles" characterInfo={''} />
              <div className="list">
                {vehicles.map((vehicle) =>
                  (<FigureCard figure={vehicle} figureImage={vehicleImage} />))}
              </div>
            </>
          )}
          </div>
          </div>
        </div>
      </div>
  );
}

export default App;
