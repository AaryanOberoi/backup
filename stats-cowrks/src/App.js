import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import Grid from 'material-ui/Grid';
import AppBar from 'material-ui/AppBar';
import Paper from 'material-ui/Paper';
import { Card, CardActions, CardHeader, CardText } from 'material-ui/Card';
import Typography from 'material-ui/Typography';
import Flexbox from 'react-material-flexbox'
import StatsCard from './components/Cards/StatsCard';
import { ContentCopy, Store, InfoOutline, Warning, DateRange, LocalOffer, Update, ArrowUpward, AccessTime, Accessibility } from "material-ui-icons";
import ItemGrid from './components/ItemGrid';

class App extends Component {
    render() {
        return (
            <div className="App">
                <Grid container>
                <ItemGrid xs={12} sm={6} md={3}>
            <StatsCard
            icon={ContentCopy}
            iconColor="orange"
            title="Devices Online"
            description="750"
            small="Queues Active"
            statIcon={Warning}
            statIconColor="danger"
            statLink={{
                text: "Get More Space...",
                href: "#pablo"
            }}
            />
          </ItemGrid>
            </Grid>
            </div>
        );
    }
}

export default App;
