import React, { Component } from 'react';
import {Link} from 'react-router-dom';

export default class CarList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            cars:[]
        };
    }

    componentDidMount() {
        var self = this;
        fetch('http://127.0.0.1:8000/api/cars/')
            .then(function(response) {
                return response.json();
            })
            .then(function(json) {
                self.setState({cars: json});
            })
    }

    render() {
        var cars = this.state.cars;
        return (
            <div>
                {cars.map(car => (
                    <div>
                        <p>{car.make}</p>
                        <p>{car.body_type}</p>
                        <p>{car.owner_profile.user.username}</p>
                        <p>{car.owner_profile.user.email}</p>
                    </div>
                ))}
            </div>
        )
    }
}