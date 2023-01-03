import React, { useState } from "react";
import { Container } from 'react-bootstrap';
import Login from './views/login/Login';
import Styles from "./App.module.css";

const App = () => {
    if (isLogged) {
        return (<></>);
    } else {
        return (
            <Container className={Styles.contenedorLogin}>
                <Login />
            </Container>
        );
    }
};

export default App;