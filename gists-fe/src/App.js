import React from 'react';
import Container from '@material-ui/core/Container';

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
      </Container>
    );
  }
}

export default App;
