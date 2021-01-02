import react, {Component} from 'react';
import { FaTicketAlt } from 'react-icons/fa'
import Moment from 'react-moment'

class ShowBoards extends Component{
  render(){
    const BoardsItems = this.props.boards.map(item =>(
            <div>{item.title}</div>
    ));
    return(
  <div className="appointment-list item-list mb-3">
    {this.props.boards.map(item => (
      <div className="pet-item col media py-3" key={item.boardId}>
          <div className="mr-3">
            <button className="pet-delete btn btn-sm btn-danger" onClick={()=> this.props.deleteBoard(item)}><FaTicketAlt /></button>
          </div>

          <div className="pet-info media-body">
            <div className="pet-head d-flex">
              <span className="pet-name">{item.boardId} {item.title}</span>
              <span className="apt-date ml-auto"><image src={item.ImageUrl}></image></span>
            </div>

            <div className="owner-name">
              <span className="label-item">{item.Description}</span>
              <span>ownerName</span>
            </div>

          <div className="apt-notes">
              <Moment
                  date = {item.CreatedAt}
                  format= "MM-DD hh:mm"
              />
          </div>
        </div>
      </div>
    ))}

</div>
    );

  }
}

export default ShowBoards;
