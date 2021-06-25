import mask from '../assets/swmask.jpeg'


const CharacterCard = (props) => {
    const {
        getCharacter, 
        character
    } = props;
    

    return (
        <div className="character-box" onClick={() => getCharacter(character.url)} key={character.name}>
            <div>
                <img src={mask} className="character-img" alt={character.name} />
            </div>
            <h3>
                {character.name}
            </h3>
        </div>
    );
}

export default CharacterCard;
