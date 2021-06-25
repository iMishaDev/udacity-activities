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
    // getAllCharacter();
    // getCharacter();
    return () => { isMountedRef.current = false; };
  }, [])



  return (
    <div className="App">
      <div className="container">
        <div id='stars'></div>
        <div className="characters-box">
          { !_.isEmpty(characters) && 
          characters.map((character) => 
          (<CharacterCard character={character} getCharacter={()=>console.log('call getCharacter')} />
          ))}
          { _.isEmpty(characters) && 
            (
              <div> No Characters to show </div>
            )}
        </div>

      <div className="detail-box">
        <div className="detail-content"> 
          <div>
            { !_.isEmpty(selectCharacter) && (
              <>
                <InfoBox title="Name" characterInfo={selectCharacter.name} />
                <InfoBox title="Birth Year" characterInfo={selectCharacter.birth_year} />
                <InfoBox title="Eye Color" characterInfo={selectCharacter.eye_color} />
                <InfoBox title="Hair Color" characterInfo={selectCharacter.hair_color} />

                <InfoBox title="Skin Color" characterInfo={selectCharacter.skin_color} />
                <InfoBox title="Gender" characterInfo={selectCharacter.gender} />
                <InfoBox title="Height" characterInfo={selectCharacter.height} />
                <InfoBox title="Mass" characterInfo={selectCharacter.mass} />
              </>
            )}

            { _.isEmpty(selectCharacter) && (
              <>
                  <div> No Character to show </div>
              </>
            )}
              
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
