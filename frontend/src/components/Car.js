import React, { Component } from 'react';
import {Link} from 'react-router-dom';


export default class Car extends Component {

    constructor(props) {
        super(props);
        this.state = {
            make: null,
            body_type: null,
            owner_profile: {
                user: {
                    username: null,
                    email: null,
                }
            }
        }

    }

    componentDidMount() {
        var self = this;
        fetch('http://127.0.0.1:8000/api/cars/1/')
            .then(function(response) {
                return response.json();
            })
            .then(function(json) {
                self.setState(json);
            })
    }

    render() {
        return (
            <div>
                <h1>{this.state.make}</h1>
                <p>{this.state.body_type}</p>
                <p>{this.state.owner_profile.user.username}</p>
                <p>{this.state.owner_profile.user.email}</p>
            </div>
        );
    }
}

