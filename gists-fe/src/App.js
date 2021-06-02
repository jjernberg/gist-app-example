import React from 'react';
import Container from '@material-ui/core/Container';
import TextField from '@material-ui/core/TextField';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActions';
import Typography from "@material-ui/core/Typography";


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

class Gist extends React.Component {

  render() {
    return (
      <Card>
        <CardContent>
          <Typography>
            Gist ID: {this.props.gistId}
          </Typography>
          <Typography>
            Github User: {this.props.githubUsername}
          </Typography>
          <Typography>
            Description: {this.props.description}
          </Typography>
          <Typography>
            Created: {this.props.createdAt}
          </Typography>
        </CardContent>
      </Card>
    )
  }

}

class GistList extends React.Component {

  render() {
    const gists = this.props.gists;
    const gistItems = gists.map((gist) =>
      <Gist
        key={gist.gist_id}
        gistId={gist.gist_id}
        githubUsername={gist.github_user}
        description={gist.description}
        createdAt={gist.created_at}
      />
    );

    return (
      <Container>
        {gistItems}
      </Container>
    );
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
        <GistList gists={this.state.gists} />
      </Container>
    );
  }
}

export default App;
