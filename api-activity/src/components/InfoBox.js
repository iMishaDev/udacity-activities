
const InfoBox = (props) => {
    const {
        title,
        characterInfo
    } = props;
    

    return (
        <div className="detail-box-element">
            <strong className="title">{title}: </strong>
            {characterInfo}
        </div>
    );
}

export default InfoBox;
