
const FigureCard = (props) => {
    const {
        figure,
        figureImage
    } = props;
    

    return (
        <div className="card">
            <img src={figureImage} width="170" alt="" />
            <div>
                <strong>
                    {figure.name}
                </strong>
            </div> 
        </div>
    );
}

export default FigureCard;
