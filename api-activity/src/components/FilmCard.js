
const FilmCard = (props) => {
    const {
        film
    } = props;
    

    return (
       <> 
            <div className="card card-background">
            <strong> {film.title} </strong>
                <div>
                    <div><small>Producer:  {film.producer} </small></div>
                    <div><small>Director:  {film.director}</small>  </div>
                    <div><small>release date: {film.release_date}</small>  </div>
                </div>
            </div>
    </>
    );
}

export default FilmCard;
