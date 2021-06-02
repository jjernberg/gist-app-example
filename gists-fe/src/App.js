import React from 'react';
import Container from '@material-ui/core/Container';
import TextField from '@material-ui/core/TextField'

const axios = require('axios');

class Search extends React.Component {
  constructor(props) {
    super(props);
    this.handleKeyPress = this.handleKeyPress.bind(this);
  }

  handleKeyPress(event) {
    if(event.key === 'Enter') {
      this.props.handleSearchByUsername(event.target.value);
    }
  }

  render() {
    return (
      <TextField id="username-search" label="Search by username" onKeyPress={this.handleKeyPress} />
    )
  }

}


class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {username: '', gists: []};
    this.instance = axios.create({
      xsrfCookieName: 'csrftoken',
      xsrfHeaderName: 'X-CSRFToken'
    });
    this.handleSearchByUsername = this.handleSearchByUsername.bind(this);
  }

  handleSearchByUsername(username){
    this.instance.get('http://localhost:8000/gists/by_username/' + username + '/')
      .then(res => {
        this.setState({username: username, gists: res.data})
      })
      .catch(error => {
        // Get to error handling if I can, but API may not return errors yet
        console.log(error);
      });
  }

  render() {
    return (
      <Container fixed>
        <header className="App-header">
          <p>Gists App</p>
        </header>
        <Search handleSearchByUsername={this.handleSearchByUsername} />
      </Container>
    );
  }
}

export default App;
