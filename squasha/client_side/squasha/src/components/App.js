import React, { Component } from 'react';
import '../css/App.css';

import AddTickets from './AddTicket'
import SearchTickets from './SearchTicket'
import ShowBoards from './ShowBoard'

class App extends Component{

  constructor() {
    super();
    this.state = {
      theBoards :[],
      lastIndex: 1
    }
  }

  componentDidMount(){
    fetch('./data.json')
      .then(response => response.json())
      .then(result =>{

        const boards = result.map(item =>{
          item.boardId = this.state.lastIndex;
          this.setState({lastIndex: this.state.lastIndex + 1});
          return item;
        });

        this.setState({
          theBoards : boards
        });

      });

  }


  render(){



  return (
    <main className="page bg-white" id="petratings">
      <div className="container">
        <div className="row">
          <div className="col-md-12 bg-white">
            <div className="container">
              <AddTickets />
              <SearchTickets/>
              <ShowBoards boards={this.state.theBoards}/>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
}

export default App;
